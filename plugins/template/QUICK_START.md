# 插件模板快速开始 - Plugin Template Quick Start

## 一分钟创建插件 - Create Plugin in 1 Minute

### 复制并修改 - Copy and Modify

```bash
# 1. 复制模板
cp -r plugins/template plugins/你的插件名

# 2. 修改插件名
cd plugins/你的插件名
# 编辑 routes.py，将 'template' 改为 '你的插件名'

# 3. 修改视图内容
# 编辑 view/example/hm.py（以及其他尺寸文件）

# 4. 测试
python app.py
# 访问: http://localhost:5000/你的插件名/view/example?size=hm
```

## 完整文件列表 - Complete File List

```
template/
├── README.md              📖 完整使用文档
├── USAGE_GUIDE.md         📘 详细使用指南
├── QUICK_START.md         ⚡ 本文件（快速开始）
├── __init__.py            
├── routes.py              🔧 必须修改：改插件名
│
├── view/                  🎨 视图模块（生成图片）
│   └── example/
│       ├── utils.py       🛠 工具函数
│       ├── hm.py          📱 200x200
│       ├── hL.py          📱 250x122
│       ├── hxl.py         📱 384x184
│       ├── h2xl.py        📱 400x300
│       ├── h3xl.py        📱 600x480
│       ├── h4xl.py        📱 800x480
│       ├── vm.py          📱 200x200 (竖)
│       ├── vL.py          📱 122x250 (竖)
│       ├── vxl.py         📱 184x384 (竖)
│       ├── v2xl.py        📱 300x400 (竖)
│       ├── v3xl.py        📱 480x600 (竖)
│       └── v4xl.py        📱 480x800 (竖)
│
├── json_module/           📊 JSON数据模块
│   ├── example.py         示例JSON
│   └── data.py            数据JSON
│
├── lib/                   💼 业务逻辑
│   └── data_processor.py  数据处理
│
└── assets/                📦 静态资源
    └── README.md          资源说明
```

## 核心API - Core APIs

### 生成图像 - Generate Image

```python
from .utils import prepare_canvas, finalize_image

def generate_image(rotate=0, invert=False, 你的参数='默认值'):
    # 准备画布
    img, draw, font = prepare_canvas('hm', font_size=32)
    
    # 绘制内容
    draw.text((10, 10), "你的内容", font=font, fill=1)
    
    # 返回图像
    return finalize_image(img, rotate=rotate, invert=invert)
```

### 返回JSON - Return JSON

```python
from flask import jsonify

def to_json(你的参数='默认值'):
    return jsonify({
        "status": "success",
        "data": "你的数据"
    })
```

## 测试访问 - Test Access

### 图像接口 - Image API
```
http://localhost:5000/插件名/view/example?size=hm&参数=值
```

### JSON接口 - JSON API
```
http://localhost:5000/插件名/json/example?参数=值
```

## 支持的尺寸 - Supported Sizes

| 标识 | 尺寸      | 方向 |
|------|-----------|------|
| hm   | 200x200   | 横   |
| hL   | 250x122   | 横   |
| hxl  | 384x184   | 横   |
| h2xl | 400x300   | 横   |
| h3xl | 600x480   | 横   |
| h4xl | 800x480   | 横   |
| vm   | 200x200   | 竖   |
| vL   | 122x250   | 竖   |
| vxl  | 184x384   | 竖   |
| v2xl | 300x400   | 竖   |
| v3xl | 480x600   | 竖   |
| v4xl | 480x800   | 竖   |

## 实用示例 - Practical Examples

### 示例1: 显示文本 - Display Text
```python
def generate_image(rotate=0, invert=False, text='Hello'):
    img, draw, font = prepare_canvas('hm', font_size=32)
    draw.text((10, 10), text, font=font, fill=1)
    return finalize_image(img, rotate=rotate, invert=invert)
```

### 示例2: 显示时间 - Display Time
```python
from datetime import datetime

def generate_image(rotate=0, invert=False):
    img, draw, font = prepare_canvas('hm', font_size=28)
    now = datetime.now().strftime("%H:%M:%S")
    draw.text((10, 10), now, font=font, fill=1)
    return finalize_image(img, rotate=rotate, invert=invert)
```

### 示例3: 显示天气 - Display Weather
```python
from plugins.template.lib.data_processor import fetch_data_from_api

def generate_image(rotate=0, invert=False, city='北京'):
    img, draw, font = prepare_canvas('hm', font_size=24)
    
    # 获取天气（示例）
    # weather = fetch_data_from_api(f'https://api.weather.com?city={city}')
    
    draw.text((10, 10), f"{city}天气", font=font, fill=1)
    draw.text((10, 40), "晴 25°C", font=font, fill=1)
    
    return finalize_image(img, rotate=rotate, invert=invert)
```

### 示例4: 添加二维码 - Add QR Code
```python
from modules.generate_views.qrcode_util import generate_qrcode

def generate_image(rotate=0, invert=False, url='https://github.com'):
    img, draw, font = prepare_canvas('hm', font_size=24)
    
    # 绘制文本
    draw.text((10, 10), "扫码访问", font=font, fill=1)
    
    # 生成二维码
    qr = generate_qrcode(url, box_size=3)
    qr = qr.convert('P')
    
    # 粘贴二维码
    x = img.width - qr.width - 10
    y = img.height - qr.height - 10
    img.paste(qr, (x, y))
    
    return finalize_image(img, rotate=rotate, invert=invert)
```

## 需要帮助？ - Need Help?

- 📖 查看 README.md 了解完整功能
- 📘 查看 USAGE_GUIDE.md 了解详细用法
- 🔍 查看 plugins/date/ 了解实际案例
- 💬 在 GitHub 提 Issue 获取支持

---

🎉 开始创建你的第一个插件吧！
