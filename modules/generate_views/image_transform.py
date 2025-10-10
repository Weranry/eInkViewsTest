from PIL import Image

def rotate_image(img, angle):
    if angle:
        return img.rotate(angle, expand=True)
    return img

def invert_image(img):
    return Image.eval(img, lambda x: 255 - x)
