# -*- coding: utf-8 -*-
"""
UI组件定义
包括词条项组件、历史记录项组件等
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.core.audio import SoundLoader


class WordItemWidget(BoxLayout):
    """词条列表项组件"""

    zh_text = StringProperty("")
    hhani_text = StringProperty("")
    pronunciation = StringProperty("")
    is_favorite = BooleanProperty(False)
    audio_file = StringProperty("")

    def __init__(self, **kwargs):
        super(WordItemWidget, self).__init__(**kwargs)
        self.audio = None

    def play_audio(self):
        """播放发音"""
        if self.audio_file:
            try:
                if self.audio:
                    self.audio.stop()
                self.audio = SoundLoader.load(self.audio_file)
                if self.audio:
                    self.audio.play()
            except Exception as e:
                print(f"播放音频失败: {e}")

    def toggle_favorite(self):
        """切换收藏状态"""
        self.is_favorite = not self.is_favorite
        # 通知父组件更新收藏状态


class HistoryItemWidget(BoxLayout):
    """历史记录列表项组件"""

    source_text = StringProperty("")
    result_text = StringProperty("")
    timestamp = StringProperty("")
    source_lang = StringProperty("zh")
    item_id = StringProperty("")

    def __init__(self, **kwargs):
        super(HistoryItemWidget, self).__init__(**kwargs)
        self.audio = None

    def play_audio(self):
        """播放译文"""
        # 根据语言播放对应音频
        pass

    def copy_text(self):
        """复制译文"""
        from kivy.core.clipboard import Clipboard

        Clipboard.put(self.result_text)

    def delete_item(self):
        """删除记录"""
        # 通知父组件删除
        pass


class CategoryTabButton:
    """分类标签按钮"""

    pass


class CultureCardWidget(BoxLayout):
    """文化科普卡片组件"""

    title = StringProperty("")
    title_hani = StringProperty("")
    intro = StringProperty("")
    icon = StringProperty("")

    def __init__(self, **kwargs):
        super(CultureCardWidget, self).__init__(**kwargs)


class SearchBarWidget(BoxLayout):
    """搜索栏组件"""

    search_text = StringProperty("")
    placeholder = StringProperty("搜索...")

    def __init__(self, **kwargs):
        super(SearchBarWidget, self).__init__(**kwargs)

    def on_search(self, text):
        """执行搜索"""
        self.search_text = text


class LanguageToggleWidget(BoxLayout):
    """语言切换组件"""

    current_direction = StringProperty("zh_to_hani")

    def __init__(self, **kwargs):
        super(LanguageToggleWidget, self).__init__(**kwargs)

    def toggle(self):
        """切换翻译方向"""
        if self.current_direction == "zh_to_hani":
            self.current_direction = "hani_to_zh"
        else:
            self.current_direction = "zh_to_hani"


class BottomNavWidget(BoxLayout):
    """底部导航栏组件"""

    current_page = StringProperty("translator")

    def __init__(self, **kwargs):
        super(BottomNavWidget, self).__init__(**kwargs)

    def navigate_to(self, page_name):
        """导航到指定页面"""
        self.current_page = page_name
        # 通过事件或回调通知页面切换
