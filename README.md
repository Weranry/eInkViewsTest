# eInkViews

**eInkViews** 是一个为[Open ePaper Link](https://openepaperlink.org)项目中image_url功能设计的墨水屏图像信息展示服务，支持插件化扩展。它可以灵活适配多种尺寸的墨水屏，可通过 RESTful API 动态生成图片,也可生成对应的 Json 数据可按需调用。

本项目基于另一个墨水屏图像信息展示服务[ePapaer DashBoard](https://github.com/weranry/epaperdashboard)升级而来，与其相比增加了插件化扩展功能，可以按需灵活增减模块，另外对图像绘制等代码进行了封装，可以专注于信息与图像排版设计，解决了使用单片机驱动墨水屏并进行信息展示的困难和 Open ePaper Link 中不支持复杂排版和 Unicode 字符的问题。

---

## 快速开始

### 获取代码

```bash
git clone https://github.com/Weranry/eInkViews.git
cd eInkViews
```

### 本地运行

#### 安装依赖（建议 Python 3.9+）：

   ```bash
   pip install -r requirements.txt
   ```

#### 启动服务：

   ```bash
   python app.py
   ```

#### 访问主页：  

   http://localhost:5000

### 部署到 Vercel ：

1. 注册并安装 [Vercel CLI](https://vercel.com/docs/cli)。
2. 配置 `vercel.json`（已提供）。
3. 部署：

   ```bash
   vercel --prod
   ```
4. 在 Vercel 的环境变量中设置 api_key （可选）
---

## 项目结构与依赖

### 目录说明

- `app.py`                主入口
- `public/`               前端静态页面
- `plugins/`              插件目录
- `modules/`              公共模块（画布、字体、路由注册等）
- `config.py`             全局配置
- `requirements.txt`      Python 依赖
- `vercel.json`           Vercel 部署配置

### 依赖说明

- **Flask**           Web 框架
- **Pillow**          图片处理
- **requests**        网络请求（部分插件用）
- **pytz**            时区支持
- **beautifulsoup4**  网页解析（部分插件用）
- **qrcode**          二维码生成

### 已封装模块

- 绘图模块
- 网络爬虫模块
- 二维码生成模块

## 路由与参数

### Views 视图接口

```
GET /{plugin_name}/view/{view_name}?size={size}&rotate={r}&invert={i}&参数...
```
- **plugin_name**：插件名称
- **view_name**：一个插件下可能存在多种不同的视图，可按需选择
- **size**：相同的视图可能存在不同的大小和方向，根据常见的墨水屏尺寸，定义见下表：

|标识|尺寸（像素）|方向|
|---|---|---|
|hm|200x200|横向|
|hL|250x122|横向|
|hxl|384x184|横向|
|h2xl|400x300|横向|
|h3xl|600x480|横向|
|h4xl|800x480|横向|

|标识|尺寸（像素）|方向|
|---|---|---|
|vm|200x200|纵向|
|vL|122x250|纵向|
|vxl|184x384|纵向|
|v2xl|300x400|纵向|
|v3xl|480x600|纵向|
|v4xl|480x800|纵向|

- **参数**：
  - `rotate`：旋转角度，支持 `c`(顺时针90°)、`cc`(逆时针90°)、`h`(180°)、`0`(默认)
  - `invert`：反色，`t`(是)、`f`(否)
  - 其他参数：插件自定义


### JSON 数据接口

```
GET /{plugin_name}/json/{json_name}?参数=值
```

- **plugin_name**：插件名称
- **json_name**：一个插件中可能存在多种不同的 json 格式，按需调用。

- **参数**：由具体模块定义


### Random Views 视图接口

```
GET /random/views?routes={路由描述串}&rotate={r}&invert={i}
```

- **路由描述串**：格式为 `plugin_name.view_name[:size][:weight][:其他参数=值,...]`，存在多个用逗号分隔

- **参数**：全局旋转或反色参数，当与单项视图描述串中同时存在时，可覆盖全局参数，以单项参数为准。

---

## 插件开发

### 插件目录

每个插件位于 `plugins/{插件名}`，推荐结构如下：

```
plugins/
  └── date/
      ├── routes.py         # 路由注册
      ├── view/             # 图片视图
      │   └── view_name/
      │       ├── hm.py
      │       ├── hL.py
      │       └── ...
      ├── json_module/      # JSON 数据模块
      │   ├── A.py
      │   ├── B.py
      │   └── ...
      ├── lib/              # 业务逻辑/工具
      └── assets/           # 静态资源(例如自定义字体或者图像素材)
```

---

### 插件开发详细步骤

#### 1. 新建插件目录

以 `weather` 插件为例：

```bash
mkdir -p plugins/weather/view/simple
mkdir -p plugins/weather/json_module
mkdir -p plugins/weather/lib
mkdir -p plugins/weather/assets
touch plugins/weather/routes.py
```

#### 2. 编写视图模块

每个视图对应一个 Python 文件，必须实现 `generate_image` 函数。

**模板：**

```python
# filepath: plugins/weather/view/simple/hm.py
from .utils import prepare_canvas, finalize_image

def generate_image(rotate=0, invert=False, city='Beijing'):
    img, draw, font = prepare_canvas('hm', font_size=48)
    # 业务逻辑：绘制天气信息
    draw.text((10, 10), f"Weather: {city}", font=font, fill=1)
    return finalize_image(img, rotate=rotate, invert=invert)
```

**注意事项：**
- `generate_image` 必须接收 `rotate` 和 `invert` 参数（由框架自动传入）。
- 其他参数（如 `city`）可自定义，前端通过 URL 参数传递。
- 推荐通过 `prepare_canvas` 获取画布、画笔和字体。

#### 3. 编写工具模块（可选）

如需复用代码，可在 `view/simple/utils.py` 中封装：

```python
# filepath: plugins/weather/view/simple/utils.py
from modules.generate_views.canvas_factory import prepare_canvas_with_font, finalize_image_common

FONT_PATHS = {
    'default': 'static/fonts/font.ttf',
}

def prepare_canvas(kind, font_size=48, font_type='default'):
    return prepare_canvas_with_font(kind, font_size, font_type, font_paths=FONT_PATHS)

def finalize_image(img, rotate=0, invert=False):
    return finalize_image_common(img, rotate=rotate, invert=invert)
```

#### 4. 编写 JSON 数据模块（可选）

每个 JSON 数据模块需实现 `to_json` 函数，参数自定义。

**模板：**

```python
# filepath: plugins/weather/json_module/now.py
from flask import jsonify

def to_json(city='Beijing'):
    # 业务逻辑：获取天气数据
    return jsonify({"city": city, "weather": "Sunny"})
```

#### 5. 注册路由

在 `routes.py` 中注册视图和 JSON 路由：

```python
# filepath: plugins/weather/routes.py
from flask import Blueprint
import os
from modules.register.auto_view_routes import register_view_routes
from modules.register.auto_json_routes import register_json_routes

bp = Blueprint('weather', __name__)

PLUGIN_NAME = 'weather'
VIEW_DIR = os.path.join(os.path.dirname(__file__), 'view')
JSON_MODULE_DIR = os.path.join(os.path.dirname(__file__), 'json_module')

register_view_routes(bp, PLUGIN_NAME, VIEW_DIR)
register_json_routes(bp, PLUGIN_NAME, JSON_MODULE_DIR)
```

#### 6. 使用自定义参数

- 视图接口：所有非保留参数（`size`、`rotate`、`invert`）会自动传递给 `generate_image`。
- JSON 接口：参数名需与 `to_json` 函数参数一致，类型自动转换（支持 int/float/bool/str）。

**示例：**

```
GET /weather/view/simple?size=hm&city=Shanghai
GET /weather/json/now?city=Shanghai
```

#### 7. 引入自定义字体/素材

将字体文件放入 `plugins/weather/assets/` 或 `static/fonts/`，在 `FONT_PATHS` 中配置路径。

---

### 插件开发注意事项

- 每个插件必须有 `routes.py` 并注册到 Blueprint。
- 视图和 JSON 模块文件名不能重复，且需实现指定函数。
- 推荐所有参数均设置默认值，避免缺参报错。
- 插件目录结构可根据实际需求扩展，但建议遵循上述规范。

---

