def startup_banner():
    print(
        "         ___           _     __     __  _                         \n"
        "   ___  |_ _|  _ __   | | __ \\ \\   / / (_)   ___  __      __  ___ \n"
        "  / _ \\  | |  | '_ \\  | |/ /  \\ \\ / /  | |  / _ \\ \\ \\ /\\ / / / __|\n"
        " |  __/  | |  | | | | |   <    \\ V /   | | |  __/  \\ V  V /  \\__ \\\n"
        "  \\___| |___| |_| |_| |_|\\_\\    \\_/    |_|  \\___|   \\_/\\_/   |___/\n"
        "                                                                  "
    )

def create_app():
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

    return app
