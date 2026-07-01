# -*- coding: utf-8 -*-
"""
绿县文旅哈尼语翻译通 - 主程序入口
基于Kivy框架的移动端应用
"""

import os
import sys
import json
from datetime import datetime

# 导入Kivy模块
try:
    from kivy.app import App
    from kivy.lang import Builder
    from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.floatlayout import FloatLayout
    from kivy.uix.button import Button
    from kivy.uix.label import Label
    from kivy.uix.textinput import TextInput
    from kivy.uix.scrollview import ScrollView
    from kivy.uix.recycleview import RecycleView
    from kivy.uix.popup import Popup
    from kivy.uix.spinner import Spinner
    from kivy.uix.switch import Switch
    from kivy.uix.checkbox import CheckBox
    from kivy.core.window import Window
    from kivy.metrics import dp, sp
    from kivy.properties import (
        BooleanProperty,
        StringProperty,
        ListProperty,
        ObjectProperty,
    )
    from kivy.clock import Clock
    from kivy.animation import Animation
except ImportError:
    # 如果未安装Kivy，提供降级提示
    print("请安装Kivy框架: pip install kivy")
    sys.exit(1)

# 导入本地模块
from translation_engine import TranslationEngine
from dictionary_manager import DictionaryManager
from audio_player import AudioPlayer
from storage_manager import StorageManager
from bili_text import BilingualText

# 全局配置
CONFIG = {
    "APP_NAME": "绿县文旅翻译通",
    "VERSION": "1.0.0",
    "THEME_COLOR": (0.106, 0.369, 0.125, 1),  # 墨绿 #1B5E20
    "ACCENT_COLOR": (0.302, 0.212, 0.173, 1),  # 土红 #4E342E
    "BG_COLOR": (0.980, 0.980, 0.980, 1),  # #FAFAFA
}

# Kivy样式定义
KV_CODE = """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import Spinner kivy.uix.spinner
#:import CheckBox kivy.uix.checkbox

<RootWidget>:
    transition: FadeTransition()
    SplashScreen:
        name: 'splash'
    MainTranslatorScreen:
        name: 'translator'
    DictionaryScreen:
        name: 'dictionary'
    HistoryScreen:
        name: 'history'
    AboutScreen:
        name: 'about'

<CustomButton>:
    background_color: root.bg_color
    color: root.text_color
    font_size: '18sp'
    size_hint_y: None
    height: '60dp'
    padding: 10, 5
    canvas.before:
        Color:
            rgba: root.bg_color if root.state == 'normal' else (root.bg_color[0]*0.8, root.bg_color[1]*0.8, root.bg_color[2]*0.8, 1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [10]

<CustomTextInput>:
    font_size: '18sp'
    padding: 10, 10
    background_color: 1, 1, 1, 1
    foreground_color: 0.13, 0.13, 0.13, 1
    canvas.before:
        Color:
            rgba: 0.9, 0.9, 0.9, 1
        Line:
            points: [self.x, self.y, self.x + self.width, self.y]
            width: 1

<PrimaryButton>:
    background_color: 0.106, 0.369, 0.125, 1
    color: 1, 1, 1, 1
    font_size: '18sp'
    size_hint_y: None
    height: '56dp'
    background_normal: ''
    background_down: ''
    canvas.before:
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [12]

<IconButton>:
    background_color: 0, 0, 0, 0
    color: 0.106, 0.369, 0.125, 1
    font_size: '24sp'
    size_hint: None, None
    size: '48dp', '48dp'

<SectionHeader>:
    size_hint_y: None
    height: '50dp'
    padding: 15, 0
    canvas.before:
        Color:
            rgba: 0.98, 0.98, 0.98, 1
        Rectangle:
            pos: self.pos
            size: self.size
"""


class RootWidget(ScreenManager):
    """根控件 - 屏幕管理器"""

    pass


class CustomButton(Button):
    """自定义按钮"""

    bg_color = ListProperty((0.106, 0.369, 0.125, 1))
    text_color = ListProperty((1, 1, 1, 1))


class PrimaryButton(Button):
    """主按钮样式"""

    pass


class CustomTextInput(TextInput):
    """自定义文本输入框"""

    pass


class IconButton(Button):
    """图标按钮"""

    pass


class SectionHeader(Label):
    """分段标题"""

    pass


# ================== 启动页 ==================
class SplashScreen(Screen):
    """启动页面"""

    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        self.opacity = 0
        Clock.schedule_once(self.fade_in, 0.5)

    def fade_in(self, *args):
        """淡入动画"""
        anim = Animation(opacity=1, duration=0.5)
        anim.start(self)
        Clock.schedule_once(self.check_resources, 2)

    def check_resources(self, *args):
        """检查资源后进入主页面"""
        anim = Animation(opacity=0, duration=0.3)
        anim.bind(on_complete=self.go_to_main)
        anim.start(self)

    def go_to_main(self, *args):
        """跳转到主翻译页面"""
        self.manager.current = "translator"


# ================== 主翻译页面 ==================
class MainTranslatorScreen(Screen):
    """主翻译页面"""

    # 语言方向: 0=汉译哈, 1=哈译汉
    translation_direction = 0

    # 输入文本
    input_text = StringProperty("")

    # 输出文本
    output_text = StringProperty("")

    # 离线模式开关
    offline_mode = BooleanProperty(False)

    # 按钮文字 (双语)
    btn_translate_text = StringProperty("")
    btn_swap_text = StringProperty("")
    btn_voice_text = StringProperty("")

    def __init__(self, **kwargs):
        super(MainTranslatorScreen, self).__init__(**kwargs)
        self.engine = TranslationEngine()
        self.dict_manager = DictionaryManager()
        self.storage = StorageManager()
        self.audio = AudioPlayer()

        # 初始化双语文字
        self.update_bilingual_texts()

    def update_bilingual_texts(self):
        """更新双语文字"""
        bili = BilingualText()
        if self.translation_direction == 0:
            self.btn_translate_text = bili.get("translate_han_to_hani")
            self.btn_swap_text = bili.get("swap_languages")
        else:
            self.btn_translate_text = bili.get("translate_hani_to_han")
            self.btn_swap_text = bili.get("swap_languages")
        self.btn_voice_text = bili.get("voice_input")

    def swap_direction(self, *args):
        """切换翻译方向"""
        self.translation_direction = 1 - self.translation_direction
        self.input_text = ""
        self.output_text = ""
        self.update_bilingual_texts()
        # 切换输入语言提示
        self.ids.input_field.hint_text = BilingualText().get(
            "input_hint_hani"
            if self.translation_direction == 1
            else "input_hint_chinese"
        )

    def do_translate(self, *args):
        """执行翻译"""
        text = self.input_text.strip()
        if not text:
            self.output_text = BilingualText().get("please_input_text")
            return

        # 调用翻译引擎
        if self.translation_direction == 0:
            result = self.engine.translate(
                text, "zh", "hani", offline=self.offline_mode
            )
        else:
            result = self.engine.translate(
                text, "hani", "zh", offline=self.offline_mode
            )

        self.output_text = result["text"]

        # 保存到历史记录
        self.storage.save_history(
            source_text=text,
            result_text=result["text"],
            source_lang="zh" if self.translation_direction == 0 else "hani",
            result_lang="hani" if self.translation_direction == 0 else "zh",
        )

    def start_voice_input(self, *args):
        """启动语音输入"""
        # TODO: 调用语音识别API
        pass

    def play_source_audio(self, *args):
        """播放原文朗读"""
        if self.input_text:
            lang = "zh-CN" if self.translation_direction == 0 else "hani"
            self.audio.speak(self.input_text, lang)

    def play_result_audio(self, *args):
        """播放译文朗读"""
        if self.output_text:
            lang = "hani" if self.translation_direction == 0 else "zh-CN"
            self.audio.speak(self.output_text, lang)

    def copy_result(self, *args):
        """复制译文"""
        from kivy.core.clipboard import Clipboard

        Clipboard.put(self.output_text)

    def share_result(self, *args):
        """分享译文"""
        # TODO: 调用系统分享功能
        pass

    def clear_input(self, *args):
        """清空输入"""
        self.input_text = ""


# ================== 词汇库页面 ==================
class DictionaryScreen(Screen):
    """文旅词汇库页面"""

    # 当前分类
    current_category = StringProperty("lvyou")

    # 搜索关键词
    search_keyword = StringProperty("")

    # 词条列表
    word_items = ListProperty([])

    def __init__(self, **kwargs):
        super(DictionaryScreen, self).__init__(**kwargs)
        self.dict_manager = DictionaryManager()
        self.audio = AudioPlayer()
        self.load_words("lvyou")

    def load_words(self, category, keyword=""):
        """加载词条"""
        self.current_category = category
        words = self.dict_manager.search_words(category, keyword)
        self.word_items = words

    def play_audio(self, word_item):
        """播放词条发音"""
        if "audio_hani" in word_item:
            self.audio.play(word_item["audio_hani"])

    def toggle_favorite(self, word_item):
        """收藏词条"""
        word_id = word_item.get("id")
        self.dict_manager.toggle_favorite(word_id)


# ================== 历史记录页面 ==================
class HistoryScreen(Screen):
    """翻译历史记录页面"""

    # 历史记录列表
    history_items = ListProperty([])

    def __init__(self, **kwargs):
        super(HistoryScreen, self).__init__(**kwargs)
        self.storage = StorageManager()
        self.audio = AudioPlayer()
        self.load_history()

    def load_history(self):
        """加载历史记录"""
        history = self.storage.get_history()
        self.history_items = history

    def play_item(self, item):
        """播放记录中的语音"""
        lang = "zh-CN" if item.get("source_lang") == "zh" else "hani"
        self.audio.speak(item.get("result_text", ""), lang)

    def copy_item(self, item):
        """复制记录"""
        from kivy.core.clipboard import Clipboard

        Clipboard.put(item.get("result_text", ""))

    def delete_item(self, item):
        """删除单条记录"""
        self.storage.delete_history_item(item.get("id"))
        self.load_history()

    def clear_all(self):
        """清空所有历史"""
        self.storage.clear_history()
        self.load_history()


# ================== 关于页面 ==================
class AboutScreen(Screen):
    """关于软件页面"""

    app_name = StringProperty(CONFIG["APP_NAME"])
    version = StringProperty(CONFIG["VERSION"])

    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)
        self.dict_manager = DictionaryManager()

    def get_word_count(self):
        """获取词条总数"""
        return self.dict_manager.get_total_count()


# ================== 主应用类 ==================
class LvTranslatorApp(App):
    """绿县文旅哈尼语翻译通 - 主应用类"""

    title = CONFIG["APP_NAME"]

    def build(self):
        """构建应用"""
        # 加载KV样式
        Builder.load_string(KV_CODE)

        # 创建根控件
        root = RootWidget()

        return root

    def on_start(self):
        """应用启动回调"""
        # 初始化存储
        self.storage = StorageManager()
        self.storage.init_storage()

    def on_pause(self):
        """应用暂停回调"""
        return True

    def on_resume(self):
        """应用恢复回调"""
        pass


# ================== 应用入口 ==================
if __name__ == "__main__":
    LvTranslatorApp().run()
