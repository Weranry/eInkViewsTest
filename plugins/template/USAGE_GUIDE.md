# 使用模板创建新插件 - Creating a New Plugin from Template

## 快速创建 - Quick Creation

### 步骤 1: 复制模板 - Step 1: Copy Template

```bash
# 在 plugins 目录下复制 template 并重命名为你的插件名
# Copy template in plugins directory and rename to your plugin name
cp -r plugins/template plugins/my_plugin
```

### 步骤 2: 修改插件名称 - Step 2: Modify Plugin Name

编辑 `plugins/my_plugin/routes.py`，修改两处：
Edit `plugins/my_plugin/routes.py`, modify two places:

```python
# 第 13 行 - Line 13
bp = Blueprint('my_plugin', __name__)  # 改为你的插件名

# 第 18 行 - Line 18
PLUGIN_NAME = 'my_plugin'  # 改为你的插件名
```

### 步骤 3: 重命名视图（可选）- Step 3: Rename View (Optional)

如果你想修改视图名称（例如从 `example` 改为 `main`）：
If you want to rename the view (e.g., from `example` to `main`):

```bash
cd plugins/my_plugin/view
mv example main
```

### 步骤 4: 自定义内容 - Step 4: Customize Content

根据需要修改以下文件：
Modify these files as needed:

1. **视图文件** - View Files (`view/example/*.py`)
   - 修改 `generate_image` 函数中的绘图逻辑
   - 添加或删除自定义参数
   - 调整字体大小和布局

2. **JSON 模块** - JSON Modules (`json_module/*.py`)
   - 修改 `to_json` 函数返回的数据
   - 添加新的 JSON 模块文件

3. **业务逻辑** - Business Logic (`lib/*.py`)
   - 在 `data_processor.py` 中添加你的业务逻辑
   - 创建新的工具模块

4. **静态资源** - Static Resources (`assets/`)
   - 添加自定义字体、图片等资源

### 步骤 5: 测试插件 - Step 5: Test Plugin

启动应用并测试：
Start the app and test:

```bash
# 启动应用
python app.py

# 测试视图接口
curl "http://localhost:5000/my_plugin/view/example?size=hm"

# 测试 JSON 接口
curl "http://localhost:5000/my_plugin/json/example"
```

## 示例：创建天气插件 - Example: Creating Weather Plugin

### 1. 复制并重命名 - Copy and Rename

```bash
cp -r plugins/template plugins/weather
```

### 2. 修改 routes.py

```python
bp = Blueprint('weather', __name__)
PLUGIN_NAME = 'weather'
```

### 3. 修改视图文件 - Modify View File

编辑 `plugins/weather/view/example/hm.py`:

```python
from .utils import prepare_canvas, finalize_image
from plugins.weather.lib.weather_api import get_weather

def generate_image(rotate=0, invert=False, city='Beijing'):
    img, draw, font = prepare_canvas('hm', font_size=32)
    
    # 获取天气数据
    weather = get_weather(city)
    
    # 绘制天气信息
    draw.text((10, 10), f"{city}", font=font, fill=1)
    
    small_font = prepare_canvas('hm', font_size=24)[2]
    draw.text((10, 50), f"{weather['temp']}°C", font=small_font, fill=1)
    draw.text((10, 80), weather['desc'], font=small_font, fill=1)
    
    return finalize_image(img, rotate=rotate, invert=invert)
```

### 4. 添加业务逻辑 - Add Business Logic

创建 `plugins/weather/lib/weather_api.py`:

```python
import requests

def get_weather(city):
    # 这里调用真实的天气 API
    # Call real weather API here
    try:
        # 示例 API 调用
        response = requests.get(f'https://api.weather.com/data?city={city}')
        data = response.json()
        return {
            'temp': data.get('temperature', 'N/A'),
            'desc': data.get('description', 'Unknown')
        }
    except:
        return {
            'temp': '25',
            'desc': 'Sunny'
        }
```

### 5. 测试 - Test

```bash
# 启动应用
python app.py

# 访问天气插件
curl "http://localhost:5000/weather/view/example?size=hm&city=Shanghai"
```

## 最佳实践 - Best Practices

### 1. 参数设计 - Parameter Design

```python
def generate_image(
    rotate=0,           # 必需参数，由框架传入
    invert=False,       # 必需参数，由框架传入
    city='Beijing',     # 自定义参数，设置合理默认值
    lang='zh',          # 自定义参数，设置合理默认值
    unit='metric'       # 自定义参数，设置合理默认值
):
    pass
```

### 2. 错误处理 - Error Handling

```python
def generate_image(rotate=0, invert=False, city='Beijing'):
    try:
        img, draw, font = prepare_canvas('hm', font_size=32)
        
        # 可能出错的操作
        data = fetch_data(city)
        
        # 绘制内容
        draw.text((10, 10), data, font=font, fill=1)
        
        return finalize_image(img, rotate=rotate, invert=invert)
    except Exception as e:
        # 返回错误提示图像
        img, draw, font = prepare_canvas('hm', font_size=24)
        draw.text((10, 10), f"Error: {str(e)}", font=font, fill=1)
        return finalize_image(img, rotate=rotate, invert=invert)
```

### 3. 代码复用 - Code Reuse

将通用逻辑放入 `utils.py` 或 `lib/` 目录：

```python
# view/example/utils.py
from plugins.my_plugin.lib.data_processor import process_data

def get_formatted_data(param1, param2):
    """封装通用的数据处理逻辑"""
    raw_data = process_data(param1, param2)
    return f"Data: {raw_data}"
```

### 4. 性能优化 - Performance Optimization

```python
# 缓存字体对象，避免重复创建
_font_cache = {}

def get_cached_font(size):
    if size not in _font_cache:
        _, _, font = prepare_canvas('hm', font_size=size)
        _font_cache[size] = font
    return _font_cache[size]
```

## 常见问题 - Common Issues

### Q1: 插件没有被加载？
**A:** 检查 `routes.py` 中的 `PLUGIN_NAME` 是否与目录名一致。

### Q2: 视图无法访问？
**A:** 确认视图文件名与尺寸标识匹配（如 `hm.py`, `v2xl.py`），且实现了 `generate_image` 函数。

### Q3: 自定义参数无法传递？
**A:** 确保参数名在 `generate_image` 或 `to_json` 函数签名中定义，并设置了默认值。

### Q4: 图像显示异常？
**A:** 检查画布尺寸是否正确，文本位置是否超出边界。

## 进阶功能 - Advanced Features

### 1. 多视图支持 - Multiple Views

```bash
plugins/my_plugin/view/
├── simple/        # 简单视图
│   ├── hm.py
│   └── ...
├── detailed/      # 详细视图
│   ├── hm.py
│   └── ...
└── compact/       # 紧凑视图
    ├── hm.py
    └── ...
```

访问路径：
- `/my_plugin/view/simple?size=hm`
- `/my_plugin/view/detailed?size=hm`
- `/my_plugin/view/compact?size=hm`

### 2. 数据缓存 - Data Caching

```python
# lib/cache.py
import time

_cache = {}
_cache_timeout = 300  # 5 minutes

def cached_fetch(key, fetch_func):
    now = time.time()
    if key in _cache:
        data, timestamp = _cache[key]
        if now - timestamp < _cache_timeout:
            return data
    
    data = fetch_func()
    _cache[key] = (data, now)
    return data
```

### 3. 配置文件支持 - Configuration File

```python
# lib/config.py
import json
import os

def load_config():
    config_path = os.path.join(
        os.path.dirname(__file__), 
        '../assets/config.json'
    )
    with open(config_path, 'r') as f:
        return json.load(f)

CONFIG = load_config()
```

## 更多资源 - More Resources

- 查看 `plugins/date/` 目录了解实际插件示例
- 阅读 `modules/` 目录了解框架提供的工具
- 参考主项目 README 了解完整功能

---

祝你开发顺利！如有问题，欢迎在 GitHub 提 Issue。
Happy coding! Feel free to open an issue on GitHub if you have questions.
