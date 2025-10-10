from PIL import ImageFont

def load_font(font_path, size):
    try:
        return ImageFont.truetype(font_path, size)
    except OSError:
        return ImageFont.load_default()
