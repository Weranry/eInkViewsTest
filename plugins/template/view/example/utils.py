"""
视图工具函数 - View Utility Functions
这个文件包含了视图生成的辅助函数
This file contains helper functions for view generation

主要功能 - Main Features:
1. prepare_canvas: 准备画布、画笔和字体
   prepare_canvas: Prepare canvas, draw object and font
2. finalize_image: 完成图像处理（旋转、反色）
   finalize_image: Finalize image processing (rotation, inversion)
3. 其他自定义工具函数
   Other custom utility functions
"""

from modules.generate_views.canvas_factory import prepare_canvas_with_font, finalize_image_common

# 字体路径配置 - Font Path Configuration
# 你可以使用系统字体或自定义字体
# You can use system fonts or custom fonts
FONT_PATHS = {
    'default': 'static/fonts/font.ttf',
    'bold': 'static/fonts/font_bold.ttf',
    # 添加更多字体路径...
    # Add more font paths...
    # 'custom': 'plugins/template/assets/custom_font.ttf',
}

def prepare_canvas(kind, font_size=48, font_type='default'):
    """
    准备画布和字体 - Prepare canvas and font
    
    参数 - Parameters:
        kind (str): 画布类型，如 'hm', 'hL', 'hxl', 'h2xl', 'h3xl', 'h4xl', 
                   'vm', 'vL', 'vxl', 'v2xl', 'v3xl', 'v4xl'
        font_size (int): 字体大小
        font_type (str): 字体类型，对应 FONT_PATHS 中的键
    
    返回 - Returns:
        tuple: (img, draw, font) - 图像对象、绘图对象、字体对象
    
    示例 - Example:
        img, draw, font = prepare_canvas('hm', font_size=48)
        draw.text((10, 10), "Hello World", font=font, fill=1)
    """
    return prepare_canvas_with_font(kind, font_size, font_type, font_paths=FONT_PATHS)

def finalize_image(img, rotate=0, invert=False):
    """
    完成图像处理 - Finalize image processing
    
    参数 - Parameters:
        img: PIL Image 对象
        rotate: 旋转角度，'c'(顺时针90°), 'cc'(逆时针90°), 'h'(180°), 0(不旋转)
        invert: 是否反色，True/False
    
    返回 - Returns:
        处理后的图像响应 - Processed image response
    
    示例 - Example:
        return finalize_image(img, rotate=rotate, invert=invert)
    """
    return finalize_image_common(img, rotate=rotate, invert=invert)

# ============ 添加你的自定义工具函数 - Add Your Custom Utility Functions ============

def get_example_data(param1=None, param2=None):
    """
    示例数据获取函数 - Example data fetching function
    
    你可以在这里添加自己的业务逻辑
    You can add your own business logic here
    
    参数 - Parameters:
        param1: 自定义参数1
        param2: 自定义参数2
    
    返回 - Returns:
        处理后的数据 - Processed data
    """
    # 示例：从 lib 模块导入业务逻辑
    # Example: Import business logic from lib module
    # from plugins.template.lib.data_processor import process_data
    # return process_data(param1, param2)
    
    return f"Example: {param1}, {param2}"
