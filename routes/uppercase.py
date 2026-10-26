from flask import Blueprint, request, jsonify

uppercase_bp = Blueprint('uppercase_bp', __name__)

@uppercase_bp.route('/api/uppercase', methods=['POST'])
def api_uppercase():
    data = request.json or {}
    text = data.get('text', '').strip()
    return jsonify({'result': text.upper() if text else '-'})