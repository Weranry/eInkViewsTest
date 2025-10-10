import os
from PIL import ImageDraw
from modules.generate_views.canvas_factory import create_canvas
from modules.generate_views.font_loader import load_font
from modules.generate_views.image_transform import rotate_image, invert_image
from plugins.date.lib.date_generate import get_today

FONT_PATH = os.path.join(os.path.dirname(__file__), '../static/fonts/font.ttf')

def prepare_canvas(kind, font_size=48):
    img = create_canvas('P', kind)
    draw = ImageDraw.Draw(img)
    font = load_font(FONT_PATH, font_size)
    return img, draw, font

def finalize_image(img, rotate=0, invert=False):
    rgb_img = img.convert('RGB')
    if invert:
        rgb_img = invert_image(rgb_img)
    rgb_img = rotate_image(rgb_img, rotate)
    return rgb_img

def get_date_text(tz=None):
    return get_today(tz=tz)
