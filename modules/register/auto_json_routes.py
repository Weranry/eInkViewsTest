import importlib
import os
from flask import request

def _convert_arg(val, anno):
    if val is None:
        return None
    if anno is int:
        try:
            return int(val)
        except Exception:
            return None
    if anno is float:
        try:
            return float(val)
        except Exception:
            return None
    if anno is bool:
        try:
            return bool(int(val))
        except Exception:
            return None
    return val

def register_json_routes(bp, plugin_name, json_module_dir):
    for fname in os.listdir(json_module_dir):
        if fname.endswith('.py') and fname != '__init__.py':
            mod_name = fname[:-3]
            mod = importlib.import_module(f'plugins.{plugin_name}.json_module.{mod_name}')
            for attr in dir(mod):
                if attr.startswith('to_json'):
                    func = getattr(mod, attr)
                    route_name = attr.replace('to_json', '').lstrip('_') or mod_name
                    route_path = f'/{plugin_name}/json/{route_name}'
                    def make_json_func(f, plugin_name=plugin_name, route_name=route_name, mod_name=mod_name):
                        def json_func():
                            # 类型自动转换
                            arg_names = f.__code__.co_varnames[:f.__code__.co_argcount]
                            annos = getattr(f, '__annotations__', {})
                            args = []
                            for name in arg_names:
                                val = request.args.get(name, None)
                                anno = annos.get(name, str)
                                args.append(_convert_arg(val, anno))
                            return f(*args)
                        # endpoint 唯一化
                        json_func.__name__ = f'json_{plugin_name}_{route_name}_{mod_name}'
                        return json_func
                    bp.add_url_rule(route_path, view_func=make_json_func(func))
