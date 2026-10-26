from flask import Blueprint, request, jsonify

triangle_bp = Blueprint('triangle_bp', __name__)

@triangle_bp.route('/api/triangle', methods=['POST'])
def api_triangle():
    data = request.json or {}
    try:
        b = float(data.get('base', 0))
        h = float(data.get('height', 0))
        if b > 0 and h > 0:
            area = 0.5 * b * h
            return jsonify({'area': f"{area:.2f} sq. units", 'valid': True, 'base': b, 'height': h})
    except ValueError:
        pass
    return jsonify({'area': 'Enter valid Base & Height!', 'valid': False, 'base': 0, 'height': 0})