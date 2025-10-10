import importlib
import io
import os
from flask import send_file, request
from modules.errors.errors import ParamError
from config import DEFAULT_IMAGE_QUALITY, DEFAULT_ROTATE, DEFAULT_INVERT

def register_view_routes(bp, plugin_name, view_dir):
    # 遍历 view_dir 下所有子目录（视图类）
    for kind in os.listdir(view_dir):
        kind_path = os.path.join(view_dir, kind)
        if not os.path.isdir(kind_path):
            continue
        # 注册路由: /{plugin}/view/{kind}
        def make_view_func(kind=kind):  # 绑定默认参数，防止闭包陷阱
            def view_func():
                code = request.args.get('code')
                if not code:
                    raise ParamError('缺少 code 参数')
                try:
                    mod = importlib.import_module(f'plugins.{plugin_name}.view.{kind}.{code}')
                except ModuleNotFoundError:
                    raise ParamError(f'视图 {plugin_name}.view.{kind}.{code} 不存在')
                if not hasattr(mod, 'generate_image'):
                    raise ParamError(f'视图 {plugin_name}.view.{kind}.{code} 未实现 generate_image')
                rotate_arg = request.args.get('rotate')
                try:
                    rotate = int(rotate_arg) if rotate_arg is not None else DEFAULT_ROTATE
                except ValueError:
                    raise ParamError('rotate 参数必须为整数')
                invert_arg = request.args.get('invert')
                if invert_arg is None:
                    invert = DEFAULT_INVERT
                else:
                    try:
                        invert = bool(int(invert_arg))
                    except ValueError:
                        raise ParamError('invert 参数必须为 0 或 1')
                # 自动收集所有额外参数
                extra_args = {
                    k: v for k, v in request.args.items()
                    if k not in ('code', 'rotate', 'invert')
                }
                try:
                    img = mod.generate_image(rotate=rotate, invert=invert, **extra_args)
                except Exception as e:
                    raise ParamError(f'图片生成失败: {str(e)}')
                buf = io.BytesIO()
                img.save(buf, format='JPEG', quality=DEFAULT_IMAGE_QUALITY, subsampling=0, progressive=False)
                buf.seek(0)
                return send_file(buf, mimetype='image/jpeg')
            # 唯一化函数名
            view_func.__name__ = f'view_{plugin_name}_{kind}'
            return view_func
        bp.add_url_rule(f'/{plugin_name}/view/{kind}', view_func=make_view_func())