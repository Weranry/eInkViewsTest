from PIL import Image, ImageDraw

from modules.generate_views.font_loader import load_font
from modules.generate_views.image_transform import rotate_image, invert_image

SIZES = {
    'hm': (200, 200),
    'hL': (250, 122),
    'hxl': (384, 184),
    'h2xl': (400, 300),
    'h3xl': (600, 480),
    'h4xl': (800, 480),
    'vm': (200, 200),
    'vL': (122, 250),
    'vxl': (184, 384),
    'v2xl': (300, 400),
    'v3xl': (480, 600),
    'v4xl': (480, 800)
}
PALETTE = [255, 255, 255, 0, 0, 0, 255, 0, 0] + [0] * 249 * 3  # 白、黑、红，后续填充为0


def create_canvas(mode, size_key):
    if mode not in ('P', 'RGB'):
        raise ValueError(f'不支持的图像模式: {mode}')
    size = SIZES.get(size_key)
    if not size:
        raise ValueError(f'未知尺寸: {size_key}')
    img = Image.new(mode, size)
    if mode == 'P':
        img.putpalette(PALETTE)
    return img


def prepare_canvas_with_font(kind, font_size=48, font_type='default', font_paths=None):
    img = create_canvas('P', kind)
    draw = ImageDraw.Draw(img)
    if not font_paths or font_type not in font_paths:
        raise ValueError("必须在 font_paths 中指定所需字体类型的路径")
    font_path = font_paths[font_type]
    font = load_font(font_size, font_path=font_path)
    return img, draw, font


def finalize_image_common(img, rotate=0, invert=False):
    rgb_img = img.convert('RGB')
    rgb_img = rotate_image(rgb_img, rotate)
    if invert:
        rgb_img = invert_image(rgb_img)
    return rgb_img
