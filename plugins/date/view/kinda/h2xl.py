from .utils import prepare_canvas, finalize_image, get_date_text

def generate_image(rotate=0, invert=False, tz=None):
    img, draw, font = prepare_canvas('h2xl', font_size=48)
    date_text = get_date_text(tz=tz)
    draw.text((10, 10), date_text, font=font, fill=1)
    return finalize_image(img, rotate=rotate, invert=invert)