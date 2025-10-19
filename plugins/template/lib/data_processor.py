"""
数据处理模块 - Data Processing Module

这个模块包含插件的核心业务逻辑
This module contains the core business logic of the plugin

使用场景 - Use Cases:
1. 数据获取和处理
   Data fetching and processing
2. 复杂计算逻辑
   Complex calculation logic
3. 第三方API调用
   Third-party API calls
4. 数据格式转换
   Data format conversion
"""

import requests
from datetime import datetime

def process_data(param1, param2):
    """
    处理数据 - Process data
    
    这是一个示例函数，演示如何处理业务逻辑
    This is an example function demonstrating how to handle business logic
    
    参数 - Parameters:
        param1: 参数1
        param2: 参数2
    
    返回 - Returns:
        处理后的数据 - Processed data
    """
    # 示例：简单的数据处理
    # Example: Simple data processing
    result = f"Processed: {param1} + {param2}"
    return result


def fetch_data_from_api(url, params=None):
    """
    从API获取数据 - Fetch data from API
    
    这是一个通用的API调用示例
    This is a general API call example
    
    参数 - Parameters:
        url (str): API URL
        params (dict): 查询参数
    
    返回 - Returns:
        dict: API 返回的数据
    
    示例 - Example:
        data = fetch_data_from_api('https://api.example.com/data', {'key': 'value'})
    """
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # 错误处理
        # Error handling
        print(f"API request failed: {e}")
        return None


def format_timestamp(timestamp=None, format_str="%Y-%m-%d %H:%M:%S"):
    """
    格式化时间戳 - Format timestamp
    
    参数 - Parameters:
        timestamp: 时间戳（秒），None 表示当前时间
        format_str: 格式字符串
    
    返回 - Returns:
        str: 格式化后的时间字符串
    """
    if timestamp is None:
        dt = datetime.now()
    else:
        dt = datetime.fromtimestamp(timestamp)
    
    return dt.strftime(format_str)


def calculate_example(value1, value2, operation='add'):
    """
    示例计算函数 - Example calculation function
    
    参数 - Parameters:
        value1: 数值1
        value2: 数值2
        operation: 操作类型 ('add', 'subtract', 'multiply', 'divide')
    
    返回 - Returns:
        计算结果 - Calculation result
    """
    try:
        v1 = float(value1)
        v2 = float(value2)
        
        if operation == 'add':
            return v1 + v2
        elif operation == 'subtract':
            return v1 - v2
        elif operation == 'multiply':
            return v1 * v2
        elif operation == 'divide':
            if v2 != 0:
                return v1 / v2
            else:
                return "Error: Division by zero"
        else:
            return "Error: Unknown operation"
    except ValueError:
        return "Error: Invalid number format"


# ============ 添加更多业务逻辑函数 - Add More Business Logic Functions ============

# 你可以在这里添加更多自定义的业务逻辑函数
# You can add more custom business logic functions here
#
# 例如 - Examples:
# - 数据库操作函数
#   Database operation functions
# - 文件处理函数
#   File processing functions
# - 图像处理函数
#   Image processing functions
# - 网络爬虫函数
#   Web scraping functions
