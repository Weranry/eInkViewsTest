"""
纵向2XL尺寸视图 - Vertical 2X Large Size View
尺寸 - Size: 300x400 像素 (pixels)
方向 - Orientation: 纵向 (Vertical)

访问路径 - Access Path:
GET /template/view/example?size=v2xl&param1=value1&param2=value2
"""

from .utils import prepare_canvas, finalize_image, get_example_data

def generate_image(rotate=0, invert=False, param1='默认值1', param2='默认值2'):
    """生成 v2xl 尺寸图像 - Generate v2xl size image"""
    
    img, draw, font = prepare_canvas('v2xl', font_size=32)
    data = get_example_data(param1, param2)
    
    # 绘制标题
    draw.text((15, 15), "Template", font=font, fill=1)
    draw.text((15, 60), "Plugin", font=font, fill=1)
    
    # 绘制数据
    medium_font = prepare_canvas('v2xl', font_size=22)[2]
    draw.text((15, 110), data, font=medium_font, fill=1)
    
    # 绘制更多内容
    small_font = prepare_canvas('v2xl', font_size=18)[2]
    draw.text((15, 160), "纵向布局示例", font=small_font, fill=1)
    draw.text((15, 190), "Vertical Layout", font=small_font, fill=1)
    
    # 绘制尺寸标识
    tiny_font = prepare_canvas('v2xl', font_size=14)[2]
    draw.text((15, img.height - 30), "v2xl: 300x400", font=tiny_font, fill=1)
    
    # 绘制边框
    draw.rectangle([0, 0, img.width - 1, img.height - 1], outline=1, width=2)
    
    return finalize_image(img, rotate=rotate, invert=invert)
