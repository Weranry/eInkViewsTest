import os
from flask import request, Response
from config import PLUGIN_WHITELIST, ENABLE_AUTH

API_KEY = os.environ.get("API_KEY")
EXEMPT_ROUTES = [
    '/favicon.ico',
    '/',
]

def setup_auth(app):
    if not ENABLE_AUTH:
        return
    if not API_KEY:
        raise RuntimeError("环境变量 API_KEY 未设置，无法启用鉴权")
    @app.before_request
    def verify_api_key():
        for plugin in PLUGIN_WHITELIST:
            if request.path.startswith(f'/{plugin}/'):
                return None
        if request.path in EXEMPT_ROUTES:
            return None
        api_key = request.args.get('api_key') or request.headers.get('X-API-Key')
        if not api_key:
            return Response("请使用 APIKey 访问", status=401, mimetype='text/plain')
        if api_key != API_KEY:
            return Response("无效的 APIKey ，没有权限访问", status=403, mimetype='text/plain')

def should_skip_auth(plugin_name):
    return plugin_name in PLUGIN_WHITELIST