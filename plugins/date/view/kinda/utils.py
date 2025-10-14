from modules.generate_views.canvas_factory import prepare_canvas_with_font, finalize_image_common
from plugins.date.lib.date_generate import get_today

FONT_PATHS = {
    'default': 'static/fonts/font.ttf',
    'bold': 'static/fonts/font_bold.ttf',
    'other': 'static/fonts/other.ttf',
    # 用户可完全自定义
}

def prepare_canvas(kind, font_size=48, font_type='default'):
    return prepare_canvas_with_font(kind, font_size, font_type, font_paths=FONT_PATHS)

def finalize_image(img, rotate=0, invert=False):
    return finalize_image_common(img, rotate=rotate, invert=invert)

def get_date_text(tz=None):
    return get_today(tz=tz)
