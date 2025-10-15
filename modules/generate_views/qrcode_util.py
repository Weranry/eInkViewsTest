import qrcode
from PIL import Image

def generate_qrcode(data, box_size=10, border=2, fill_color=0, back_color=255):
    """
    生成二维码图片（PIL.Image对象，单通道L模式，黑白）
    :param data: 二维码内容
    :param box_size: 每个点的像素大小
    :param border: 边框宽度（点数）
    :param fill_color: 前景色（0=黑，255=白）
    :param back_color: 背景色（0=黑，255=白）
    :return: PIL.Image
    """
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    # 转为L模式，方便paste到P模式画布
    if img.mode != 'L':
        img = img.convert('L')
    return img
