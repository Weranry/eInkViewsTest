"""
数据JSON模块 - Data JSON Module

这个模块演示如何返回简单的数据
This module demonstrates how to return simple data

访问路径 - Access Path:
GET /template/json/data?key=value
"""

from flask import jsonify
from datetime import datetime

def to_json(key='default'):
    """
    返回简单数据 - Return simple data
    
    参数 - Parameters:
        key: 数据键值
    
    返回 - Returns:
        JSON 响应
    """
    
    return jsonify({
        "key": key,
        "timestamp": datetime.now().isoformat(),
        "message": f"Data for key: {key}"
    })
