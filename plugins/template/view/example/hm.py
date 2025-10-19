"""
横向小尺寸视图 - Horizontal Medium Size View
尺寸 - Size: 200x200 像素 (pixels)
方向 - Orientation: 横向 (Horizontal)

这是最小尺寸的示例视图，适合简单的信息展示
This is the smallest size example view, suitable for simple information display

访问路径 - Access Path:
GET /template/view/example?size=hm&param1=value1&param2=value2&rotate=0&invert=f

必需参数 - Required Parameters:
- rotate: 旋转角度 (Rotation angle) - 'c', 'cc', 'h', 0
- invert: 是否反色 (Invert colors) - True/False, 't'/'f'

自定义参数 - Custom Parameters:
- param1: 示例参数1 (Example parameter 1)
- param2: 示例参数2 (Example parameter 2)
"""

from .utils import prepare_canvas, finalize_image, get_example_data

def generate_image(rotate=0, invert=False, param1='默认值1', param2='默认值2'):
    """
    生成图像 - Generate Image
    
    这个函数是视图模块的入口点，必须存在
    This function is the entry point of the view module and must exist
    
    参数 - Parameters:
        rotate: 由框架自动传入 (Automatically passed by framework)
        invert: 由框架自动传入 (Automatically passed by framework)
        param1: 自定义参数，从URL查询参数获取 (Custom parameter from URL query)
        param2: 自定义参数，从URL查询参数获取 (Custom parameter from URL query)
    
    返回 - Returns:
        图像响应 (Image response)
    """
    
    # 1. 准备画布 - Prepare canvas
    # 第一个参数 'hm' 必须与文件名一致
    # The first parameter 'hm' must match the filename
    img, draw, font = prepare_canvas('hm', font_size=24)
    
    # 2. 获取数据 - Get data
    data = get_example_data(param1, param2)
    
    # 3. 绘制内容 - Draw content
    # 绘制标题
    # Draw title
    draw.text((10, 10), "Template", font=font, fill=1)
    
    # 绘制数据
    # Draw data
    small_font = prepare_canvas('hm', font_size=18)[2]
    draw.text((10, 50), data, font=small_font, fill=1)
    
    # 绘制尺寸标识
    # Draw size identifier
    tiny_font = prepare_canvas('hm', font_size=14)[2]
    draw.text((10, img.height - 25), "hm: 200x200", font=tiny_font, fill=1)
    
    # 4. 示例：绘制边框（可选）
    # Example: Draw border (optional)
    draw.rectangle([0, 0, img.width - 1, img.height - 1], outline=1, width=2)
    
    # 5. 完成图像处理并返回
    # Finalize image processing and return
    return finalize_image(img, rotate=rotate, invert=invert)
