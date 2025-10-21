import importlib
import io
import os
import hashlib
from flask import send_file, request, make_response
from functools import lru_cache
from modules.errors.errors import ParamError
from config import DEFAULT_IMAGE_QUALITY, DEFAULT_ROTATE, DEFAULT_INVERT, VIEW_CACHE_MAX_AGE, MODULE_IMPORT_CACHE_SIZE, ENABLE_VIEW_CACHE, ENABLE_MODULE_IMPORT_CACHE

# 缓存已导入的模块
def _import_view_module(module_path):
    return importlib.import_module(module_path)

if ENABLE_MODULE_IMPORT_CACHE:
    _import_view_module = lru_cache(maxsize=MODULE_IMPORT_CACHE_SIZE)(_import_view_module)

def _generate_etag(plugin_name, kind, size, **params):
    """生成ETag用于HTTP缓存"""
    # 将所有参数排序后组合成字符串
    param_str = ''.join(f'{k}={v}' for k, v in sorted(params.items()))
    etag_source = f'{plugin_name}:{kind}:{size}:{param_str}'
    return hashlib.md5(etag_source.encode()).hexdigest()

def register_view_routes(bp, plugin_name, view_dir):
    # 遍历 view_dir 下所有子目录（视图类）
    for kind in os.listdir(view_dir):
        kind_path = os.path.join(view_dir, kind)
        if not os.path.isdir(kind_path):
            continue
        # 注册路由: /{plugin}/view/{kind}
        def make_view_func(kind=kind):  # 绑定默认参数，防止闭包陷阱
            def view_func():
                size = request.args.get('size')
                if not size:
                    raise ParamError('缺少 size 参数')
                try:
                    mod = _import_view_module(f'plugins.{plugin_name}.view.{kind}.{size}')
                except ModuleNotFoundError:
                    raise ParamError(f'视图 {plugin_name}.view.{kind}.{size} 不存在')
                if not hasattr(mod, 'generate_image'):
                    raise ParamError(f'视图 {plugin_name}.view.{kind}.{size} 未实现 generate_image')
                rotate_arg = request.args.get('rotate')
                rotate_map = {'c': 270, 'cc': 90, 'h': 180}
                rotate = rotate_map.get(rotate_arg, DEFAULT_ROTATE)
                invert_arg = request.args.get('invert')
                invert_map = {'t': True, 'f': False}
                if invert_arg is None:
                    invert = DEFAULT_INVERT
                else:
                    try:
                        invert = invert_map[invert_arg]
                    except KeyError:
                        raise ParamError('invert 参数必须为 t 或 f')
                # 只过滤全局参数，其余全部传递给插件
                plugin_args = {
                    k: v for k, v in request.args.items()
                    if k not in ('size', 'rotate', 'invert')
                }
                
                # 生成ETag用于HTTP缓存
                all_params = {'rotate': rotate, 'invert': invert, **plugin_args}
                etag = _generate_etag(plugin_name, kind, size, **all_params)
                
                # 检查客户端缓存
                if ENABLE_VIEW_CACHE and request.headers.get('If-None-Match') == etag:
                    response = make_response('', 304)
                    response.headers['ETag'] = etag
                    return response
                
                try:
                    img = mod.generate_image(rotate=rotate, invert=invert, **plugin_args)
                except Exception as e:
                    raise ParamError(f'图片生成失败: {str(e)}')
                buf = io.BytesIO()
                img.save(buf, format='JPEG', quality=DEFAULT_IMAGE_QUALITY, subsampling=0, progressive=False)
                buf.seek(0)
                response = make_response(send_file(buf, mimetype='image/jpeg'))
                # 优先使用视图模块自定义缓存时间
                cache_max_age = getattr(mod, 'CACHE_MAX_AGE', VIEW_CACHE_MAX_AGE)
                if ENABLE_VIEW_CACHE:
                    response.headers['ETag'] = etag
                    response.headers['Cache-Control'] = f'public, max-age={cache_max_age}'
                return response
            view_func.__name__ = f'view_{plugin_name}_{kind}'
            return view_func
        bp.add_url_rule(f'/{plugin_name}/view/{kind}', view_func=make_view_func())