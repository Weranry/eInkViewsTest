"""
插件路由注册文件 - Plugin Routes Registration
这个文件负责将插件注册到Flask应用中
This file is responsible for registering the plugin to the Flask application

使用说明 - Usage:
1. 修改 PLUGIN_NAME 为你的插件名称（必须与插件目录名一致）
   Change PLUGIN_NAME to your plugin name (must match the plugin directory name)
2. 确保 view 和 json_module 目录存在
   Ensure the view and json_module directories exist
3. 框架会自动扫描并注册所有视图和JSON模块
   The framework will automatically scan and register all views and JSON modules
"""

from flask import Blueprint
import os
from modules.register.auto_view_routes import register_view_routes
from modules.register.auto_json_routes import register_json_routes

# 创建蓝图 - Create Blueprint
# 修改 'template' 为你的插件名称
# Change 'template' to your plugin name
bp = Blueprint('template', __name__)

# 插件名称（必须与目录名一致）
# Plugin name (must match directory name)
PLUGIN_NAME = 'template'

# 视图目录路径
# View directory path
VIEW_DIR = os.path.join(os.path.dirname(__file__), 'view')

# JSON模块目录路径
# JSON module directory path
JSON_MODULE_DIR = os.path.join(os.path.dirname(__file__), 'json_module')

# 自动注册视图路由
# Automatically register view routes
# 路由格式: /{PLUGIN_NAME}/view/{view_name}?size={size}&rotate={r}&invert={i}&...
# Route format: /{PLUGIN_NAME}/view/{view_name}?size={size}&rotate={r}&invert={i}&...
register_view_routes(bp, PLUGIN_NAME, VIEW_DIR)

# 自动注册JSON路由
# Automatically register JSON routes
# 路由格式: /{PLUGIN_NAME}/json/{json_name}?param1=value1&param2=value2&...
# Route format: /{PLUGIN_NAME}/json/{json_name}?param1=value1&param2=value2&...
register_json_routes(bp, PLUGIN_NAME, JSON_MODULE_DIR)
