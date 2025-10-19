"""
横向4XL尺寸视图 - Horizontal 4X Large Size View
尺寸 - Size: 800x480 像素 (pixels)
方向 - Orientation: 横向 (Horizontal)

访问路径 - Access Path:
GET /template/view/example?size=h4xl&param1=value1&param2=value2
"""

from .utils import prepare_canvas, finalize_image, get_example_data

def generate_image(rotate=0, invert=False, param1='默认值1', param2='默认值2'):
    """生成 h4xl 尺寸图像 - Generate h4xl size image"""
    
    img, draw, font = prepare_canvas('h4xl', font_size=56)
    data = get_example_data(param1, param2)
    
    # 绘制大标题
    draw.text((25, 25), "Template Plugin", font=font, fill=1)
    
    # 绘制数据
    large_font = prepare_canvas('h4xl', font_size=40)[2]
    draw.text((25, 110), data, font=large_font, fill=1)
    
    # 绘制更多内容
    medium_font = prepare_canvas('h4xl', font_size=28)[2]
    draw.text((25, 180), "这是一个插件模板示例", font=medium_font, fill=1)
    draw.text((25, 225), "This is a plugin template", font=medium_font, fill=1)
    draw.text((25, 270), "适合最大尺寸的墨水屏", font=medium_font, fill=1)
    draw.text((25, 315), "Suitable for the largest e-ink display", font=medium_font, fill=1)
    
    # 绘制尺寸标识
    small_font = prepare_canvas('h4xl', font_size=18)[2]
    draw.text((25, img.height - 40), "h4xl: 800x480", font=small_font, fill=1)
    
    # 绘制边框
    draw.rectangle([0, 0, img.width - 1, img.height - 1], outline=1, width=2)
    
    return finalize_image(img, rotate=rotate, invert=invert)
