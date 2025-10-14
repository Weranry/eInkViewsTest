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
    for plugin_name in os.listdir(plugins_dir):
        plugin_path = os.path.join(plugins_dir, plugin_name)
        routes_module = f'{plugins_dir}.{plugin_name}.routes'
        if os.path.isdir(plugin_path) and os.path.exists(os.path.join(plugin_path, 'routes.py')):
            try:
                start = time.time()
                module = importlib.import_module(routes_module)
                if hasattr(module, 'bp'):
                    app.register_blueprint(module.bp)
                elapsed = time.time() - start
                print(f'插件 {plugin_name} 加载成功，用时 {elapsed:.3f}s')
            except Exception as e:
                print(f'插件 {plugin_name} 加载失败: {e}')
                traceback.print_exc()
