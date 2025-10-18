from PIL import Image

def rotate_image(img, angle):
    """优化的图像旋转，只在需要时执行"""
    if angle and angle != 0:
        return img.rotate(angle, expand=True)
    return img

def invert_image(img):
    """优化的图像反色，使用更快的point方法"""
    # 使用point方法比eval更快
    return img.point(lambda x: 255 - x)
