import sys
sys.dont_write_bytecode = True
from flask import Flask
from modules.plugins.plugin_loader import register_plugins
from modules.auth.auth import setup_auth
from modules.errors.errors import register_error_handlers
from modules.register.random_view_route import bp_random

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.json.ensure_ascii = False
setup_auth(app)
register_plugins(app)
register_error_handlers(app)
app.register_blueprint(bp_random)

@app.after_request
def ensure_json_utf8(response):
    content_type = response.headers.get('Content-Type', '')
    if content_type.startswith('application/json'):
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

if __name__ == '__main__':
    app.run()


