# -*- coding: utf-8 -*-
"""
双语文本管理模块
所有界面文字的哈尼语-汉语双语对照
"""

from typing import Dict, Optional


class BilingualText:
    """双语文本管理类"""

    def __init__(self, language: str = "bi"):
        """
        初始化

        Args:
            language: 语言模式，'zh'=仅中文，'hani'=仅哈尼语，'bi'=双语
        """
        self.language = language
        self._texts = self._init_texts()

    def _init_texts(self) -> Dict[str, Dict[str, str]]:
        """初始化双语文本库"""
        return {
            # ================== 通用文本 ==================
            "app_name": {
                "zh": "绿县文旅翻译通",
                "hani": "Lul Kul Hhaq Nao Lul",
            },
            "version": {
                "zh": "版本",
                "hani": "mal",
            },
            "loading": {
                "zh": "加载中...",
                "hani": "ciq haol...",
            },
            # ================== 主翻译页面 ==================
            "translate_han_to_hani": {
                "zh": "汉译哈尼",
                "hani": "Zul Hhaniq",
            },
            "translate_hani_to_han": {
                "zh": "哈尼译汉",
                "hani": "Hhani Zul",
            },
            "swap_languages": {
                "zh": "切换",
                "hani": "peiq",
            },
            "input_hint_chinese": {
                "zh": "请输入要翻译的中文...",
                "hani": "nisoq zul hhaniq...",
            },
            "input_hint_hani": {
                "zh": "请输入要翻译的哈尼文...",
                "hani": "nisoq zul hhani...",
            },
            "translate_button": {
                "zh": "翻译",
                "hani": "zul",
            },
            "please_input_text": {
                "zh": "请输入要翻译的内容",
                "hani": "nisoq zul hhaq niao",
            },
            "voice_input": {
                "zh": "语音输入",
                "hani": "nil zaq",
            },
            "clear_input": {
                "zh": "清空",
                "hani": "sheq pyu",
            },
            "copy_result": {
                "zh": "复制",
                "hani": "moq nee",
            },
            "share_result": {
                "zh": "分享",
                "hani": "paoq",
            },
            "play_audio": {
                "zh": "朗读",
                "hani": "nil taq",
            },
            "offline_mode": {
                "zh": "离线模式",
                "hani": "aoq neiq",
            },
            "language_switch": {
                "zh": "语言切换",
                "hani": "hhaq peiq",
            },
            "result_label": {
                "zh": "翻译结果",
                "hani": "zullul",
            },
            # ================== 词汇库页面 ==================
            "dictionary": {
                "zh": "词汇库",
                "hani": "sul pyu",
            },
            "category_daily": {
                "zh": "日常用语",
                "hani": "ssol hhaq",
            },
            "category_lvyou": {
                "zh": "旅游词汇",
                "hani": "hhaq naol",
            },
            "category_festival": {
                "zh": "节日词汇",
                "hani": "cil ceiq",
            },
            "category_food": {
                "zh": "美食词汇",
                "hani": "aol",
            },
            "category_building": {
                "zh": "建筑词汇",
                "hani": "zeil",
            },
            "category_clothing": {
                "zh": "服饰词汇",
                "hani": "aq gee",
            },
            "category_etiquette": {
                "zh": "礼仪词汇",
                "hani": "hhaq miq",
            },
            "category_direction": {
                "zh": "问路词汇",
                "hani": "diiq",
            },
            "search": {
                "zh": "搜索",
                "hani": "caol",
            },
            "search_hint": {
                "zh": "搜索词汇...",
                "hani": "caol pyu...",
            },
            "add_to_favorites": {
                "zh": "收藏",
                "hani": "ao",
            },
            "remove_favorites": {
                "zh": "取消收藏",
                "hani": "ao qif",
            },
            "play_pronunciation": {
                "zh": "播放发音",
                "hani": "nil ye",
            },
            "no_results": {
                "zh": "未找到相关词汇",
                "hani": "ul pieq",
            },
            # ================== 历史记录页面 ==================
            "history": {
                "zh": "历史记录",
                "hani": "hhaq gu",
            },
            "clear_history": {
                "zh": "清空历史",
                "hani": "sheq gu",
            },
            "no_history": {
                "zh": "暂无翻译历史",
                "hani": "ul pieq",
            },
            "delete": {
                "zh": "删除",
                "hani": "sil",
            },
            "confirm_delete": {
                "zh": "确认删除",
                "hani": "sil yol",
            },
            "confirm": {
                "zh": "确认",
                "hani": "yol",
            },
            "cancel": {
                "zh": "取消",
                "hani": "qif",
            },
            "copied": {
                "zh": "已复制到剪贴板",
                "hani": "moq nee laq",
            },
            "translation_time": {
                "zh": "翻译时间",
                "hani": "hhaq gu",
            },
            # ================== 关于页面 ==================
            "about": {
                "zh": "关于",
                "hani": "siq",
            },
            "about_app": {
                "zh": "关于绿县文旅翻译通",
                "hani": "siq lul",
            },
            "app_description": {
                "zh": "绿县文旅哈尼语-汉语双向翻译应用，服务于绿春县游客、文旅工作人员和本地哈尼群众。",
                "hani": "Lul Kul hhaq naol hhani zul hhaniq, lul cheeq hhaq naol aqma piul wul.",
            },
            "word_count": {
                "zh": "词条总数",
                "hani": "pyu mal",
            },
            "developer": {
                "zh": "开发者",
                "hani": "zairul",
            },
            "contact": {
                "zh": "联系我们",
                "hani": "nga ni caq",
            },
            "copyright": {
                "zh": "版权所有",
                "hani": "siq yul",
            },
            "disclaimer": {
                "zh": "免责声明",
                "hani": "siq yol",
            },
            # ================== 设置页面 ==================
            "settings": {
                "zh": "设置",
                "hani": "teiq",
            },
            "text_size": {
                "zh": "字体大小",
                "hani": "ceiq hha",
            },
            "text_size_normal": {
                "zh": "标准",
                "hani": "haol",
            },
            "text_size_large": {
                "zh": "大",
                "hani": "laq",
            },
            "text_size_extra_large": {
                "zh": "特大",
                "hani": "laq bol",
            },
            "voice_settings": {
                "zh": "语音设置",
                "hani": "nil teiq",
            },
            "auto_play": {
                "zh": "自动朗读",
                "hani": "ciq nil",
            },
            "history_settings": {
                "zh": "历史记录设置",
                "hani": "gu teiq",
            },
            "enable_history": {
                "zh": "启用历史记录",
                "hani": "gu yol",
            },
            "clear_all_history": {
                "zh": "清空所有历史",
                "hani": "sheq gu",
            },
            # ================== 文化科普 ==================
            "culture_card": {
                "zh": "文化小科普",
                "hani": "hhaq siq",
            },
            "culture_ten_months": {
                "zh": "十月年",
                "hani": "cilceiq",
                "intro": "哈尼族最隆重的传统节日，相当于汉族的春节。",
            },
            "culture_long_street_banquet": {
                "zh": "长街宴",
                "hani": "aol ngeq",
                "intro": '十月年期间的盛大宴席，被列入世界吉尼斯纪录，被誉为"天下第一长街宴"。',
            },
            "culture_fan_dance": {
                "zh": "棕扇舞",
                "hani": "miao seil",
                "intro": "哈尼族传统舞蹈，表演者手持棕扇，模拟棕扇鸟的优美姿态。",
            },
            "culture_tuzhangfang": {
                "zh": "土掌房",
                "hani": "zeil qei",
                "intro": "哈尼族传统民居，土木结构，层层叠叠非常有特色。",
            },
            "culture_mushroom_house": {
                "zh": "蘑菇房",
                "hani": "aq puq",
                "intro": "哈尼族传统建筑，形似蘑菇，具有独特的民族风格。",
            },
            "culture_kuzaza": {
                "zh": "矻扎扎节",
                "hani": "kul za",
                "intro": "哈尼族传统节日，通常在农历五月举行。",
            },
            # ================== 错误提示 ==================
            "error_network": {
                "zh": "网络连接失败",
                "hani": "neiq al qif",
            },
            "error_translation": {
                "zh": "翻译失败，请重试",
                "hani": "zul qif niao",
            },
            "error_voice": {
                "zh": "语音识别失败",
                "hani": "nil al qif",
            },
            "error_audio": {
                "zh": "音频播放失败",
                "hani": "nil ye qif",
            },
        }

    def get(self, key: str, lang: Optional[str] = None) -> str:
        """
        获取双语文本

        Args:
            key: 文本键名
            lang: 语言，'zh'=中文，'hani'=哈尼语，None=使用当前语言设置

        Returns:
            str: 对应语言的文本
        """
        if key not in self._texts:
            return key  # 返回原始key

        texts = self._texts[key]

        # 确定使用哪种语言模式
        if lang:
            target_lang = lang
        else:
            target_lang = self.language

        if target_lang == "zh":
            return texts.get("zh", key)
        elif target_lang == "hani":
            return texts.get("hani", texts.get("zh", key))
        else:  # bi (双语)
            zh_text = texts.get("zh", "")
            hhani_text = texts.get("hani", "")

            if zh_text and hhani_text:
                return f"{zh_text} / {hhani_text}"
            elif zh_text:
                return zh_text
            else:
                return hhani_text

    def get_both(self, key: str) -> tuple:
        """
        获取双语对照文本

        Args:
            key: 文本键名

        Returns:
            tuple: (中文文本, 哈尼语文本)
        """
        if key not in self._texts:
            return (key, key)

        texts = self._texts[key]
        return (texts.get("zh", ""), texts.get("hani", ""))

    def get_all_keys(self) -> list:
        """获取所有文本键名"""
        return list(self._texts.keys())


# 预定义实例
_bi_text = BilingualText("bi")


def t(key: str) -> str:
    """快速获取双语文本"""
    return _bi_text.get(key)


def t_zh(key: str) -> str:
    """快速获取中文文本"""
    return BilingualText("zh").get(key)


def t_hani(key: str) -> str:
    """快速获取哈尼语文本"""
    return BilingualText("hani").get(key)
