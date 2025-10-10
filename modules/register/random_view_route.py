import io
from flask import Blueprint, request, send_file
from modules.generate_views.random_image import generate_random_image
from modules.errors.errors import ParamError
from config import DEFAULT_IMAGE_QUALITY

bp_random = Blueprint('random_views', __name__)

def parse_routes_param(param):
    items = []
    for part in param.split(','):
        part = part.strip()
        if not part:
            continue
        segs = part.split(':')
        if len(segs) < 2:
            continue  # 必须至少有 plugin.kind:code
        view_path = segs[0]
        code = segs[1]
        # 权重
        if len(segs) > 2 and '=' not in segs[2]:
            try:
                weight = float(segs[2])
                param_start = 3
            except ValueError:
                weight = 1.0
                param_start = 2
        else:
            weight = 1.0
            param_start = 2
        # 解析参数
        param_dict = {}
        for s in segs[param_start:]:
            if '=' in s:
                k, v = s.split('=', 1)
                param_dict[k] = v
        items.append(((view_path, code), weight, param_dict))
    # 只保留权重大于0的项
    filtered = [(vc, weight, param_dict) for vc, weight, param_dict in items if weight > 0]
    if not filtered:
        raise ParamError('所有权重均为0或未设置，无法选择视图')
    return filtered

@bp_random.route('/random/views')
def random_views():
    routes_param = request.args.get('routes')
    global_rotate = int(request.args.get('rotate', 0))
    global_invert = bool(int(request.args.get('invert', 0)))
    if not routes_param:
        raise ParamError('缺少 routes 参数')
    choices = parse_routes_param(routes_param)
    view_code_pairs = [vc for vc, _, _ in choices]
    weights = [weight for _, weight, _ in choices]
    params_list = [param_dict for _, _, param_dict in choices]
    try:
        import random
        idx = random.choices(range(len(view_code_pairs)), weights=weights, k=1)[0]
        (view_path, code) = view_code_pairs[idx]
        params = params_list[idx]
        rotate = int(params.pop('rotate', global_rotate))
        invert = bool(int(params.pop('invert', int(global_invert))))
        extra_params = params
        img = generate_random_image(view_path, code=code, rotate=rotate, invert=invert, **extra_params)
    except Exception as e:
        raise ParamError(f'随机图片生成失败: {str(e)}')
    buf = io.BytesIO()
    img.save(buf, format='JPEG', quality=DEFAULT_IMAGE_QUALITY, subsampling=0, progressive=False)
    buf.seek(0)
    return send_file(buf, mimetype='image/jpeg')