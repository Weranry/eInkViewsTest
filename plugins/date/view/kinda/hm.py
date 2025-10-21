from .utils import prepare_canvas, finalize_image, get_date_text
from modules.generate_views.qrcode_util import generate_qrcode

CACHE_MAX_AGE = 100  # 单独设置本视图缓存时间为 100 秒

def generate_image(rotate=0, invert=False, tz=None):
    img, draw, font = prepare_canvas('hm', font_size=48)
    date_text = get_date_text(tz=tz)
    draw.text((10, 10), date_text, font=font, fill=1)
    # 生成第一个二维码
    qr_img1 = generate_qrcode('https://openepaperlink.org', box_size=3)
    qr_img1 = qr_img1.convert('P')
    x1 = img.width - qr_img1.width - 10
    y1 = img.height - qr_img1.height - 10
    img.paste(qr_img1, (x1, y1))
    return finalize_image(img, rotate=rotate, invert=invert)