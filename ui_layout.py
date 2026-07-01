# -*- coding: utf-8 -*-
"""
UI布局文件（Kivy语言定义）
定义所有页面的布局结构
"""

# 主翻译页面布局
MAIN_TRANSLATOR_KV = """
<MainTranslatorScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 15
        spacing: 10
        
        # 顶部标题栏
        BoxLayout:
            size_hint_y: None
            height: '60dp'
            spacing: 10
            
            Label:
                text: app.title
                font_size: '22sp'
                bold: True
                color: 0.106, 0.369, 0.125, 1
                size_hint_x: 0.7
            
            Button:
                text: '☰'
                font_size: '24sp'
                size_hint_x: 0.15
                on_press: root.manager.current = 'dictionary'
            
            Button:
                text: '☎'
                font_size: '24sp'
                size_hint_x: 0.15
                on_press: root.manager.current = 'history'
        
        # 语言切换栏
        BoxLayout:
            size_hint_y: None
            height: '50dp'
            spacing: 10
            
            ToggleButton:
                id: btn_zh_to_hani
                text: '汉→哈' if root.translation_direction == 0 else '哈→汉'
                state: 'down' if root.translation_direction == 0 else 'normal'
                font_size: '16sp'
                on_press: root.translation_direction = 0; root.update_bilingual_texts()
            
            Button:
                text: '⇄'
                font_size: '20sp'
                size_hint_x: 0.2
                on_press: root.swap_direction()
            
            ToggleButton:
                id: btn_hani_to_zh
                text: '哈→汉' if root.translation_direction == 1 else '汉→哈'
                state: 'down' if root.translation_direction == 1 else 'normal'
                font_size: '16sp'
                on_press: root.translation_direction = 1; root.update_bilingual_texts()
        
        # 离线模式开关
        BoxLayout:
            size_hint_y: None
            height: '40dp'
            spacing: 10
            padding: [10, 0]
            
            Label:
                text: '离线模式'
                font_size: '14sp'
                size_hint_x: 0.6
            
            Switch:
                id: offline_switch
                active: root.offline_mode
                on_active: root.offline_mode = args[1]
        
        # 输入区域
        BoxLayout:
            size_hint_y: 0.35
            orientation: 'vertical'
            spacing: 5
            
            Label:
                text: '输入文字'
                font_size: '14sp'
                color: 0.5, 0.5, 0.5, 1
                size_hint_y: None
                height: '25dp'
            
            TextInput:
                id: input_field
                text: root.input_text
                hint_text: '请输入要翻译的中文...'
                font_size: '18sp'
                multiline: True
                padding: 10
                background_color: 1, 1, 1, 1
            
            # 输入操作按钮
            BoxLayout:
                size_hint_y: None
                height: '40dp'
                spacing: 10
                
                Button:
                    text: '🎤 语音'
                    font_size: '14sp'
                    size_hint_x: 0.33
                    on_press: root.start_voice_input()
                
                Button:
                    text: '清空'
                    font_size: '14sp'
                    size_hint_x: 0.33
                    on_press: root.clear_input()
                
                Button:
                    text: '翻译 →'
                    font_size: '14sp'
                    size_hint_x: 0.34
                    background_color: 0.106, 0.369, 0.125, 1
                    color: 1, 1, 1, 1
                    on_press: root.do_translate()
        
        # 翻译结果区域
        BoxLayout:
            size_hint_y: 0.35
            orientation: 'vertical'
            spacing: 5
            
            Label:
                text: '翻译结果'
                font_size: '14sp'
                color: 0.5, 0.5, 0.5, 1
                size_hint_y: None
                height: '25dp'
            
            TextInput:
                id: output_field
                text: root.output_text
                hint_text: '翻译结果将显示在这里'
                font_size: '18sp'
                multiline: True
                padding: 10
                background_color: 0.95, 0.95, 0.95, 1
            
            # 输出操作按钮
            BoxLayout:
                size_hint_y: None
                height: '40dp'
                spacing: 10
                
                Button:
                    text: '🔊 朗读'
                    font_size: '14sp'
                    size_hint_x: 0.25
                    on_press: root.play_result_audio()
                
                Button:
                    text: '📋 复制'
                    font_size: '14sp'
                    size_hint_x: 0.25
                    on_press: root.copy_result()
                
                Button:
                    text: '📤 分享'
                    font_size: '14sp'
                    size_hint_x: 0.25
                    on_press: root.share_result()
                
                Button:
                    text: '⭐ 收藏'
                    font_size: '14sp'
                    size_hint_x: 0.25
                    on_press: root.save_favorite()
        
        # 底部导航
        BoxLayout:
            size_hint_y: None
            height: '50dp'
            spacing: 5
            
            Button:
                text: '🏠 翻译'
                font_size: '14sp'
                on_press: root.manager.current = 'translator'
            
            Button:
                text: '📖 词库'
                font_size: '14sp'
                on_press: root.manager.current = 'dictionary'
            
            Button:
                text: '📋 历史'
                font_size: '14sp'
                on_press: root.manager.current = 'history'
            
            Button:
                text: 'ℹ️ 关于'
                font_size: '14sp'
                on_press: root.manager.current = 'about'
"""

# 词汇库页面布局
DICTIONARY_KV = """
<DictionaryScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 15
        spacing: 10
        
        # 顶部标题
        BoxLayout:
            size_hint_y: None
            height: '60dp'
            spacing: 10
            
            Button:
                text: '←'
                font_size: '24sp'
                size_hint_x: 0.15
                on_press: root.manager.current = 'translator'
            
            Label:
                text: '文旅词汇库'
                font_size: '22sp'
                bold: True
                color: 0.106, 0.369, 0.125, 1
        
        # 搜索栏
        BoxLayout:
            size_hint_y: None
            height: '50dp'
            spacing: 10
            
            TextInput:
                id: search_input
                hint_text: '搜索词汇...'
                font_size: '16sp'
                padding: 10
            
            Button:
                text: '搜索'
                font_size: '14sp'
                size_hint_x: 0.25
                on_press: root.load_words(root.current_category, search_input.text)
        
        # 分类标签
        ScrollView:
            size_hint_y: None
            height: '50dp'
            do_scroll_x: True
            do_scroll_y: False
            
            BoxLayout:
                id: category_scroll
                size_hint_x: None
                width: '800dp'
                spacing: 5
                padding: [5, 5]
                
                Button:
                    text: '日常'
                    size_hint_x: None
                    width: '80dp'
                    on_press: root.load_words('daily')
                
                Button:
                    text: '旅游'
                    size_hint_x: None
                    width: '80dp'
                    on_press: root.load_words('lvyou')
                
                Button:
                    text: '节日'
                    size_hint_x: None
                    width: '80dp'
                    on_press: root.load_words('festival')
                
                Button:
                    text: '美食'
                    size_hint_x: None
                    width: '80dp'
                    on_press: root.load_words('food')
                
                Button:
                    text: '建筑'
                    size_hint_x: None
                    width: '80dp'
                    on_press: root.load_words('building')
                
                Button:
                    text: '服饰'
                    size_hint_x: None
                    width: '80dp'
                    on_press: root.load_words('clothing')
                
                Button:
                    text: '礼仪'
                    size_hint_x: None
                    width: '80dp'
                    on_press: root.load_words('etiquette')
                
                Button:
                    text: '问路'
                    size_hint_x: None
                    width: '80dp'
                    on_press: root.load_words('direction')
        
        # 词条列表
        RecycleView:
            id: word_list
            viewclass: 'WordItemWidget'
            data: root.word_items
        
        # 文化科普卡片
        BoxLayout:
            size_hint_y: None
            height: '120dp'
            orientation: 'vertical'
            padding: 10
            canvas:
                Color:
                    rgba: 0.95, 0.92, 0.87, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [8]
            
            Label:
                text: '📚 文化小科普'
                font_size: '16sp'
                bold: True
                size_hint_y: None
                height: '30dp'
            
            ScrollView:
                size_hint_y: None
                height: '75dp'
                
                Label:
                    text: '十月年（cilceiq）：哈尼族最隆重的传统节日，相当于汉族的春节。长街宴是十月年期间的传统宴席，被誉为"天下第一长街宴"。'
                    font_size: '13sp'
                    text_size: self.width, None
                    size_hint_y: None
"""


# 历史记录页面布局
HISTORY_KV = """
<HistoryScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 15
        spacing: 10
        
        # 顶部标题
        BoxLayout:
            size_hint_y: None
            height: '60dp'
            spacing: 10
            
            Button:
                text: '←'
                font_size: '24sp'
                size_hint_x: 0.15
                on_press: root.manager.current = 'translator'
            
            Label:
                text: '翻译历史'
                font_size: '22sp'
                bold: True
                color: 0.106, 0.369, 0.125, 1
            
            Button:
                text: '清空'
                font_size: '14sp'
                size_hint_x: 0.25
                on_press: root.clear_all()
        
        # 历史记录列表
        RecycleView:
            id: history_list
            viewclass: 'HistoryItemWidget'
            data: root.history_items
        
        # 空状态提示
        Label:
            text: '暂无翻译历史'
            font_size: '16sp'
            color: 0.5, 0.5, 0.5, 1
            opacity: 1 if len(root.history_items) == 0 else 0
"""


# 关于页面布局
ABOUT_KV = """
<AboutScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        
        # 顶部返回
        BoxLayout:
            size_hint_y: None
            height: '50dp'
            spacing: 10
            
            Button:
                text: '←'
                font_size: '24sp'
                size_hint_x: 0.15
                on_press: root.manager.current = 'translator'
            
            Label:
                text: '关于'
                font_size: '22sp'
                bold: True
        
        # 应用图标区域
        BoxLayout:
            size_hint_y: 0.25
            orientation: 'vertical'
            padding: 20
            
            Label:
                text: '🧭'
                font_size: '60sp'
                halign: 'center'
            
            Label:
                text: root.app_name
                font_size: '24sp'
                bold: True
                halign: 'center'
                color: 0.106, 0.369, 0.125, 1
            
            Label:
                text: '版本 ' + root.version
                font_size: '14sp'
                halign: 'center'
                color: 0.5, 0.5, 0.5, 1
        
        # 应用介绍
        BoxLayout:
            orientation: 'vertical'
            padding: 15
            canvas:
                Color:
                    rgba: 0.95, 0.95, 0.95, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [10]
            
            Label:
                text: '应用介绍'
                font_size: '18sp'
                bold: True
                size_hint_y: None
                height: '40dp'
            
            Label:
                text: '绿县文旅哈尼语-汉语双向翻译应用，服务于绿春县游客、文旅工作人员和本地哈尼群众。提供日常对话、旅游问路、民俗交流等功能，兼顾民族文化保护与传播。'
                font_size: '14sp'
                text_size: self.width, None
                size_hint_y: None
        
        # 词条统计
        BoxLayout:
            orientation: 'vertical'
            padding: 15
            canvas:
                Color:
                    rgba: 0.95, 0.95, 0.95, 1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [10]
            
            Label:
                text: '词条统计'
                font_size: '18sp'
                bold: True
                size_hint_y: None
                height: '40dp'
            
            Label:
                text: '内置词条: ' + str(root.get_word_count()) + ' 条'
                font_size: '16sp'
                size_hint_y: None
                height: '30dp'
        
        # 版权信息
        BoxLayout:
            size_hint_y: 0.15
            orientation: 'vertical'
            
            Label:
                text: '© 2024 绿县文旅翻译通'
                font_size: '12sp'
                halign: 'center'
                color: 0.5, 0.5, 0.5, 1
            
            Label:
                text: '保留所有权利'
                font_size: '12sp'
                halign: 'center'
                color: 0.5, 0.5, 0.5, 1
"""

# 词条项组件
WORD_ITEM_KV = """
<WordItemWidget>:
    size_hint_y: None
    height: '80dp'
    padding: 10
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [5]
        Color:
            rgba: 0.9, 0.9, 0.9, 1
        Line:
            points: [self.x, self.y, self.x + self.width, self.y]
            width: 1
    
    BoxLayout:
        orientation: 'vertical'
        spacing: 5
        
        # 汉语
        Label:
            text: root.zh_text
            font_size: '16sp'
            bold: True
            size_hint_y: None
            height: '25dp'
        
        # 哈尼语
        Label:
            text: root.hani_text
            font_size: '14sp'
            color: 0.3, 0.3, 0.3, 1
            size_hint_y: None
            height: '20dp'
        
        # 操作按钮
        BoxLayout:
            size_hint_y: None
            height: '25dp'
            spacing: 10
            
            Button:
                text: '🔊'
                font_size: '14sp'
                size_hint_x: 0.2
                on_press: root.play_audio()
            
            Button:
                text: '⭐' if not root.is_favorite else '★'
                font_size: '14sp'
                size_hint_x: 0.2
                on_press: root.toggle_favorite()
"""

# 历史记录项组件
HISTORY_ITEM_KV = """
<HistoryItemWidget>:
    size_hint_y: None
    height: '100dp'
    padding: 10
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [5]
    
    BoxLayout:
        orientation: 'vertical'
        spacing: 5
        
        # 原文
        Label:
            text: root.source_text
            font_size: '14sp'
            color: 0.3, 0.3, 0.3, 1
            size_hint_y: None
            height: '30dp'
            text_size: self.width, None
        
        # 译文
        Label:
            text: root.result_text
            font_size: '16sp'
            bold: True
            size_hint_y: None
            height: '30dp'
            text_size: self.width, None
        
        # 操作按钮和时间
        BoxLayout:
            size_hint_y: None
            height: '30dp'
            spacing: 10
            
            Label:
                text: root.timestamp
                font_size: '12sp'
                color: 0.5, 0.5, 0.5, 1
                size_hint_x: 0.5
            
            Button:
                text: '🔊'
                font_size: '12sp'
                size_hint_x: 0.15
                on_press: root.play_audio()
            
            Button:
                text: '📋'
                font_size: '12sp'
                size_hint_x: 0.15
                on_press: root.copy_text()
            
            Button:
                text: '🗑'
                font_size: '12sp'
                size_hint_x: 0.15
                on_press: root.delete_item()
"""


# 启动页面布局
SPLASH_KV = """
<SplashScreen>:
    canvas:
        Color:
            rgba: 0.106, 0.369, 0.125, 1
        Rectangle:
            pos: self.pos
            size: self.size
    
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 30
        pos: root.pos
        size: root.size
        
        Label:
            text: '🧭'
            font_size: '80sp'
            halign: 'center'
           _opacity: root.opacity
        
        Label:
            text: '绿县文旅翻译通'
            font_size: '28sp'
            bold: True
            color: 1, 1, 1, 1
            halign: 'center'
            opacity: root.opacity
        
        Label:
            text: '绿春哈尼语 · 汉语 双语互译'
            font_size: '16sp'
            color: 0.9, 0.9, 0.9, 1
            halign: 'center'
            opacity: root.opacity
        
        Label:
            text: 'loading...'
            font_size: '14sp'
            color: 0.8, 0.8, 0.8, 1
            halign: 'center'
            opacity: root.opacity
"""


# 组合所有布局
ALL_KV = (
    MAIN_TRANSLATOR_KV
    + DICTIONARY_KV
    + HISTORY_KV
    + ABOUT_KV
    + WORD_ITEM_KV
    + HISTORY_ITEM_KV
    + SPLASH_KV
)
