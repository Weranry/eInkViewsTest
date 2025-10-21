import importlib
import os
from flask import Flask
import sys
import time
import traceback

def register_plugins(app: Flask, plugins_dir='plugins'):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    plugin_names = [
        name for name in os.listdir(plugins_dir)
        if os.path.isdir(os.path.join(plugins_dir, name)) and os.path.exists(os.path.join(plugins_dir, name, 'routes.py'))
    ]
    total = len(plugin_names)
    success = 0
    failed = 0
    if not plugin_names:
        print('未发现插件，请在 plugins 目录下添加插件')
        return
    for plugin_name in plugin_names:
        routes_module = f'{plugins_dir}.{plugin_name}.routes'
        try:
            start = time.time()
            module = importlib.import_module(routes_module)
            if hasattr(module, 'bp'):
                app.register_blueprint(module.bp)
            elapsed = time.time() - start
            print(f'插件 {plugin_name} 加载成功，用时 {elapsed:.3f}s')
            success += 1
        except Exception as e:
            print(f'插件 {plugin_name} 加载失败: {e}')
            traceback.print_exc()
            failed += 1
    print(f'插件加载统计：成功 {success} 个，失败 {failed} 个，共 {total} 个')
