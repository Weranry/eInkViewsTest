from flask import jsonify
from plugins.date.lib.date_generate import get_today

def to_json(tz=None):
    return jsonify({"date": get_today(tz=tz)})
