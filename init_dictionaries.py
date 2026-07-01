#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
词库初始化脚本
用于生成完整的JSON词库文件
"""

import json
import os


def create_lvyou_dictionary():
    """创建旅游词汇库"""
    return {
        "scenic_spots": [
            {
                "id": "ly001",
                "zh": "绿春县城",
                "hani": "lav cheeq",
                "pronunciation": "腊夫切",
                "category": "scenic",
                "intro": "绿春县城是哈尼族聚居的县城，仅有一条主街道",
            },
            {
                "id": "ly002",
                "zh": "黄连山",
                "hani": "hhaq ggu",
                "pronunciation": "哈谷",
                "category": "scenic",
                "intro": "绿春县境内的高山原始森林",
            },
            {
                "id": "ly003",
                "zh": "勐阿水库",
                "hani": "moq a",
                "pronunciation": "莫阿",
                "category": "scenic",
                "intro": "绿春县境内的人工湖泊",
            },
            {
                "id": "ly004",
                "zh": "诺玛阿美民族文化生态城",
                "hani": "noq ma a meiq",
                "pronunciation": "诺玛阿美",
                "category": "scenic",
                "intro": "重要的哈尼族文化展示场所",
            },
            {
                "id": "ly005",
                "zh": "勐角大峡谷",
                "hani": "moq jioq",
                "pronunciation": "莫角",
                "category": "scenic",
                "intro": "绿春著名峡谷景观",
            },
            {
                "id": "ly006",
                "zh": "绿春古城",
                "hani": "lav cheeq maq",
                "pronunciation": "腊夫切马",
                "category": "scenic",
                "intro": "哈尼族历史文化古城",
            },
        ],
        "transport": [
            {
                "id": "ly101",
                "zh": "汽车站",
                "hani": "xeiqnil jaiq",
                "pronunciation": "写你及",
                "category": "transport",
                "intro": "县城汽车站",
            },
            {
                "id": "ly102",
                "zh": "公交车",
                "hani": "koqge",
                "pronunciation": "科各",
                "category": "transport",
                "intro": "城市公共交通",
            },
            {
                "id": "ly103",
                "zh": "出租车",
                "hani": "ciqu",
                "pronunciation": "此去",
                "category": "transport",
                "intro": "出租车辆",
            },
            {
                "id": "ly104",
                "zh": "机场",
                "hani": "jul",
                "pronunciation": "局",
                "category": "transport",
                "intro": "周边机场",
            },
            {
                "id": "ly105",
                "zh": "火车站",
                "hani": "huq ceiq jaiq",
                "pronunciation": "胡层及",
                "category": "transport",
                "intro": "火车站",
            },
        ],
        "accommodation": [
            {
                "id": "ly201",
                "zh": "酒店",
                "hani": "jiuq deq",
                "pronunciation": "九的",
                "category": "hotel",
                "intro": "住宿酒店",
            },
            {
                "id": "ly202",
                "zh": "宾馆",
                "hani": "beq gal",
                "pronunciation": "别嘎",
                "category": "hotel",
                "intro": "住宿宾馆",
            },
            {
                "id": "ly203",
                "zh": "客栈",
                "hani": "keq zaq",
                "pronunciation": "科扎",
                "category": "hotel",
                "intro": "民宿客栈",
            },
            {
                "id": "ly204",
                "zh": "民宿",
                "hani": "miq zaq",
                "pronunciation": "米扎",
                "category": "hotel",
                "intro": "当地民宿",
            },
        ],
        "services": [
            {
                "id": "ly301",
                "zh": "门票",
                "hani": "meiq piu",
                "pronunciation": "美批",
                "category": "ticket",
                "intro": "景区门票",
            },
            {
                "id": "ly302",
                "zh": "导游",
                "hani": "dao y",
                "pronunciation": "倒一",
                "category": "service",
                "intro": "导游服务",
            },
            {
                "id": "ly303",
                "zh": "讲解员",
                "hani": "gaq saq",
                "pronunciation": "嘎撒",
                "category": "service",
                "intro": "景区讲解",
            },
        ],
    }


def create_festival_dictionary():
    """创建节日词汇库"""
    return {
        "festivals": [
            {
                "id": "fj001",
                "zh": "十月年",
                "hani": "cilceiq",
                "pronunciation": "次层",
                "category": "festival",
                "intro": "哈尼族最隆重的传统节日，相当于汉族的春节",
            },
            {
                "id": "fj002",
                "zh": "长街宴",
                "hani": "aol ngeq",
                "pronunciation": "奥恩",
                "category": "festival",
                "intro": "十月年期间的盛大宴席，被列入世界吉尼斯纪录",
            },
            {
                "id": "fj003",
                "zh": "祭龙节",
                "hani": "moq za",
                "pronunciation": "莫扎",
                "category": "festival",
                "intro": "哈尼族传统祭祀节日",
            },
            {
                "id": "fj004",
                "zh": "矻扎扎节",
                "hani": "kul za",
                "pronunciation": "苦扎",
                "category": "festival",
                "intro": "哈尼族传统节日，通常在农历五月",
            },
            {
                "id": "fj005",
                "zh": "六月年",
                "hani": "laol ceiq",
                "pronunciation": "劳层",
                "category": "festival",
                "intro": "哈尼族另一个重要节日",
            },
            {
                "id": "fj006",
                "zh": "嘎汤帕节",
                "hani": "gaq ta ma pa",
                "pronunciation": "嘎汤马爬",
                "category": "festival",
                "intro": "哈尼族传统节日",
            },
        ],
        "customs": [
            {
                "id": "fc101",
                "zh": "祭祖",
                "hani": "siq paol",
                "pronunciation": "四跑",
                "category": "custom",
                "intro": "祭祀祖先仪式",
            },
            {
                "id": "fc102",
                "zh": "祭祀",
                "hani": "za",
                "pronunciation": "扎",
                "category": "custom",
                "intro": "传统祭祀活动",
            },
            {
                "id": "fc103",
                "zh": "送年",
                "hani": "pei ceiq",
                "pronunciation": "配层",
                "category": "custom",
                "intro": "送别旧年仪式",
            },
        ],
        "activities": [
            {
                "id": "fa101",
                "zh": "长龙宴",
                "hani": "coq ngeq",
                "pronunciation": "从恩",
                "category": "activity",
                "intro": "长街宴的另一种说法",
            },
            {
                "id": "fa102",
                "zh": "篝火晚会",
                "hani": "hhaq neiq mo",
                "pronunciation": "哈呢莫",
                "category": "activity",
                "intro": "民族歌舞晚会",
            },
            {
                "id": "fa103",
                "zh": "民族歌舞",
                "hani": "hhaq niq",
                "pronunciation": "哈你",
                "category": "activity",
                "intro": "哈尼族传统歌舞",
            },
        ],
    }


def create_food_dictionary():
    """创建美食词汇库"""
    return {
        "dishes": [
            {
                "id": "fd001",
                "zh": "长街宴",
                "hani": "aol ngeq",
                "pronunciation": "奥恩",
                "category": "food",
                "intro": "绿春特色宴席，汇聚各种哈尼族特色菜",
            },
            {
                "id": "fd002",
                "zh": "哈尼腊肉",
                "hani": "a saq",
                "pronunciation": "阿撒",
                "category": "food",
                "intro": "哈尼族传统腌制食品",
            },
            {
                "id": "fd003",
                "zh": "竹筒饭",
                "hani": "coq pyu",
                "pronunciation": "从普",
                "category": "food",
                "intro": "用竹筒烹制的糯米饭",
            },
            {
                "id": "fd004",
                "zh": "哈尼糯米酒",
                "hani": "aq daq",
                "pronunciation": "阿大",
                "category": "food",
                "intro": "哈尼族传统米酒",
            },
            {
                "id": "fd005",
                "zh": "血肠",
                "hani": "shei cbaq",
                "pronunciation": "舍巴",
                "category": "food",
                "intro": "用猪血和糯米制成的特色食品",
            },
            {
                "id": "fd006",
                "zh": "染蛋",
                "hani": "ngee daq",
                "pronunciation": "呢大",
                "category": "food",
                "intro": "用植物染色剂染色的蛋",
            },
            {
                "id": "fd007",
                "zh": "黄米饭",
                "hani": "hhaq paq",
                "pronunciation": "哈爬",
                "category": "food",
                "intro": "用 黄米制成的米饭",
            },
            {
                "id": "fd008",
                "zh": "三色蛋",
                "hani": "so daq",
                "pronunciation": "索大",
                "category": "food",
                "intro": "三种颜色的煮蛋",
            },
            {
                "id": "fd009",
                "zh": "糯米魔芋",
                "hani": "laol moq",
                "pronunciation": "劳莫",
                "category": "food",
                "intro": "糯米与魔芋混合食品",
            },
            {
                "id": "fd010",
                "zh": "豆腐圆子",
                "hani": "toufu yeiq",
                "pronunciation": "头夫也",
                "category": "food",
                "intro": "油炸豆腐丸",
            },
            {
                "id": "fd011",
                "zh": "油炸竹虫",
                "hani": "coq neiq",
                "pronunciation": "从呢",
                "category": "food",
                "intro": "油炸竹林昆虫",
            },
        ],
        "ingredients": [
            {
                "id": "fi101",
                "zh": "糯米",
                "hani": "laol",
                "pronunciation": "劳",
                "category": "ingredient",
                "intro": "糯米饭原料",
            },
            {
                "id": "fi102",
                "zh": "香茅草",
                "hani": "cao ca",
                "pronunciation": "草草",
                "category": "ingredient",
                "intro": "香料植物",
            },
        ],
    }


def create_building_dictionary():
    """创建建筑词汇库"""
    return {
        "buildings": [
            {
                "id": "bd001",
                "zh": "土掌房",
                "hani": "zeil qei",
                "pronunciation": "则其",
                "category": "building",
                "intro": "哈尼族传统民居，土木结构",
            },
            {
                "id": "bd002",
                "zh": "蘑菇房",
                "hani": "aq puq",
                "pronunciation": "阿普",
                "category": "building",
                "intro": "哈尼族传统建筑，形似蘑菇",
            },
            {
                "id": "bd003",
                "zh": "寨门",
                "hani": "zaq me",
                "pronunciation": "扎么",
                "category": "building",
                "intro": "哈尼村寨入口处的建筑",
            },
            {
                "id": "bd004",
                "zh": "龙树",
                "hani": "moq shul",
                "pronunciation": "莫书",
                "category": "building",
                "intro": "哈尼族神圣的祭祀树木",
            },
            {
                "id": "bd005",
                "zh": "祭祀房",
                "hani": "siq za",
                "pronunciation": "四扎",
                "category": "building",
                "intro": "用于祭祀的房屋",
            },
            {
                "id": "bd006",
                "zh": "磨房",
                "hani": "moq za",
                "pronunciation": "莫扎",
                "category": "building",
                "intro": "研磨粮食的房间",
            },
        ],
        "parts": [
            {
                "id": "bp101",
                "zh": "火塘",
                "hani": "piu",
                "pronunciation": "批",
                "category": "part",
                "intro": "室内火塘",
            },
            {
                "id": "bp102",
                "zh": "粮仓",
                "hani": "qo",
                "pronunciation": "却",
                "category": "part",
                "intro": "存放粮食的仓库",
            },
        ],
    }


def create_clothing_dictionary():
    """创建服饰词汇库"""
    return {
        "clothing": [
            {
                "id": "cl001",
                "zh": "哈尼服",
                "hani": "aq gee",
                "pronunciation": "阿给",
                "category": "clothing",
                "intro": "哈尼族传统服装",
            },
            {
                "id": "cl002",
                "zh": "包头",
                "hani": "aq pei",
                "pronunciation": "阿配",
                "category": "clothing",
                "intro": "哈尼族男子头饰",
            },
            {
                "id": "cl003",
                "zh": "银饰",
                "hani": "nil nie",
                "pronunciation": "你捏",
                "category": "clothing",
                "intro": "哈尼族传统银质饰品",
            },
            {
                "id": "cl004",
                "zh": "刺绣",
                "hani": "aq be",
                "pronunciation": "阿别",
                "category": "clothing",
                "intro": "哈尼族传统刺绣工艺",
            },
            {
                "id": "cl005",
                "zh": "腰带",
                "hani": "deiq za",
                "pronunciation": "得扎",
                "category": "clothing",
                "intro": "民族腰带",
            },
            {
                "id": "cl006",
                "zh": "绑腿",
                "hani": "piul",
                "pronunciation": "批乌",
                "category": "clothing",
                "intro": "腿部装饰",
            },
        ],
        "colors": [
            {
                "id": "cc101",
                "zh": "黑色",
                "hani": "naq",
                "pronunciation": "那",
                "color": "#000000",
            },
            {
                "id": "cc102",
                "zh": "红色",
                "hani": "cil",
                "pronunciation": "此",
                "color": "#FF0000",
            },
            {
                "id": "cc103",
                "zh": "蓝色",
                "hani": "nil",
                "pronunciation": "你",
                "color": "#0000FF",
            },
        ],
    }


def create_etiquette_dictionary():
    """创建礼仪词汇库"""
    return {
        "etiquette": [
            {
                "id": "et001",
                "zh": "敬酒",
                "hani": "mil za",
                "pronunciation": "米扎",
                "category": "etiquette",
                "intro": "哈尼族热情好客的敬酒礼仪",
            },
            {
                "id": "et002",
                "zh": "让座",
                "hani": "deiq yul",
                "pronunciation": "得约",
                "category": "etiquette",
                "intro": "尊老爱幼的传统美德",
            },
            {
                "id": "et003",
                "zh": "磕头",
                "hani": "khao tiao",
                "pronunciation": "考跳",
                "category": "etiquette",
                "intro": "哈尼族传统礼仪",
            },
            {
                "id": "et004",
                "zh": "作客",
                "hani": "zaq pa",
                "pronunciation": "扎爬",
                "category": "etiquette",
                "intro": "拜访客人",
            },
            {
                "id": "et005",
                "zh": "待客",
                "hani": "yol za",
                "pronunciation": "约扎",
                "category": "etiquette",
                "intro": "接待客人",
            },
        ],
        "words": [
            {
                "id": "ew101",
                "zh": "欢迎",
                "hani": "laol da",
                "pronunciation": "劳大",
                "category": "word",
                "intro": "欢迎光临",
            },
            {
                "id": "ew102",
                "zh": "请进",
                "hani": "laol yol",
                "pronunciation": "劳约",
                "category": "word",
                "intro": "邀请进入",
            },
            {
                "id": "ew103",
                "zh": "请坐",
                "hani": "deiq yul yol",
                "pronunciation": "得约约",
                "category": "word",
                "intro": "邀请入座",
            },
        ],
    }


def create_direction_dictionary():
    """创建问路词汇库"""
    return {
        "directions": [
            {
                "id": "dr001",
                "zh": "左转",
                "hani": "peiq cei",
                "pronunciation": "配脆",
                "category": "direction",
            },
            {
                "id": "dr002",
                "zh": "右转",
                "hani": "naol cei",
                "pronunciation": "闹脆",
                "category": "direction",
            },
            {
                "id": "dr003",
                "zh": "直走",
                "hani": "dil diq",
                "pronunciation": "地地",
                "category": "direction",
            },
            {
                "id": "dr004",
                "zh": "前面",
                "hani": "maq zai",
                "pronunciation": "马在",
                "category": "direction",
            },
            {
                "id": "dr005",
                "zh": "后面",
                "hani": "huq zai",
                "pronunciation": "胡在",
                "category": "direction",
            },
            {
                "id": "dr006",
                "zh": "旁边",
                "hani": "naq zai",
                "pronunciation": "那在",
                "category": "direction",
            },
            {
                "id": "dr007",
                "zh": "多远",
                "hani": "al bol",
                "pronunciation": "阿波",
                "category": "distance",
            },
            {
                "id": "dr008",
                "zh": "在哪里",
                "hani": "aol daq",
                "pronunciation": "奥大",
                "category": "location",
            },
            {
                "id": "dr009",
                "zh": "这边",
                "hani": "ciq zai",
                "pronunciation": "此在",
                "category": "direction",
            },
            {
                "id": "dr010",
                "zh": "那边",
                "hani": "hao zai",
                "pronunciation": "好在",
                "category": "direction",
            },
            {
                "id": "dr011",
                "zh": "东",
                "hani": "dong",
                "pronunciation": "东",
                "category": "direction",
            },
            {
                "id": "dr012",
                "zh": "西",
                "hani": "xi",
                "pronunciation": "西",
                "category": "direction",
            },
            {
                "id": "dr013",
                "zh": "南",
                "hani": "nan",
                "pronunciation": "南",
                "category": "direction",
            },
            {
                "id": "dr014",
                "zh": "北",
                "hani": "bei",
                "pronunciation": "北",
                "category": "direction",
            },
        ],
        "distances": [
            {
                "id": "ds101",
                "zh": "很近",
                "hani": "al qei",
                "pronunciation": "阿气",
                "distance": "near",
            },
            {
                "id": "ds102",
                "zh": "很远",
                "hani": "al bol",
                "pronunciation": "阿波",
                "distance": "far",
            },
            {
                "id": "ds103",
                "zh": "十分钟",
                "hani": "ceiq gal",
                "pronunciation": "层嘎",
                "time": "10min",
            },
            {
                "id": "ds104",
                "zh": "三十分钟",
                "hani": "so gal",
                "pronunciation": "索嘎",
                "time": "30min",
            },
        ],
        "landmarks": [
            {
                "id": "lm101",
                "zh": "路口",
                "hani": "diul jaiq",
                "pronunciation": "丢及",
                "intro": "道路交叉口",
            },
            {
                "id": "lm102",
                "zh": "桥",
                "hani": "coq",
                "pronunciation": "从",
                "intro": "过河桥梁",
            },
            {
                "id": "lm103",
                "zh": "市场",
                "hani": "saol",
                "pronunciation": "扫",
                "intro": "交易市场",
            },
        ],
    }


def create_daily_dictionary():
    """创建日常用语词汇库"""
    return {
        "greetings": [
            {
                "id": "gr001",
                "zh": "你好",
                "hani": "nisoq",
                "pronunciation": "尼梭",
                "category": "greeting",
            },
            {
                "id": "gr002",
                "zh": "再见",
                "hani": "haqma",
                "pronunciation": "哈玛",
                "category": "greeting",
            },
            {
                "id": "gr003",
                "zh": "谢谢",
                "hani": "aqda",
                "pronunciation": "阿大",
                "category": "greeting",
            },
            {
                "id": "gr004",
                "zh": "对不起",
                "hani": "ulpuq",
                "pronunciation": "乌尔普",
                "category": "greeting",
            },
            {
                "id": "gr005",
                "zh": "没关系",
                "hani": "ulpuq qif",
                "pronunciation": "乌尔普期",
                "category": "greeting",
            },
            {
                "id": "gr006",
                "zh": "是",
                "hani": "ee",
                "pronunciation": "额",
                "category": "greeting",
            },
            {
                "id": "gr007",
                "zh": "不是",
                "hani": "qif ee",
                "pronunciation": "期额",
                "category": "greeting",
            },
            {
                "id": "gr008",
                "zh": "好的",
                "hani": "hha",
                "pronunciation": "哈",
                "category": "greeting",
            },
        ],
        "common": [
            {
                "id": "cm001",
                "zh": "我",
                "hani": "nga",
                "pronunciation": "昂",
                "category": "pronoun",
            },
            {
                "id": "cm002",
                "zh": "你",
                "hani": "ni",
                "pronunciation": "你",
                "category": "pronoun",
            },
            {
                "id": "cm003",
                "zh": "他/她",
                "hani": "ma",
                "pronunciation": "马",
                "category": "pronoun",
            },
            {
                "id": "cm004",
                "zh": "我们",
                "hani": "nga teiq",
                "pronunciation": "昂台",
                "category": "pronoun",
            },
            {
                "id": "cm005",
                "zh": "你们",
                "hani": "ni teiq",
                "pronunciation": "你台",
                "category": "pronoun",
            },
            {
                "id": "cm006",
                "zh": "他们",
                "hani": "ma teiq",
                "pronunciation": "马台",
                "category": "pronoun",
            },
        ],
        "family": [
            {
                "id": "fm001",
                "zh": "爸爸",
                "hani": "aqpa",
                "pronunciation": "阿帕",
                "category": "family",
            },
            {
                "id": "fm002",
                "zh": "妈妈",
                "hani": "aqma",
                "pronunciation": "阿马",
                "category": "family",
            },
            {
                "id": "fm003",
                "zh": "爷爷",
                "hani": "appa",
                "pronunciation": "阿爬",
                "category": "family",
            },
            {
                "id": "fm004",
                "zh": "奶奶",
                "hani": "appa ma",
                "pronunciation": "阿爬马",
                "category": "family",
            },
            {
                "id": "fm005",
                "zh": "哥哥",
                "hani": "aqpa",
                "pronunciation": "阿帕",
                "category": "family",
            },
            {
                "id": "fm006",
                "zh": "姐姐",
                "hani": "aqpie",
                "pronunciation": "阿别",
                "category": "family",
            },
        ],
    }


def save_dictionaries(base_path):
    """保存所有词库到文件"""
    os.makedirs(base_path, exist_ok=True)

    dicts = {
        "daily.json": create_daily_dictionary,
        "lvyou.json": create_lvyou_dictionary,
        "festival.json": create_festival_dictionary,
        "food.json": create_food_dictionary,
        "building.json": create_building_dictionary,
        "clothing.json": create_clothing_dictionary,
        "etiquette.json": create_etiquette_dictionary,
        "direction.json": create_direction_dictionary,
    }

    for filename, creator in dicts.items():
        data = creator()
        filepath = os.path.join(base_path, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"已创建: {filepath}")

    print(f"\n共创建 {len(dicts)} 个词库文件")


if __name__ == "__main__":
    base_path = os.path.join(os.path.dirname(__file__), "resources", "dictionaries")
    save_dictionaries(base_path)
    print("词库初始化完成！")
