from flask import Blueprint, request, jsonify
import math

circle_bp = Blueprint('circle_bp', __name__)

@circle_bp.route('/api/circle', methods=['POST'])
def api_circle():
    data = request.json or {}
    try:
        r = float(data.get('radius', 0))
        if r > 0:
            area = math.pi * (r ** 2)
            return jsonify({'area': f"{area:.2f} sq. units", 'valid': True, 'radius': r})
    except ValueError:
        pass
    return jsonify({'area': 'Please enter valid radius!', 'valid': False, 'radius': 0})