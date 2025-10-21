"""
横向3XL尺寸视图 - Horizontal 3X Large Size View
尺寸 - Size: 600x480 像素 (pixels)
方向 - Orientation: 横向 (Horizontal)

访问路径 - Access Path:
GET /template/view/example?size=h3xl&param1=value1&param2=value2
"""

from .utils import prepare_canvas, finalize_image, get_example_data

def generate_image(rotate=0, invert=False, param1='默认值1', param2='默认值2'):
    """生成 h3xl 尺寸图像 - Generate h3xl size image"""
    
    img, draw, font = prepare_canvas('h3xl', font_size=48)
    data = get_example_data(param1, param2)
    
    # 绘制大标题
    draw.text((20, 20), "Template Plugin", font=font, fill=1)
    
    # 绘制数据
    medium_font = prepare_canvas('h3xl', font_size=32)[2]
    draw.text((20, 90), data, font=medium_font, fill=1)
    
    # 绘制更多内容
    small_font = prepare_canvas('h3xl', font_size=24)[2]
    draw.text((20, 160), "这是一个插件模板示例", font=small_font, fill=1)
    draw.text((20, 200), "This is a plugin template", font=small_font, fill=1)
    draw.text((20, 240), "适合较大尺寸的墨水屏", font=small_font, fill=1)
    
    # 绘制尺寸标识
    tiny_font = prepare_canvas('h3xl', font_size=16)[2]
    draw.text((20, img.height - 35), "h3xl: 600x480", font=tiny_font, fill=1)
    
    # 绘制边框
    draw.rectangle([0, 0, img.width - 1, img.height - 1], outline=1, width=2)
    
    return finalize_image(img, rotate=rotate, invert=invert)
