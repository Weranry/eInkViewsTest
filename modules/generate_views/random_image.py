import importlib
from functools import lru_cache
from modules.errors.errors import ParamError
from config import MODULE_IMPORT_CACHE_SIZE, ENABLE_MODULE_IMPORT_CACHE

def _import_view_module(module_path):
    return importlib.import_module(module_path)

if ENABLE_MODULE_IMPORT_CACHE:
    _import_view_module = lru_cache(maxsize=MODULE_IMPORT_CACHE_SIZE)(_import_view_module)

def generate_random_image(view_path, size, rotate=0, invert=False, **extra_params):
    # view_path: "date.kinda", size: "hm"
    if not size:
        raise ParamError('缺少 size 参数')
    if '.' not in view_path:
        raise ParamError('view_path 格式应为 插件名.视图类')
    plugin, kind = view_path.split('.', 1)
    mod_path = f'plugins.{plugin}.view.{kind}.{size}'
    try:
        mod = _import_view_module(mod_path)
    except ModuleNotFoundError:
        raise ParamError(f'视图 {mod_path} 不存在')
    if not hasattr(mod, 'generate_image'):
        raise ParamError(f'视图 {mod_path} 未实现 generate_image')
    kwargs = dict(rotate=rotate, invert=invert, **extra_params)
    return mod.generate_image(**kwargs)