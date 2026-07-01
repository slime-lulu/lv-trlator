# -*- coding: utf-8 -*-
"""
翻译引擎模块
支持汉语-哈尼语双向翻译
包含离线翻译能力
"""

import os
import json
import re
from difflib import SequenceMatcher


class TranslationEngine:
    """翻译引擎核心类"""

    def __init__(self):
        """初始化翻译引擎"""
        self.offline_mode = True
        self.dictionaries = {}
        self.cache = {}
        self.max_cache_size = 100

        # 加载离线词库
        self._load_dictionaries()

    def _load_dictionaries(self):
        """加载离线词库"""
        base_path = os.path.join(os.path.dirname(__file__), "resources", "dictionaries")

        # 确保目录存在
        if not os.path.exists(base_path):
            os.makedirs(base_path)
            self._create_default_dictionaries(base_path)

        # 加载各分类词库
        dict_files = [
            "daily.json",  # 日常用语
            "lvyou.json",  # 旅游词汇
            "festival.json",  # 节日词汇
            "food.json",  # 美食词汇
            "building.json",  # 建筑词汇
            "clothing.json",  # 服饰词汇
            "etiquette.json",  # 礼仪词汇
            "direction.json",  # 问路词汇
        ]

        for filename in dict_files:
            filepath = os.path.join(base_path, filename)
            if os.path.exists(filepath):
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    category = filename.replace(".json", "")
                    self.dictionaries[category] = data

    def _create_default_dictionaries(self, base_path):
        """创建默认词库（首次运行）"""
        # 日常词汇
        daily_dict = {
            "greetings": [
                {"zh": "你好", "hani": "nisoq"},
                {"zh": "早上好", "hani": "nisoq ceil"},
                {"zh": "晚上好", "hani": "nisoq yeil"},
                {"zh": "再见", "hani": "haqma"},
                {"zh": "谢谢", "hani": "aqda"},
                {"zh": "对不起", "hani": "ulpuq"},
                {"zh": "没关系", "hani": "ulpuq qif"},
                {"zh": "请", "hani": "yol"},
                {"zh": "是", "hani": "ee"},
                {"zh": "不是", "hani": "qif ee"},
                {"zh": "好的", "hani": "hha"},
                {"zh": "可以吗", "hani": "naqni"},
            ],
            "numbers": [
                {"zh": "一", "hani": "teiq"},
                {"zh": "二", "hani": "nil"},
                {"zh": "三", "hani": "so"},
                {"zh": "四", "hani": "hiq"},
                {"zh": "五", "hani": "ngaq"},
                {"zh": "六", "hani": "khohh/yul"},
                {"zh": "七", "hani": "shet"},
                {"zh": "八", "hani": "hhaq"},
                {"zh": "九", "hani": "ga"},
                {"zh": "十", "hani": "ceiq"},
            ],
            "people": [
                {"zh": "我", "hani": "nga"},
                {"zh": "你", "hani": "ni"},
                {"zh": "他/她", "hani": "ma"},
                {"zh": "我们", "hani": "nga teiq"},
                {"zh": "你们", "hani": "ni teiq"},
                {"zh": "他们", "hani": "ma teiq"},
                {"zh": "爸爸", "hani": "aqpa"},
                {"zh": "妈妈", "hani": "aqma"},
                {"zh": "爷爷", "hani": "appa"},
                {"zh": "奶奶", "hani": "appa ma"},
                {"zh": "哥哥", "hani": "aqpa"},
                {"zh": "姐姐", "hani": "aqpie"},
                {"zh": "弟弟", "hani": "niu"},
                {"zh": "妹妹", "hani": "nia"},
            ],
        }

        with open(os.path.join(base_path, "daily.json"), "w", encoding="utf-8") as f:
            json.dump(daily_dict, f, ensure_ascii=False, indent=2)

    def translate(self, text, source_lang="zh", target_lang="hani", offline=True):
        """
        翻译主函数

        Args:
            text: 待翻译文本
            source_lang: 源语言 ('zh' 或 'hani')
            target_lang: 目标语言 ('zh' 或 'hani')
            offline: 是否使用离线模式

        Returns:
            dict: 包含翻译结果和状态
        """
        if not text or not text.strip():
            return {"text": "", "status": "empty"}

        # 检查缓存
        cache_key = f"{source_lang}_{target_lang}_{text}"
        if cache_key in self.cache:
            return {"text": self.cache[cache_key], "status": "cached"}

        result_text = ""

        # 分词处理
        words = self._tokenize(text)

        # 逐词翻译
        translated_words = []
        for word in words:
            translation = self._translate_word(word, source_lang, target_lang)
            translated_words.append(translation)

        result_text = "".join(translated_words)

        # 更新缓存
        if len(self.cache) >= self.max_cache_size:
            # 删除最老的缓存
            self.cache.pop(next(iter(self.cache)))
        self.cache[cache_key] = result_text

        return {
            "text": result_text,
            "status": "success" if result_text else "not_found",
        }

    def _tokenize(self, text):
        """分词处理"""
        # 简单分词：按标点和空格分割
        # 实际生产中应使用更好的分词算法
        tokens = re.split(r'([，。！？、：；""' "（）《》【】\s])", text)
        return [t for t in tokens if t.strip()]

    def _translate_word(self, word, source_lang, target_lang):
        """
        翻译单个词/短语

        Args:
            word: 待翻译词
            source_lang: 源语言
            target_lang: 目标语言

        Returns:
            str: 翻译结果
        """
        if source_lang == target_lang:
            return word

        # 确定源和目标字段
        if source_lang == "zh":
            source_key = "zh"
            target_key = "hani"
        else:
            source_key = "hani"
            target_key = "zh"

        # 在所有词库中查找
        best_match = None
        best_score = 0

        for category, dict_data in self.dictionaries.items():
            for section_name, words in dict_data.items():
                for item in words:
                    if source_key not in item or target_key not in item:
                        continue

                    # 精确匹配
                    if item[source_key] == word:
                        return item[target_key]

                    # 模糊匹配
                    score = SequenceMatcher(None, item[source_key], word).ratio()
                    if score > best_score and score > 0.6:
                        best_score = score
                        best_match = item[target_key]

        if best_match:
            return best_match

        # 如果没有找到翻译，返回原文
        return word

    def translate_sentence(self, sentence, source_lang="zh", target_lang="hani"):
        """
        翻译句子（支持更复杂的句子结构）

        Args:
            sentence: 待翻译句子
            source_lang: 源语言
            target_lang: 目标语言

        Returns:
            str: 翻译结果
        """
        result = self.translate(sentence, source_lang, target_lang)
        return result["text"]

    def get_offline_words(self, category=None):
        """
        获取离线词汇

        Args:
            category: 词汇分类，默认为全部

        Returns:
            list: 词汇列表
        """
        if category:
            return self.dictionaries.get(category, {})

        return self.dictionaries

    def add_word(self, category, zh, hhani, pronunciation="", note=""):
        """
        添加新词汇

        Args:
            category: 分类
            zh: 汉语
            hhani: 哈尼语
            pronunciation: 发音标注
            note: 备注
        """
        if category not in self.dictionaries:
            self.dictionaries[category] = {"custom": []}

        if "custom" not in self.dictionaries[category]:
            self.dictionaries[category]["custom"] = []

        # 检查是否已存在
        for item in self.dictionaries[category]["custom"]:
            if item.get("zh") == zh:
                return False

        # 添加新词
        new_word = {
            "zh": zh,
            "hani": hhani,
        }
        if pronunciation:
            new_word["pronunciation"] = pronunciation
        if note:
            new_word["note"] = note

        self.dictionaries[category]["custom"].append(new_word)

        # 保存到文件
        self._save_dictionary(category)

        return True

    def _save_dictionary(self, category):
        """保存词库到文件"""
        base_path = os.path.join(os.path.dirname(__file__), "resources", "dictionaries")
        filepath = os.path.join(base_path, f"{category}.json")

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(
                self.dictionaries.get(category, {}), f, ensure_ascii=False, indent=2
            )

    def search_word(self, keyword, lang="zh"):
        """
        搜索词汇

        Args:
            keyword: 关键词
            lang: 搜索语言

        Returns:
            list: 匹配结果
        """
        results = []

        key = "zh" if lang == "zh" else "hani"

        for category, dict_data in self.dictionaries.items():
            for section_name, words in dict_data.items():
                for item in words:
                    if key in item and keyword.lower() in item[key].lower():
                        result = dict(item)
                        result["category"] = category
                        result["section"] = section_name
                        results.append(result)

        return results


# 测试代码
if __name__ == "__main__":
    engine = TranslationEngine()

    # 测试翻译
    tests = [
        ("你好", "zh", "hani"),
        ("谢谢", "zh", "hani"),
        ("再见", "zh", "hani"),
        ("nisoq", "hani", "zh"),
        ("aqda", "hani", "zh"),
    ]

    for text, src, tgt in tests:
        result = engine.translate(text, src, tgt)
        print(f"{src} -> {tgt}: {text} = {result['text']}")
