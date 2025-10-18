import io
import hashlib
from flask import Blueprint, request, send_file, make_response
from modules.generate_views.random_image import generate_random_image
from modules.errors.errors import ParamError
from config import DEFAULT_IMAGE_QUALITY, RANDOM_VIEW_CACHE_MAX_AGE

bp_random = Blueprint('random_views', __name__)

def _generate_random_etag(routes_param, rotate_arg, invert_arg):
    """生成随机视图的ETag"""
    etag_source = f'{routes_param}:{rotate_arg}:{invert_arg}'
    return hashlib.md5(etag_source.encode()).hexdigest()

def parse_routes_param(param):
    """优化的路由参数解析"""
    if not param:
        raise ParamError('routes参数不能为空')
    
    items = []
    parts = param.split(',')
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
        
        segs = part.split(':')
        if len(segs) < 2:
            continue  # 必须至少有 plugin.kind:size
        
        view_path = segs[0]
        size = segs[1]
        
        # 权重和参数解析
        weight = 1.0
        param_dict = {}
        param_start = 2
        
        if len(segs) > 2:
            # 检查第三个段是否为权重
            if '=' not in segs[2]:
                try:
                    weight = float(segs[2])
                    param_start = 3
                except ValueError:
                    param_start = 2
        
        # 解析参数
        for s in segs[param_start:]:
            if '=' in s:
                k, v = s.split('=', 1)
                param_dict[k] = v
        
        items.append(((view_path, size), weight, param_dict))
    
    # 只保留权重大于0的项
    filtered = [(vc, weight, param_dict) for vc, weight, param_dict in items if weight > 0]
    if not filtered:
        raise ParamError('所有权重均为0或未设置，无法选择视图')
    return filtered

@bp_random.route('/random/views')
def random_views():
    routes_param = request.args.get('routes')
    rotate_arg = request.args.get('rotate', None)
    invert_arg = request.args.get('invert', None)
    
    if not routes_param:
        raise ParamError('缺少 routes 参数')
    
    # 生成ETag用于HTTP缓存
    etag = _generate_random_etag(routes_param, rotate_arg, invert_arg)
    
    # 检查客户端缓存
    if request.headers.get('If-None-Match') == etag:
        response = make_response('', 304)
        response.headers['ETag'] = etag
        return response
    
    rotate_map = {'c': 270, 'cc': 90, 'h': 180}
    global_rotate = rotate_map.get(rotate_arg, 0)
    invert_map = {'t': True, 'f': False}
    global_invert = invert_map.get(invert_arg, False)
    
    choices = parse_routes_param(routes_param)
    view_size_pairs = [vc for vc, _, _ in choices]
    weights = [weight for _, weight, _ in choices]
    params_list = [param_dict for _, _, param_dict in choices]
    try:
        import random
        idx = random.choices(range(len(view_size_pairs)), weights=weights, k=1)[0]
        (view_path, size) = view_size_pairs[idx]
        params = params_list[idx]
        # 单项 rotate/invert 优先
        rotate_val = params.pop('rotate', None)
        rotate = rotate_map.get(rotate_val, global_rotate if rotate_val is None else 0)
        invert_val = params.pop('invert', None)
        invert = (
            invert_map[invert_val] if invert_val in invert_map
            else (global_invert if invert_val is None else False)
        )
        extra_params = params
        img = generate_random_image(view_path, size=size, rotate=rotate, invert=invert, **extra_params)
    except Exception as e:
        raise ParamError(f'随机图片生成失败: {str(e)}')
    buf = io.BytesIO()
    img.save(buf, format='JPEG', quality=DEFAULT_IMAGE_QUALITY, subsampling=0, progressive=False)
    buf.seek(0)
    response = make_response(send_file(buf, mimetype='image/jpeg'))
    response.headers['ETag'] = etag
    response.headers['Cache-Control'] = f'public, max-age={RANDOM_VIEW_CACHE_MAX_AGE}'
    return response