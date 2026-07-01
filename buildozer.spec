# 绿县文旅翻译通 - APK打包配置文件
# 使用Buildozer进行Android打包
# 
# 安装依赖:
#   pip install buildozer
#   pip install cython
#
# 打包命令:
#   buildozer android debug

[app]
# 应用名称（标题）
title = 绿县文旅翻译通

# 应用包名
package.name = lv_trlator

# 应用域名（反向域名）
package.domain = com.lvcounty

# 应用版本
version = 1.0.0

# 源代码目录
source.dir = .

# 排除的文件
source.include_exts = py,png,jpg,kv,atlas,json,wav,mp3

# 主入口文件
main = main.py

# 要求的Kivy版本
requirements = kivy==2.3.0

# 屏幕方向
orientation = portrait

# 全屏显示
fullscreen = 0

# Android特定配置
android.permissions = INTERNET,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android元数据
android.meta_data = com.google.android.gms.version=@integer/google_play_services_version

# Android启动画面
android.uses_library = com.google.android.gms

# 图标
icon.filename = resources/icon.png

# 启动画面
splash.filename = resources/splash.png

# Android API级别
android.api = 31

# Android最低版本
android.minapi = 21

# Android NDK版本
android.ndk = 23b

# 启用AndroidX
android.enable_androidx = 1

# Android需求模块
android.allow_backup = 1

# 日志级别
android.log_level = 3

# 禁用弃用警告
android.disable_deprecated_warnings = 1

# 发行版密钥库配置（需替换为实际密钥）
android.keystore = keystore.jks
android.keystore_alias = alias_name
android.keystore_password = your_keystore_password
android.keystore_alias_password = your_alias_password

[buildozer]
# 日志级别
log_level = 2

# 打包过程中的并行进程数
jobs = 4

# 是否在打包前清理
build_dir = ./.buildozer

# 是否在打包前创建随机包名（防止应用覆盖）
android.packaging.invalidate_cache = 0

# 强制下载所有依赖
android.download.force = 0

# 禁止更新
android.update_check = 0

# 指定p4a版本
android.p4a_dir = 

# 指定python-for-android版本
android.p4a_force_staging_library = 0

# 是否使用虚拟env
use_virtualenv = 0

# 是否启用bootstrap
android.bootstrap = sdl2

# SDL2支持
android.sdl2 = 1

# 警告作为错误
warn_on_root = 1

# 禁止检查root
disable_root_check = 1

# 是否打包Java源码
android.java_source = 0

# 是否打包C源码
android.cython_compile_time = 0

# 是否允许符号（调试用）
allow_debug_licenses = 0