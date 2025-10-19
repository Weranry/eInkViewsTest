"""
横向L尺寸视图 - Horizontal Large Size View
尺寸 - Size: 250x122 像素 (pixels)
方向 - Orientation: 横向 (Horizontal)

访问路径 - Access Path:
GET /template/view/example?size=hL&param1=value1&param2=value2
"""

from .utils import prepare_canvas, finalize_image, get_example_data

def generate_image(rotate=0, invert=False, param1='默认值1', param2='默认值2'):
    """生成 hL 尺寸图像 - Generate hL size image"""
    
    # 准备画布 - Prepare canvas
    img, draw, font = prepare_canvas('hL', font_size=20)
    
    # 获取数据 - Get data
    data = get_example_data(param1, param2)
    
    # 绘制内容 - Draw content
    draw.text((10, 10), "Template Plugin", font=font, fill=1)
    
    small_font = prepare_canvas('hL', font_size=16)[2]
    draw.text((10, 40), data, font=small_font, fill=1)
    
    # 绘制尺寸标识 - Draw size identifier
    tiny_font = prepare_canvas('hL', font_size=12)[2]
    draw.text((10, img.height - 20), "hL: 250x122", font=tiny_font, fill=1)
    
    # 绘制边框 - Draw border
    draw.rectangle([0, 0, img.width - 1, img.height - 1], outline=1, width=1)
    
    return finalize_image(img, rotate=rotate, invert=invert)
