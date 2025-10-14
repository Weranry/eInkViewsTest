from PIL import Image

def rotate_image(img, angle):
    if angle:
        return img.rotate(angle, expand=True)
    return img

def invert_image(img):
    # 仅适用于RGB/L模式，其他模式需扩展
    return Image.eval(img, lambda x: 255 - x)
