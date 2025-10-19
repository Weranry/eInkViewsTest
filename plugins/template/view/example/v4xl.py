"""
纵向4XL尺寸视图 - Vertical 4X Large Size View
尺寸 - Size: 480x800 像素 (pixels)
方向 - Orientation: 纵向 (Vertical)

访问路径 - Access Path:
GET /template/view/example?size=v4xl&param1=value1&param2=value2
"""

from .utils import prepare_canvas, finalize_image, get_example_data

def generate_image(rotate=0, invert=False, param1='默认值1', param2='默认值2'):
    """生成 v4xl 尺寸图像 - Generate v4xl size image"""
    
    img, draw, font = prepare_canvas('v4xl', font_size=52)
    data = get_example_data(param1, param2)
    
    # 绘制大标题
    draw.text((25, 25), "Template", font=font, fill=1)
    draw.text((25, 95), "Plugin", font=font, fill=1)
    
    # 绘制数据
    large_font = prepare_canvas('v4xl', font_size=36)[2]
    draw.text((25, 180), data, font=large_font, fill=1)
    
    # 绘制更多内容
    medium_font = prepare_canvas('v4xl', font_size=28)[2]
    draw.text((25, 260), "纵向布局示例", font=medium_font, fill=1)
    draw.text((25, 310), "Vertical Layout", font=medium_font, fill=1)
    draw.text((25, 360), "适合最大尺寸", font=medium_font, fill=1)
    draw.text((25, 410), "墨水屏显示", font=medium_font, fill=1)
    draw.text((25, 460), "Suitable for", font=medium_font, fill=1)
    draw.text((25, 510), "Largest Display", font=medium_font, fill=1)
    
    # 绘制尺寸标识
    small_font = prepare_canvas('v4xl', font_size=18)[2]
    draw.text((25, img.height - 40), "v4xl: 480x800", font=small_font, fill=1)
    
    # 绘制边框
    draw.rectangle([0, 0, img.width - 1, img.height - 1], outline=1, width=2)
    
    return finalize_image(img, rotate=rotate, invert=invert)
