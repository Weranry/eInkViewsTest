"""
纵向3XL尺寸视图 - Vertical 3X Large Size View
尺寸 - Size: 480x600 像素 (pixels)
方向 - Orientation: 纵向 (Vertical)

访问路径 - Access Path:
GET /template/view/example?size=v3xl&param1=value1&param2=value2
"""

from .utils import prepare_canvas, finalize_image, get_example_data

def generate_image(rotate=0, invert=False, param1='默认值1', param2='默认值2'):
    """生成 v3xl 尺寸图像 - Generate v3xl size image"""
    
    img, draw, font = prepare_canvas('v3xl', font_size=42)
    data = get_example_data(param1, param2)
    
    # 绘制大标题
    draw.text((20, 20), "Template", font=font, fill=1)
    draw.text((20, 75), "Plugin", font=font, fill=1)
    
    # 绘制数据
    large_font = prepare_canvas('v3xl', font_size=30)[2]
    draw.text((20, 140), data, font=large_font, fill=1)
    
    # 绘制更多内容
    medium_font = prepare_canvas('v3xl', font_size=24)[2]
    draw.text((20, 200), "纵向布局示例", font=medium_font, fill=1)
    draw.text((20, 240), "Vertical Layout", font=medium_font, fill=1)
    draw.text((20, 280), "适合较大尺寸", font=medium_font, fill=1)
    draw.text((20, 320), "墨水屏显示", font=medium_font, fill=1)
    
    # 绘制尺寸标识
    small_font = prepare_canvas('v3xl', font_size=16)[2]
    draw.text((20, img.height - 35), "v3xl: 480x600", font=small_font, fill=1)
    
    # 绘制边框
    draw.rectangle([0, 0, img.width - 1, img.height - 1], outline=1, width=2)
    
    return finalize_image(img, rotate=rotate, invert=invert)
