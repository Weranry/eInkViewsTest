"""
横向2XL尺寸视图 - Horizontal 2X Large Size View
尺寸 - Size: 400x300 像素 (pixels)
方向 - Orientation: 横向 (Horizontal)

访问路径 - Access Path:
GET /template/view/example?size=h2xl&param1=value1&param2=value2
"""

from .utils import prepare_canvas, finalize_image, get_example_data

def generate_image(rotate=0, invert=False, param1='默认值1', param2='默认值2'):
    """生成 h2xl 尺寸图像 - Generate h2xl size image"""
    
    img, draw, font = prepare_canvas('h2xl', font_size=36)
    data = get_example_data(param1, param2)
    
    # 绘制标题
    draw.text((15, 15), "Template Plugin", font=font, fill=1)
    
    # 绘制数据
    medium_font = prepare_canvas('h2xl', font_size=24)[2]
    draw.text((15, 70), data, font=medium_font, fill=1)
    
    # 绘制更多示例内容
    small_font = prepare_canvas('h2xl', font_size=18)[2]
    draw.text((15, 120), "这是一个插件模板示例", font=small_font, fill=1)
    draw.text((15, 150), "This is a plugin template example", font=small_font, fill=1)
    
    # 绘制尺寸标识
    tiny_font = prepare_canvas('h2xl', font_size=14)[2]
    draw.text((15, img.height - 30), "h2xl: 400x300", font=tiny_font, fill=1)
    
    # 绘制边框
    draw.rectangle([0, 0, img.width - 1, img.height - 1], outline=1, width=2)
    
    return finalize_image(img, rotate=rotate, invert=invert)
