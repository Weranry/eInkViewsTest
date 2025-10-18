# 全局配置文件，集中管理所有默认参数和白名单

# 跳过鉴权的插件名列表
PLUGIN_WHITELIST = [

]

# 是否开启鉴权
ENABLE_AUTH = False

# 默认旋转角度（如 0, 90, 180, 270）
DEFAULT_ROTATE = 0

# 默认是否反色
DEFAULT_INVERT = False

# 默认图片质量（JPEG）
DEFAULT_IMAGE_QUALITY = 100

# HTTP缓存配置
# 视图缓存时间（秒）
VIEW_CACHE_MAX_AGE = 300  # 5分钟

# 随机视图缓存时间（秒）
RANDOM_VIEW_CACHE_MAX_AGE = 60  # 1分钟

# 字体缓存大小
FONT_CACHE_SIZE = 128

# 模块导入缓存大小
MODULE_IMPORT_CACHE_SIZE = 256
