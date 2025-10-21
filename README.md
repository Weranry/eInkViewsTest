# eInkViews

## 项目介绍

**eInkViews** 是一个为 [Open ePaper Link](https://openepaperlink.org) 项目中 `image_url` 功能设计的墨水屏图像信息展示服务，支持插件化扩展。它可灵活适配多种尺寸墨水屏，通过 RESTful API 动态生成图片，也可生成对应的 Json 数据按需调用。

eInkViews 基于 [ePapaer DashBoard](https://github.com/weranry/epaperdashboard) 升级而来，增加了插件化扩展功能，可灵活增减模块，并对图像绘制等代码进行了抽象，专注于信息与图像排版设计，解决了单片机驱动墨水屏信息展示的困难，以及 Open ePaper Link 不支持复杂排版和 Unicode 字符的问题。

---

## 快速开始

### 获取代码

```bash
git clone https://github.com/Weranry/eInkViews.git
cd eInkViews
```

### 安装依赖

```bash
pip install -r requirements.txt
```

### 启动服务

```bash
python app.py
```

### 部署到 Vercel

1. 注册并安装 [Vercel CLI](https://vercel.com/docs/cli)
2. 配置 `vercel.json`
3. 部署：

   ```bash
   vercel --prod
   ```
4. 在 Vercel 环境变量中设置 `api_key`（可选）

---

## 项目结构

```text
/eInkViews/
├── app.py                     # 项目主程序入口
├── config.py                  # 项目配置文件
├── requirements.txt           # 项目依赖
├── vercel.json                # Vercel部署配置
├── public/                    # 静态资源公共目录
│   ├── index.html             # 项目主页
│   └── favicon.ico            # 项目图标
├── modules/                   # 核心功能模块目录
│   ├── auth/                  # 认证
│   │   └── auth.py            # 认证逻辑模块
│   ├── errors/                # 错误处理
│   │   └── errors.py          # 错误处理逻辑模块
│   ├── generate_views/        # 视图生成
│   │   ├── canvas_factory.py  # 画布创建工具
│   │   ├── font_loader.py     # 字体加载工具
│   │   ├── image_transform.py # 图像转换工具
│   │   ├── qrcode_util.py     # 二维码生成工具
│   │   └── random_image.py    # 随机图像生成工具
│   ├── plugins/               # 插件管理模块
│   │   └── plugin_loader.py   # 插件加载逻辑代码
│   └── register/              # 路由注册模块
│       ├── auto_json_routes.py# JSON路由自动注册
│       ├── auto_view_routes.py# 视图路由自动注册
│       └── random_view_route.py# 随机视图路由配置
└── plugins/                   # 插件目录
    ├── __init__.py            # 插件包初始化
    ├── README.md              # 插件使用说明
    ├── view/                  # 视图模块目录
    │   └── views_name/        # 视图名称（可继续扩展）
    │       ├── utils.py       # 视图工具函数（视图规格可按需调整，不必全部使用）
    │       ├── hm.py          # 横向200x200视图
    │       ├── hL.py          # 横向250x122视图
    │       ├── hxl.py         # 横向384x184视图
    │       ├── h2xl.py        # 横向400x300视图
    │       ├── h3xl.py        # 横向600x480视图
    │       ├── h4xl.py        # 横向800x480视图
    │       ├── vm.py          # 纵向200x200视图
    │       ├── vL.py          # 纵向122x250视图
    │       ├── vxl.py         # 纵向184x384视图
    │       ├── v2xl.py        # 纵向300x400视图
    │       ├── v3xl.py        # 纵向480x600视图
    │       └── v4xl.py        # 纵向480x800视图
    ├── json_module/           # JSON数据模块目录
    │   └── data.py            # JSON模块（可继续扩展）
    ├── lib/                   # 业务逻辑库目录
    │   └── data_processor.py  # 数据处理逻辑代码（可继续扩展）
    └── assets/                # 静态资源目录
        └── fonts              # 字体资源及其他静态资源
```

---

## 路由与参数

### Views 视图接口

```
GET /{plugin_name}/view/{view_name}?size={size}&rotate={r}&invert={i}&param=value...
```

- **plugin_name**：插件名称
- **view_name**：插件下的视图名称
- **size**：视图尺寸标识，见下表

#### 横向尺寸

| 标识  | 尺寸（像素） | 方向  |
|-------|-------------|-------|
| hm    | 200x200     | 横向  |
| hL    | 250x122     | 横向  |
| hxl   | 384x184     | 横向  |
| h2xl  | 400x300     | 横向  |
| h3xl  | 600x480     | 横向  |
| h4xl  | 800x480     | 横向  |

#### 纵向尺寸

| 标识  | 尺寸（像素） | 方向  |
|-------|-------------|-------|
| vm    | 200x200     | 纵向  |
| vL    | 122x250     | 纵向  |
| vxl   | 184x384     | 纵向  |
| v2xl  | 300x400     | 纵向  |
| v3xl  | 480x600     | 纵向  |
| v4xl  | 480x800     | 纵向  |

- **参数说明**：
  - `rotate`：旋转角度，支持 `c`(顺时针90°)、`cc`(逆时针90°)、`h`(180°)、`0`(默认)
  - `invert`：反色，`t`(是)、`f`(否)
  - 其他参数：插件自定义

#### 相关配置（config.py）

- `VIEW_CACHE_MAX_AGE`：视图接口图片的 HTTP 缓存时间（秒），默认 300
- `FONT_CACHE_SIZE`：字体对象缓存数量，默认 128

---

### JSON 数据接口

```
GET /{plugin_name}/json/{json_name}?param=value
```

- **plugin_name**：插件名称
- **json_name**：插件中的 JSON 格式名称
- **参数**：由具体模块定义

#### 相关配置（config.py）

- `MODULE_IMPORT_CACHE_SIZE`：JSON模块导入缓存数量，默认 256

---

### Random Views 视图接口

```
GET /random/views?routes={路由描述串}&rotate={r}&invert={i}
```

- **路由描述串**：格式为 `plugin_name.view_name[:size][:weight][:param=value,...]`，多个用逗号分隔
- **参数**：全局旋转或反色参数，单项参数优先

#### 相关配置（config.py）

- `RANDOM_VIEW_CACHE_MAX_AGE`：随机视图接口图片的 HTTP 缓存时间（秒），默认 60
- `MODULE_IMPORT_CACHE_SIZE`：随机视图模块导入缓存数量，默认 256

---

## 插件开发

### 推荐插件结构

```text
plugins/plugins_name/
├── README.md              # 使用文档
├── __init__.py            
├── routes.py              # 路由注册
├── view/                  # 视图模块（可扩展多种排版）
│   └── view_name/
│       ├── utils.py       # 工具函数
│       ├── hm.py          # 200x200
│       ├── hL.py          # 250x122
│       ├── hxl.py         # 384x184
│       ├── h2xl.py        # 400x300
│       ├── h3xl.py        # 600x480
│       ├── h4xl.py        # 800x480
│       ├── vm.py          # 200x200 (竖)
│       ├── vL.py          # 122x250 (竖)
│       ├── vxl.py         # 184x384 (竖)
│       ├── v2xl.py        # 300x400 (竖)
│       ├── v3xl.py        # 480x600 (竖)
│       └── v4xl.py        # 480x800 (竖)
├── json_module/           # JSON数据模块
│   ├── JSON_name.py       # JSON模块
├── lib/                   # 业务逻辑
│   └── data_processor.py  # 数据处理
└── assets/                # 静态资源(字体、图像等)
```

### 开发流程

#### 1. 新建项目

```bash
mkdir plugin_name && cd plugin_name
```

#### 2. 编辑 `routes.py`

插件路由注册文件，负责将插件注册到 Flask 应用中。

```python
from flask import Blueprint
import os
from modules.register.auto_view_routes import register_view_routes
from modules.register.auto_json_routes import register_json_routes

bp = Blueprint('your_plugin_name', __name__)
PLUGIN_NAME = 'your_plugin_name'
VIEW_DIR = os.path.join(os.path.dirname(__file__), 'view')
JSON_MODULE_DIR = os.path.join(os.path.dirname(__file__), 'json_module')

register_view_routes(bp, PLUGIN_NAME, VIEW_DIR)
register_json_routes(bp, PLUGIN_NAME, JSON_MODULE_DIR)
```

- 修改 `PLUGIN_NAME` 为你的插件名称（需与插件目录名一致）
- 确保 `view` 和 `json_module` 目录存在
- 框架会自动扫描并注册所有视图和 JSON 模块

#### 3. 编辑业务逻辑

在 `lib/` 目录下添加你的业务逻辑模块。

#### 4. 自定义视图模块

可在 `view/example/utils.py` 中封装复用代码：

```python
# filepath: plugins/your_plugin_name/view/example/utils.py
from PIL import Image, ImageDraw, ImageFont

FONT_PATHS = {
    'default': 'plugins/your_plugin_name/assets/fonts/custom_font.ttf'
}

def prepare_canvas(size, font_size=32):
    # ...existing code...
    font = ImageFont.truetype(FONT_PATHS['default'], font_size)
    # ...existing code...
    return img, draw, font

def finalize_image(img, rotate=0, invert=False):
    # ...existing code...
    return img
```

编辑 `view/example/*.py`，实现 `generate_image` 函数：

```python
from .utils import prepare_canvas, finalize_image, get_example_data

def generate_image(rotate=0, invert=False, param1='默认值1', param2='默认值2'):
    img, draw, font = prepare_canvas('hm', font_size=24)
    data = get_example_data(param1, param2)
    draw.text((10, 10), "Template", font=font, fill=1)
    small_font = prepare_canvas('hm', font_size=18)[2]
    draw.text((10, 50), data, font=small_font, fill=1)
    tiny_font = prepare_canvas('hm', font_size=14)[2]
    draw.text((10, img.height - 25), "hm: 200x200", font=tiny_font, fill=1)
    draw.rectangle([0, 0, img.width - 1, img.height - 1], outline=1, width=2)
    return finalize_image(img, rotate=rotate, invert=invert)
```

访问路径示例：

```
GET /template/view/example?size=hm&param1=value1&param2=value2&rotate=0&invert=f
```

必需参数：

- `rotate`：旋转角度（'c', 'cc', 'h', 0）
- `invert`：是否反色（True/False, 't'/'f'）

自定义参数：

- `param1`：示例参数1
- `param2`：示例参数2

#### 5. 自定义 JSON 模块（可选）

编辑 `json_module/*.py`，实现 `to_json` 函数：

```python
from flask import jsonify
from plugins.{plugin_name}.lib.{generator} import {}

def to_json(your_param='default'):
    return jsonify({"data": "your data"})
```

#### 6. 静态资源管理

在 `assets/` 目录下统一管理所需资源。可使用项目默认字体资源。

- 字体文件：`.ttf`, `.otf`
- 图像文件：`.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`
- 数据文件：`.json`, `.csv`, `.txt`

---

## config.py 使用说明

用于配置 eInkViews 项目的各项参数，支持性能优化、鉴权、缓存等功能。修改后需重启服务生效。

### 1. 鉴权相关

- `ENABLE_AUTH`: 是否启用鉴权（默认关闭）
- `PLUGIN_WHITELIST`: 跳过鉴权的插件列表

### 2. 默认参数

- `DEFAULT_ROTATE`: 图片默认旋转角度（整数，单位：度）
- `DEFAULT_INVERT`: 是否默认反色（布尔值）
- `DEFAULT_IMAGE_QUALITY`: 图片输出质量（1-100，JPEG）

### 3. 字体缓存

- `ENABLE_FONT_CACHE`: 是否启用字体加载缓存
- `FONT_CACHE_SIZE`: 字体缓存最大数量

### 4. 模块导入缓存

- `ENABLE_MODULE_IMPORT_CACHE`: 是否启用插件模块导入缓存
- `MODULE_IMPORT_CACHE_SIZE`: 模块缓存最大数量

### 5. HTTP 缓存

- `ENABLE_VIEW_CACHE`: 是否启用普通视图的 HTTP 缓存
- `VIEW_CACHE_MAX_AGE`: 普通视图缓存时间（秒）
- `ENABLE_RANDOM_VIEW_CACHE`: 是否启用随机视图的 HTTP 缓存
- `RANDOM_VIEW_CACHE_MAX_AGE`: 随机视图缓存时间（秒）

### 6. 修改建议

- 开发调试时可关闭所有缓存，便于实时查看效果
- 生产环境建议开启字体、模块、HTTP 缓存以提升性能
- 缓存越大内存占用越多，建议根据实际情况调整

### 7. 示例

```python
# 启用所有缓存，适合生产环境
ENABLE_FONT_CACHE = True
ENABLE_MODULE_IMPORT_CACHE = True
ENABLE_VIEW_CACHE = True
ENABLE_RANDOM_VIEW_CACHE = True

# 调整缓存时间
VIEW_CACHE_MAX_AGE = 600  # 10分钟
RANDOM_VIEW_CACHE_MAX_AGE = 120  # 2分钟
```

### 8. 生效方式

修改 `config.py` 后，需重启服务使配置生效。
