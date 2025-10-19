"""
示例JSON数据模块 - Example JSON Data Module

这个模块演示如何返回JSON格式的数据
This module demonstrates how to return JSON format data

访问路径 - Access Path:
GET /template/json/example?param1=value1&param2=value2

返回示例 - Return Example:
{
  "status": "success",
  "data": {
    "param1": "value1",
    "param2": "value2",
    "message": "This is example JSON data"
  }
}
"""

from flask import jsonify

def to_json(param1='默认值1', param2='默认值2'):
    """
    返回JSON数据 - Return JSON data
    
    这个函数是JSON模块的入口点，必须存在
    This function is the entry point of the JSON module and must exist
    
    参数 - Parameters:
        param1: 自定义参数1，从URL查询参数获取
                Custom parameter 1, from URL query parameters
        param2: 自定义参数2，从URL查询参数获取
                Custom parameter 2, from URL query parameters
    
    返回 - Returns:
        Flask jsonify 响应对象
        Flask jsonify response object
    
    注意事项 - Notes:
        1. 参数会自动从URL查询参数中提取
           Parameters are automatically extracted from URL query parameters
        2. 支持类型转换：int, float, bool, str
           Type conversion supported: int, float, bool, str
        3. 参数应设置默认值，避免缺参错误
           Parameters should have default values to avoid missing parameter errors
    """
    
    # 示例：从 lib 模块导入业务逻辑
    # Example: Import business logic from lib module
    # from plugins.template.lib.data_processor import process_data
    # processed_data = process_data(param1, param2)
    
    # 构建返回数据
    # Build return data
    result = {
        "status": "success",
        "data": {
            "param1": param1,
            "param2": param2,
            "message": "This is example JSON data from template plugin"
        },
        "meta": {
            "version": "1.0",
            "plugin": "template"
        }
    }
    
    # 返回 JSON 响应
    # Return JSON response
    return jsonify(result)
