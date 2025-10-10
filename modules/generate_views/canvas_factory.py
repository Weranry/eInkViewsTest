from PIL import Image

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
PALETTE = [255,255,255, 0,0,0, 255,0,0] + [0]*249*3  # 白、黑、红


def create_canvas(mode, size_key):
    size = SIZES.get(size_key)
    if not size:
        raise ValueError(f'未知尺寸: {size_key}')
    img = Image.new(mode, size)
    if mode == 'P':
        img.putpalette(PALETTE)
    return img
