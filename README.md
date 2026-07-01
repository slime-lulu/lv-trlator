# 绿县文旅哈尼语翻译通

一款服务绿春县游客、文旅工作人员和本地哈尼群众的哈尼语-汉语双向翻译移动端应用。

## 项目概述

| 项目信息 | 内容 |
|----------|------|
| 项目名称 | 绿县文旅哈尼语翻译通 |
| 英文名称 | LvCounty Hani Translator |
| 版本 | 1.0.0 |
| 开发框架 | Python Kivy |
| 目标平台 | Android / iOS |

## 功能特性

### 核心功能
- ✅ **双向翻译**：汉语↔哈尼语双向互译
- ✅ **双输入模式**：文字输入 + 语音输入
- ✅ **双输出功能**：文本展示 + 语音朗读
- ✅ **离线翻译**：内置轻量化词库，无网也能用
- ✅ **文旅词汇库**：景区、节日、美食、建筑、服饰、礼仪、问路专用词条
- ✅ **翻译历史**：自动存储，支持检索、朗读、复制
- ✅ **快捷工具**：一键复制、文字分享、清空输入

### 界面设计
- 🎨 **主色调**：墨绿(#1B5E20) + 土红(#5D4037) + 棕褐(#8D6E63)
- 📱 **民族简约风**：大字号适配中老年用户
- 🌐 **双语显示**：所有界面元素哈尼语+汉语双语

### 附加功能
- 📚 **文化科普卡片**：十月年、长街宴、棕扇舞等简介
- ⭐ **词条收藏**：常用词条一键收藏
- 📋 **导入导出**：词库可编辑，支持扩展

## 项目结构

```
lv_trlator/
├── main.py                    # 主程序入口
├── translation_engine.py      # 翻译引擎
├── dictionary_manager.py      # 词库管理
├── audio_player.py            # 语音播放
├── storage_manager.py         # 数据存储
├── bili_text.py               # 双语文本
├── ui_layout.py               # UI布局定义
├── requirements.txt           # Python依赖
├── buildozer.spec            # Android打包配置
├── project_config.ini        # 项目配置
├── README.md                  # 说明文档
├── docs/
│   └── bilingual_text_table.md # 双语文案对照表
├── resources/
│   ├── dictionaries/         # 词库文件(JSON)
│   │   ├── daily.json        # 日常用语
│   │   ├── lvyou.json        # 旅游词汇
│   │   ├── festival.json     # 节日词汇
│   │   ├── food.json         # 美食词汇
│   │   ├── building.json     # 建筑词汇
│   │   ├── clothing.json     # 服饰词汇
│   │   ├── etiquette.json    # 礼仪词汇
│   │   └── direction.json    # 问路词汇
│   ├── audio/                # 音频资源
│   └── images/               # 图片资源
└── data/                     # 应用数据目录
    ├── history.json          # 翻译历史
    ├── favorites.json        # 收藏词条
    └── settings.json         # 应用设置
```

## 环境配置

### 开发环境要求
- Python 3.8+
- Kivy 2.3.0+
- 操作系统：Windows / macOS / Linux

### 安装依赖

```bash
# 克隆项目
git clone <repository_url>
cd lv_trlator

# 安装Python依赖
pip install -r requirements.txt
```

## 运行应用

### 开发模式（桌面测试）

```bash
python main.py
```

### Android打包

#### 方式一：使用Buildozer（推荐）

```bash
# 安装Buildozer
pip install buildozer

# 初始化Buildozer（首次运行）
buildozer init

# 打包为Debug APK
buildozer android debug

# 打包为Release APK
buildozer android release
```

#### 方式二：使用本地SDK

```bash
# 设置Android SDK环境变量
export ANDROID_SDK_ROOT=/path/to/android/sdk

# 打包
python -m buildozer android debug
```

### iOS打包（仅macOS）

```bash
# 安装Buildozer
pip install buildozer

# 打包
buildozer ios
```

## 词库说明

### 词库格式

词库采用JSON格式存储，每条词条包含以下字段：

```json
{
  "id": "唯一标识符",
  "zh": "中文词条",
  "hani": "哈尼语词条",
  "pronunciation": "发音标注(可选)",
  "category": "分类标识(可选)",
  "intro": "词条介绍(可选)"
}
```

### 词库分类

| 文件名 | 说明 | 示例词条 |
|--------|------|----------|
| daily.json | 日常用语 | 你好、再见、谢谢 |
| lvyou.json | 旅游词汇 | 景点、住宿、交通 |
| festival.json | 节日词汇 | 十月年、长街宴 |
| food.json | 美食词汇 | 竹筒饭、哈尼腊肉 |
| building.json | 建筑词汇 | 土掌房、蘑菇房 |
| clothing.json | 服饰词汇 | 哈尼服、银饰 |
| etiquette.json | 礼仪词汇 | 敬酒、让座 |
| direction.json | 问路词汇 | 左转、直走、前方 |

### 自定义词条

用户可以通过编辑JSON文件添加自定义词条：

1. 打开对应的JSON文件
2. 添加新词条（注意保持JSON格式正确）
3. 保存文件后重启应用

## 语音配置

### 汉语语音
- 使用系统TTS或pyttsx3离线引擎
- 声音：标准普通话女声
- 备选：网络TTS服务

### 哈尼语语音
- 优先：本地母语者录制音频
- 备选：系统TTS
- 说明：建议添加本地母语者录制的发音音频

## 页面结构

```
启动页 (SplashScreen)
    │
    ▼
主翻译页 (MainTranslatorScreen) ─── 词汇库页 (DictionaryScreen)
    │                                      │
    ├── 历史记录页 (HistoryScreen)         │
    │                                      │
    └── 关于软件页 (AboutScreen) ──────────┘
```

## 常见问题

### Q: 离线模式下翻译失败？
A: 请确保词库文件完整，检查JSON文件格式是否正确。

### Q: 语音播放失败？
A: 
- 检查音频服务是否正常
- 离线模式下部分语音功能可能不可用
- 建议安装playsound库

### Q: 如何添加新的哈尼语词条？
A: 
- 方法1：编辑`resources/dictionaries/`下的JSON文件
- 方法2：在应用内的词汇库页面添加

### Q: 打包APK失败？
A:
- 确保已安装Android SDK
- 检查buildozer.spec配置
- 查看错误日志进行排查

## 开发者信息

- **项目维护**：绿县文旅项目组
- **联系方式**：support@lvcounty.com
- **许可证**：专有软件

## 更新日志

### v1.0.0 (2024-06)
- 初始版本发布
- 实现基础翻译功能
- 离线词库支持
- 双语文案显示

---

*感谢使用绿县文旅翻译通！*
*服务绿春文旅，传承哈尼文化！*