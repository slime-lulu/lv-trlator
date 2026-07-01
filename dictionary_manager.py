# -*- coding: utf-8 -*-
"""
词库管理模块
管理文旅专属词汇库、收藏功能、检索功能
"""

import os
import json


class DictionaryManager:
    """词库管理器"""

    def __init__(self):
        """初始化词库管理器"""
        self.dictionaries = {}
        self.favorites = set()
        self.base_path = os.path.join(
            os.path.dirname(__file__), "resources", "dictionaries"
        )

        # 确保目录存在
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

        # 加载所有词库
        self._load_all_dictionaries()

        # 加载收藏
        self._load_favorites()

    def _load_all_dictionaries(self):
        """加载所有词库"""
        dict_files = [
            "daily.json",
            "lvyou.json",
            "festival.json",
            "food.json",
            "building.json",
            "clothing.json",
            "etiquette.json",
            "direction.json",
        ]

        for filename in dict_files:
            filepath = os.path.join(self.base_path, filename)
            if os.path.exists(filepath):
                with open(filepath, "r", encoding="utf-8") as f:
                    category = filename.replace(".json", "")
                    self.dictionaries[category] = json.load(f)
            else:
                # 创建空词库
                self.dictionaries[filename.replace(".json", "")] = {}
                self._create_default_dictionary(filename.replace(".json", ""))

    def _create_default_dictionary(self, category):
        """创建默认词库"""
        default_data = {}

        if category == "lvyou":
            default_data = {
                "scenic_spots": [
                    {
                        "id": "ly001",
                        "zh": "绿春县城",
                        "hani": "lav cheeq",
                        "category": "scenic",
                        "intro": "绿春县城是哈尼族聚居的县城，仅有一条主街道",
                    },
                    {
                        "id": "ly002",
                        "zh": "黄连山",
                        "hani": "hhaq ggu",
                        "category": "scenic",
                        "intro": "绿春县境内的高山原始森林",
                    },
                    {
                        "id": "ly003",
                        "zh": "勐阿水库",
                        "hani": "moq a",
                        "category": "scenic",
                        "intro": "绿春县境内的人工湖泊",
                    },
                ],
                "transport": [
                    {
                        "id": "ly101",
                        "zh": "汽车站",
                        "hani": "xeiqnil jaiq",
                        "category": "transport",
                    },
                    {
                        "id": "ly102",
                        "zh": "公交车",
                        "hani": "koqge",
                        "category": "transport",
                    },
                    {
                        "id": "ly103",
                        "zh": "出租车",
                        "hani": "ciqu",
                        "category": "transport",
                    },
                ],
            }
        elif category == "festival":
            default_data = {
                "festivals": [
                    {
                        "id": "fj001",
                        "zh": "十月年",
                        "hani": "cilceiq",
                        "category": "festival",
                        "intro": "哈尼族最隆重的传统节日，相当于汉族的春节",
                    },
                    {
                        "id": "fj002",
                        "zh": "长街宴",
                        "hani": "aol ngeq",
                        "category": "festival",
                        "intro": "十月年期间的盛大宴席，被列入世界吉尼斯纪录",
                    },
                    {
                        "id": "fj003",
                        "zh": "祭龙节",
                        "hani": "moq za",
                        "category": "festival",
                        "intro": "哈尼族传统祭祀节日",
                    },
                    {
                        "id": "fj004",
                        "zh": "矻扎扎节",
                        "hani": "kul za",
                        "category": "festival",
                        "intro": "哈尼族传统节日",
                    },
                ]
            }
        elif category == "food":
            default_data = {
                "dishes": [
                    {
                        "id": "fd001",
                        "zh": "长街宴",
                        "hani": "aol ngeq",
                        "category": "food",
                        "intro": "绿春特色宴席，汇聚各种哈尼族特色菜",
                    },
                    {
                        "id": "fd002",
                        "zh": "哈尼腊肉",
                        "hani": "a saq",
                        "category": "food",
                        "intro": "哈尼族传统腌制食品",
                    },
                    {
                        "id": "fd003",
                        "zh": "竹筒饭",
                        "hani": "coq pyu",
                        "category": "food",
                        "intro": "用竹筒烹制的糯米饭",
                    },
                    {
                        "id": "fd004",
                        "zh": "哈尼糯米酒",
                        "hani": "aq daq",
                        "category": "food",
                        "intro": "哈尼族传统米酒",
                    },
                    {
                        "id": "fd005",
                        "zh": "血肠",
                        "hani": "shei cbaq",
                        "category": "food",
                        "intro": "用猪血和糯米制成的特色食品",
                    },
                    {
                        "id": "fd006",
                        "zh": "染蛋",
                        "hani": "ngee daq",
                        "category": "food",
                        "intro": "用植物染色剂染色的蛋",
                    },
                ]
            }
        elif category == "building":
            default_data = {
                "buildings": [
                    {
                        "id": "bd001",
                        "zh": "土掌房",
                        "hani": "zeil qei",
                        "category": "building",
                        "intro": "哈尼族传统民居，土木结构",
                    },
                    {
                        "id": "bd002",
                        "zh": "蘑菇房",
                        "hani": "aq puq",
                        "category": "building",
                        "intro": "哈尼族传统建筑，形似蘑菇",
                    },
                    {
                        "id": "bd003",
                        "zh": "寨门",
                        "hani": "zaq me",
                        "category": "building",
                        "intro": "哈尼村寨入口处的建筑",
                    },
                    {
                        "id": "bd004",
                        "zh": "龙树",
                        "hani": "moq shul",
                        "category": "building",
                        "intro": "哈尼族神圣的祭祀树木",
                    },
                ]
            }
        elif category == "clothing":
            default_data = {
                "clothing": [
                    {
                        "id": "cl001",
                        "zh": "哈尼服",
                        "hani": "aq gee",
                        "category": "clothing",
                        "intro": "哈尼族传统服装",
                    },
                    {
                        "id": "cl002",
                        "zh": "包头",
                        "hani": "aq pei",
                        "category": "clothing",
                        "intro": "哈尼族男子头饰",
                    },
                    {
                        "id": "cl003",
                        "zh": "银饰",
                        "hani": "nil nie",
                        "category": "clothing",
                        "intro": "哈尼族传统银质饰品",
                    },
                    {
                        "id": "cl004",
                        "zh": "刺绣",
                        "hani": "aq be",
                        "category": "clothing",
                        "intro": "哈尼族传统刺绣工艺",
                    },
                ]
            }
        elif category == "etiquette":
            default_data = {
                "etiquette": [
                    {
                        "id": "et001",
                        "zh": "敬酒",
                        "hani": "mil za",
                        "category": "etiquette",
                        "intro": "哈尼族热情好客的敬酒礼仪",
                    },
                    {
                        "id": "et002",
                        "zh": "让座",
                        "hani": "deiq yul",
                        "category": "etiquette",
                        "intro": "尊老爱幼的传统美德",
                    },
                    {
                        "id": "et003",
                        "zh": "磕头",
                        "hani": "khao tiao",
                        "category": "etiquette",
                        "intro": "哈尼族传统礼仪",
                    },
                ]
            }
        elif category == "direction":
            default_data = {
                "directions": [
                    {
                        "id": "dr001",
                        "zh": "左转",
                        "hani": "peiq cei",
                        "category": "direction",
                    },
                    {
                        "id": "dr002",
                        "zh": "右转",
                        "hani": "naol cei",
                        "category": "direction",
                    },
                    {
                        "id": "dr003",
                        "zh": "直走",
                        "hani": "dil diq",
                        "category": "direction",
                    },
                    {
                        "id": "dr004",
                        "zh": "前面",
                        "hani": "maq zai",
                        "category": "direction",
                    },
                    {
                        "id": "dr005",
                        "zh": "后面",
                        "hani": "huq zai",
                        "category": "direction",
                    },
                    {
                        "id": "dr006",
                        "zh": "旁边",
                        "hani": "naq zai",
                        "category": "direction",
                    },
                    {
                        "id": "dr007",
                        "zh": "多远",
                        "hani": "al bol",
                        "category": "direction",
                    },
                    {
                        "id": "dr008",
                        "zh": "在哪里",
                        "hani": "aol daq",
                        "category": "direction",
                    },
                ]
            }

        # 保存默认词库
        filepath = os.path.join(self.base_path, f"{category}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(default_data, f, ensure_ascii=False, indent=2)

        self.dictionaries[category] = default_data

    def _load_favorites(self):
        """加载收藏"""
        fav_file = os.path.join(self.base_path, "favorites.json")
        if os.path.exists(fav_file):
            with open(fav_file, "r", encoding="utf-8") as f:
                self.favorites = set(json.load(f))

    def _save_favorites(self):
        """保存收藏"""
        fav_file = os.path.join(self.base_path, "favorites.json")
        with open(fav_file, "w", encoding="utf-8") as f:
            json.dump(list(self.favorites), f, ensure_ascii=False)

    def search_words(self, category, keyword=""):
        """
        搜索词条

        Args:
            category: 词库分类
            keyword: 搜索关键词

        Returns:
            list: 匹配词条列表
        """
        results = []

        if category not in self.dictionaries:
            return results

        dict_data = self.dictionaries[category]

        for section_name, words in dict_data.items():
            for item in words:
                if keyword:
                    # 关键词搜索
                    zh = item.get("zh", "")
                    hhani = item.get("hani", "")
                    if (
                        keyword.lower() not in zh.lower()
                        and keyword.lower() not in hhani.lower()
                    ):
                        continue

                # 添加收藏状态
                item_copy = dict(item)
                item_copy["is_favorite"] = item.get("id", "") in self.favorites
                results.append(item_copy)

        return results

    def get_words_by_category(self, category):
        """
        获取指定分类的所有词条

        Args:
            category: 词库分类

        Returns:
            list: 词条列表
        """
        return self.search_words(category)

    def toggle_favorite(self, word_id):
        """
        切换收藏状态

        Args:
            word_id: 词条ID
        """
        if word_id in self.favorites:
            self.favorites.discard(word_id)
        else:
            self.favorites.add(word_id)

        self._save_favorites()

    def get_favorites(self):
        """
        获取所有收藏词条

        Returns:
            list: 收藏词条列表
        """
        favorites_list = []

        for category, dict_data in self.dictionaries.items():
            for section_name, words in dict_data.items():
                for item in words:
                    if item.get("id", "") in self.favorites:
                        item_copy = dict(item)
                        item_copy["category"] = category
                        item_copy["is_favorite"] = True
                        favorites_list.append(item_copy)

        return favorites_list

    def get_total_count(self):
        """
        获取词条总数

        Returns:
            int: 词条数量
        """
        total = 0
        for category, dict_data in self.dictionaries.items():
            for section_name, words in dict_data.items():
                total += len(words)
        return total

    def get_categories(self):
        """
        获取所有分类

        Returns:
            dict: 分类信息 {分类名: 描述}
        """
        return {
            "daily": {"name": "日常用语", "name_hani": "ssol hhaq", "icon": "daily"},
            "lvyou": {"name": "旅游词汇", "name_hani": "hhaq naol", "icon": "lvyou"},
            "festival": {
                "name": "节日词汇",
                "name_hani": "cil ceiq",
                "icon": "festival",
            },
            "food": {"name": "美食词汇", "name_hani": "aol", "icon": "food"},
            "building": {"name": "建筑词汇", "name_hani": "zeil", "icon": "building"},
            "clothing": {"name": "服饰词汇", "name_hani": "aq gee", "icon": "clothing"},
            "etiquette": {
                "name": "礼仪词汇",
                "name_hani": "hhaq miq",
                "icon": "etiquette",
            },
            "direction": {"name": "问路词汇", "name_hani": "diiq", "icon": "direction"},
        }

    def add_custom_word(self, category, word_data):
        """
        添加自定义词汇

        Args:
            category: 分类
            word_data: 词汇数据

        Returns:
            bool: 是否添加成功
        """
        if category not in self.dictionaries:
            self.dictionaries[category] = {"custom": []}

        if "custom" not in self.dictionaries[category]:
            self.dictionaries[category]["custom"] = []

        # 生成ID
        word_id = f"cu{len(self.dictionaries[category]['custom']):04d}"
        word_data["id"] = word_id
        word_data["category"] = "custom"

        self.dictionaries[category]["custom"].append(word_data)

        # 保存到文件
        self._save_dictionary(category)

        return True

    def _save_dictionary(self, category):
        """保存词库到文件"""
        filepath = os.path.join(self.base_path, f"{category}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(
                self.dictionaries.get(category, {}), f, ensure_ascii=False, indent=2
            )
