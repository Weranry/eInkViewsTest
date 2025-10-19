"""
纵向XL尺寸视图 - Vertical Extra Large Size View
尺寸 - Size: 184x384 像素 (pixels)
方向 - Orientation: 纵向 (Vertical)

访问路径 - Access Path:
GET /template/view/example?size=vxl&param1=value1&param2=value2
"""

from .utils import prepare_canvas, finalize_image, get_example_data

def generate_image(rotate=0, invert=False, param1='默认值1', param2='默认值2'):
    """生成 vxl 尺寸图像 - Generate vxl size image"""
    
    img, draw, font = prepare_canvas('vxl', font_size=24)
    data = get_example_data(param1, param2)
    
    # 绘制标题
    draw.text((10, 10), "Template", font=font, fill=1)
    draw.text((10, 40), "Plugin", font=font, fill=1)
    
    # 绘制数据
    small_font = prepare_canvas('vxl', font_size=18)[2]
    draw.text((10, 80), data, font=small_font, fill=1)
    
    # 绘制尺寸标识
    tiny_font = prepare_canvas('vxl', font_size=14)[2]
    draw.text((10, img.height - 25), "vxl: 184x384", font=tiny_font, fill=1)
    
    # 绘制边框
    draw.rectangle([0, 0, img.width - 1, img.height - 1], outline=1, width=1)
    
    return finalize_image(img, rotate=rotate, invert=invert)
