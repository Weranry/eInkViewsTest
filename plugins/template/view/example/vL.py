"""
纵向L尺寸视图 - Vertical Large Size View
尺寸 - Size: 122x250 像素 (pixels)
方向 - Orientation: 纵向 (Vertical)

访问路径 - Access Path:
GET /template/view/example?size=vL&param1=value1&param2=value2
"""

from .utils import prepare_canvas, finalize_image, get_example_data

def generate_image(rotate=0, invert=False, param1='默认值1', param2='默认值2'):
    """生成 vL 尺寸图像 - Generate vL size image"""
    
    img, draw, font = prepare_canvas('vL', font_size=18)
    data = get_example_data(param1, param2)
    
    # 绘制标题
    draw.text((5, 10), "Template", font=font, fill=1)
    
    # 绘制数据
    small_font = prepare_canvas('vL', font_size=14)[2]
    y_pos = 40
    # 由于宽度较窄，可能需要分行显示
    for line in data.split(','):
        draw.text((5, y_pos), line.strip(), font=small_font, fill=1)
        y_pos += 20
    
    # 绘制尺寸标识
    tiny_font = prepare_canvas('vL', font_size=10)[2]
    draw.text((5, img.height - 20), "vL: 122x250", font=tiny_font, fill=1)
    
    # 绘制边框
    draw.rectangle([0, 0, img.width - 1, img.height - 1], outline=1, width=1)
    
    return finalize_image(img, rotate=rotate, invert=invert)
