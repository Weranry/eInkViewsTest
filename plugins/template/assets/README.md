# Assets 目录说明 - Assets Directory Guide

这个目录用于存放插件的静态资源文件。
This directory is used to store static resource files for the plugin.

## 支持的资源类型 - Supported Resource Types

### 1. 字体文件 - Font Files
- **格式**: `.ttf`, `.otf`
- **用途**: 自定义字体显示
- **示例**: `custom_font.ttf`
- **使用方法**:
  ```python
  # 在 view/example/utils.py 的 FONT_PATHS 中配置
  FONT_PATHS = {
      'custom': 'plugins/template/assets/custom_font.ttf',
  }
  ```

### 2. 图像文件 - Image Files
- **格式**: `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`
- **用途**: 图标、Logo、背景图等
- **示例**: `logo.png`, `icon.png`
- **使用方法**:
  ```python
  from PIL import Image
  import os
  
  # 在视图模块中加载图像
  assets_dir = os.path.join(os.path.dirname(__file__), '../../assets')
  logo_path = os.path.join(assets_dir, 'logo.png')
  logo = Image.open(logo_path)
  img.paste(logo, (x, y))
  ```

### 3. 数据文件 - Data Files
- **格式**: `.json`, `.csv`, `.txt`
- **用途**: 配置数据、静态数据等
- **示例**: `config.json`, `data.csv`
- **使用方法**:
  ```python
  import json
  import os
  
  # 在 lib 模块中加载数据
  assets_dir = os.path.join(os.path.dirname(__file__), '../assets')
  config_path = os.path.join(assets_dir, 'config.json')
  with open(config_path, 'r', encoding='utf-8') as f:
      config = json.load(f)
  ```

## 使用建议 - Usage Recommendations

1. **文件命名**: 使用有意义的英文名称，避免中文和特殊字符
   **File Naming**: Use meaningful English names, avoid Chinese and special characters

2. **文件大小**: 尽量控制资源文件大小，特别是图像文件
   **File Size**: Try to control the size of resource files, especially image files

3. **版权注意**: 确保使用的资源文件有合法的使用权限
   **Copyright**: Ensure that the resource files used have legal usage rights

4. **路径引用**: 使用相对路径或 `os.path.join()` 构建路径
   **Path Reference**: Use relative paths or `os.path.join()` to build paths

## 示例文件结构 - Example File Structure

```
assets/
├── fonts/
│   ├── custom_font.ttf
│   └── bold_font.ttf
├── images/
│   ├── logo.png
│   ├── icon.png
│   └── background.png
├── data/
│   ├── config.json
│   └── static_data.csv
└── README.md
```

## 注意事项 - Notes

- 不要在 assets 目录中存放敏感信息（如 API 密钥）
  Do not store sensitive information (such as API keys) in the assets directory

- 建议将大型资源文件添加到 `.gitignore` 中
  It is recommended to add large resource files to `.gitignore`

- 如果需要动态下载资源，请在 lib 模块中实现
  If you need to download resources dynamically, implement it in the lib module
