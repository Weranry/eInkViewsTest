#----------------------------------服务器配置-----------------------------------#
#----------------------------------鉴权配置-------------------------------------#
ENABLE_AUTH = False
# 跳过鉴权的插件列表
PLUGIN_WHITELIST = [

]
#----------------------------------默认参数配置---------------------------------#
# 默认旋转角度
DEFAULT_ROTATE = 0
# 默认是否反色
DEFAULT_INVERT = False
# 默认图片质量（JPEG）
DEFAULT_IMAGE_QUALITY = 100
#----------------------------------缓存配置-------------------------------------#
# 字体加载缓存
ENABLE_FONT_CACHE = True
# 字体缓存数
FONT_CACHE_SIZE = 128

# 模块导入缓存
ENABLE_MODULE_IMPORT_CACHE = False
# 模块缓存数
MODULE_IMPORT_CACHE_SIZE = 256

# 视图 HTTP 缓存
ENABLE_VIEW_CACHE = False
# 视图缓存时间（秒）
VIEW_CACHE_MAX_AGE = 300  # 5分钟

# 随机视图 HTTP 缓存
ENABLE_RANDOM_VIEW_CACHE = False
# 随机视图缓存时间（秒）
RANDOM_VIEW_CACHE_MAX_AGE = 60  # 1分钟
#-----------------------------------其他---------------------------------------#


