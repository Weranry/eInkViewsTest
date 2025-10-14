from PIL import ImageFont
import os

def load_font(size, font_path):
    # font_path 必须由用户指定（相对根目录或绝对路径）
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    abs_font_path = os.path.join(project_root, font_path) if not os.path.isabs(font_path) else font_path
    try:
        return ImageFont.truetype(abs_font_path, size)
    except OSError as e:
        print(f"警告: 字体文件 {abs_font_path} 加载失败，错误信息: {e}")
        return ImageFont.load_default()
