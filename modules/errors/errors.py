from flask import jsonify
from werkzeug.exceptions import NotFound

def error_response(message, code=400):
    return jsonify({"success": False, "message": message, "code": code}), code

# 自定义异常
class NotFoundError(Exception):
    pass

class AuthError(Exception):
    pass

class ParamError(Exception):
    pass

def register_error_handlers(app):
    """注册全局错误处理器"""

    # 处理自定义的 NotFoundError
    @app.errorhandler(NotFoundError)
    def handle_not_found_error(e):
        return error_response(str(e), 404)

    # 处理自定义的参数错误
    @app.errorhandler(ParamError)
    def handle_param_error(e):
        return error_response(str(e), 400)

    # 处理标准 404 错误（如路由不存在）
    @app.errorhandler(NotFound)
    def handle_werkzeug_not_found(e):
        return error_response('未找到资源', 404)

    # 处理所有未捕获的异常
    @app.errorhandler(Exception)
    def handle_general_exception(e):
        app.logger.exception(e)
        return error_response('服务器内部错误', 500)