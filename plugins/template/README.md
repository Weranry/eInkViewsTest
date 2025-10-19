# Template Plugin - 插件模板

这是一个完整的 eInkViews 插件模板，包含了所有必要的组件和详细的示例代码。
This is a complete eInkViews plugin template with all necessary components and detailed example code.

## 目录结构 - Directory Structure

```
template/
├── __init__.py              # 插件初始化文件
├── routes.py                # 路由注册（必需）
├── README.md                # 插件说明文档
├── view/                    # 视图模块目录
│   ├── __init__.py
│   └── example/             # 视图名称（可有多个）
│       ├── __init__.py
│       ├── utils.py         # 工具函数
│       ├── hm.py            # 横向中等尺寸 (200x200)
│       ├── hL.py            # 横向大尺寸 (250x122)
│       ├── hxl.py           # 横向超大尺寸 (384x184)
│       ├── h2xl.py          # 横向2XL尺寸 (400x300)
│       ├── h3xl.py          # 横向3XL尺寸 (600x480)
│       ├── h4xl.py          # 横向4XL尺寸 (800x480)
│       ├── vm.py            # 纵向中等尺寸 (200x200)
│       ├── vL.py            # 纵向大尺寸 (122x250)
│       ├── vxl.py           # 纵向超大尺寸 (184x384)
│       ├── v2xl.py          # 纵向2XL尺寸 (300x400)
│       ├── v3xl.py          # 纵向3XL尺寸 (480x600)
│       └── v4xl.py          # 纵向4XL尺寸 (480x800)
├── json_module/             # JSON 数据模块目录
│   ├── __init__.py
│   ├── example.py           # 示例 JSON 模块
│   └── data.py              # 数据 JSON 模块
├── lib/                     # 业务逻辑库
│   ├── __init__.py
│   └── data_processor.py    # 数据处理模块
└── assets/                  # 静态资源目录
    └── README.md            # 资源说明
```

## 快速开始 - Quick Start

### 1. 复制模板创建新插件 - Copy Template to Create New Plugin

```bash
# 复制整个 template 目录并重命名为你的插件名
cp -r plugins/template plugins/your_plugin_name
```

### 2. 修改插件配置 - Modify Plugin Configuration

编辑 `plugins/your_plugin_name/routes.py`:

```python
# 修改这两行
bp = Blueprint('your_plugin_name', __name__)
PLUGIN_NAME = 'your_plugin_name'
```

### 3. 自定义视图 - Customize Views

编辑 `plugins/your_plugin_name/view/example/` 目录下的文件，或创建新的视图目录。

每个视图文件必须实现 `generate_image` 函数：

```python
def generate_image(rotate=0, invert=False, your_param='default'):
    # 你的视图逻辑
    pass
```

### 4. 自定义 JSON 模块 - Customize JSON Modules

编辑 `plugins/your_plugin_name/json_module/` 目录下的文件。

每个 JSON 文件必须实现 `to_json` 函数：

```python
def to_json(your_param='default'):
    return jsonify({"data": "your data"})
```

### 5. 添加业务逻辑 - Add Business Logic

在 `plugins/your_plugin_name/lib/` 目录下添加你的业务逻辑模块。

## 访问路径 - Access Paths

### 视图接口 - View Endpoints

```
GET /template/view/example?size=hm&param1=value1&param2=value2&rotate=0&invert=f
```

参数说明 - Parameter Description:
- `size`: 必需，画布尺寸 (hm, hL, hxl, h2xl, h3xl, h4xl, vm, vL, vxl, v2xl, v3xl, v4xl)
- `rotate`: 旋转角度 ('c'=顺时针90°, 'cc'=逆时针90°, 'h'=180°, 0=不旋转)
- `invert`: 反色 ('t'=True, 'f'=False)
- `param1`, `param2`: 自定义参数

### JSON 接口 - JSON Endpoints

```
GET /template/json/example?param1=value1&param2=value2
GET /template/json/data?key=value
```

## 支持的画布尺寸 - Supported Canvas Sizes

### 横向 - Horizontal
| 标识 | 尺寸 (像素) | 文件名 |
|------|-------------|--------|
| hm   | 200x200     | hm.py  |
| hL   | 250x122     | hL.py  |
| hxl  | 384x184     | hxl.py |
| h2xl | 400x300     | h2xl.py|
| h3xl | 600x480     | h3xl.py|
| h4xl | 800x480     | h4xl.py|

### 纵向 - Vertical
| 标识 | 尺寸 (像素) | 文件名 |
|------|-------------|--------|
| vm   | 200x200     | vm.py  |
| vL   | 122x250     | vL.py  |
| vxl  | 184x384     | vxl.py |
| v2xl | 300x400     | v2xl.py|
| v3xl | 480x600     | v3xl.py|
| v4xl | 480x800     | v4xl.py|

## 核心 API - Core API

### 画布和字体 - Canvas and Font

```python
from .utils import prepare_canvas, finalize_image

# 准备画布
img, draw, font = prepare_canvas('hm', font_size=48, font_type='default')

# 绘制文本
draw.text((x, y), "文本内容", font=font, fill=1)

# 完成图像处理
return finalize_image(img, rotate=rotate, invert=invert)
```

### 二维码生成 - QR Code Generation

```python
from modules.generate_views.qrcode_util import generate_qrcode

# 生成二维码
qr_img = generate_qrcode('https://example.com', box_size=3)
qr_img = qr_img.convert('P')
img.paste(qr_img, (x, y))
```

### 网络请求 - Network Requests

```python
from modules.network.http_client import get_json, get_text

# GET JSON 数据
data = get_json('https://api.example.com/data')

# GET 文本数据
text = get_text('https://example.com/page')
```

## 开发建议 - Development Tips

1. **参数默认值**: 所有自定义参数都应该设置默认值
   **Parameter Defaults**: All custom parameters should have default values

2. **错误处理**: 添加适当的异常处理，避免程序崩溃
   **Error Handling**: Add appropriate exception handling to avoid crashes

3. **字体大小**: 根据画布尺寸选择合适的字体大小
   **Font Size**: Choose appropriate font size based on canvas size

4. **测试**: 在实际部署前测试所有尺寸的视图
   **Testing**: Test all size views before deployment

5. **文档**: 为自定义参数添加清晰的注释
   **Documentation**: Add clear comments for custom parameters

## 示例代码 - Example Code

### 基础视图 - Basic View

```python
from .utils import prepare_canvas, finalize_image

def generate_image(rotate=0, invert=False, text='Hello'):
    img, draw, font = prepare_canvas('hm', font_size=32)
    draw.text((10, 10), text, font=font, fill=1)
    return finalize_image(img, rotate=rotate, invert=invert)
```

### 带数据处理的视图 - View with Data Processing

```python
from .utils import prepare_canvas, finalize_image
from plugins.template.lib.data_processor import process_data

def generate_image(rotate=0, invert=False, param1='A', param2='B'):
    img, draw, font = prepare_canvas('hm', font_size=28)
    
    # 处理数据
    result = process_data(param1, param2)
    
    # 绘制结果
    draw.text((10, 10), result, font=font, fill=1)
    
    return finalize_image(img, rotate=rotate, invert=invert)
```

### JSON 数据模块 - JSON Data Module

```python
from flask import jsonify
from plugins.template.lib.data_processor import fetch_data_from_api

def to_json(city='Beijing'):
    # 获取数据
    data = fetch_data_from_api(f'https://api.example.com/weather?city={city}')
    
    # 返回 JSON
    return jsonify({
        "status": "success",
        "data": data
    })
```

## 常见问题 - FAQ

### Q: 如何添加新的视图尺寸？
**A:** 在 `view/example/` 目录下创建新的 `.py` 文件，文件名对应尺寸标识（如 `hm.py`），实现 `generate_image` 函数。

### Q: 如何使用自定义字体？
**A:** 将字体文件放入 `assets/` 目录，在 `view/example/utils.py` 的 `FONT_PATHS` 中添加配置。

### Q: 如何调用外部 API？
**A:** 使用 `modules.network.http_client` 或标准的 `requests` 库，建议在 `lib/` 目录下封装 API 调用逻辑。

### Q: 如何处理参数类型转换？
**A:** 框架会自动处理基本类型（int, float, bool, str）的转换，复杂类型需要在函数内部手动处理。

## 更多资源 - More Resources

- [eInkViews 项目主页](https://github.com/Weranry/eInkViews)
- [Open ePaper Link](https://openepaperlink.org)
- [Pillow 文档](https://pillow.readthedocs.io/)
- [Flask 文档](https://flask.palletsprojects.com/)

## 许可证 - License

本模板遵循与 eInkViews 项目相同的许可证。
This template follows the same license as the eInkViews project.

---

**祝你开发愉快！ Happy Coding!** 🎉
