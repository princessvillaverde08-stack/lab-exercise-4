from flask import Blueprint, request, jsonify
from collections import deque

deque_bp = Blueprint('deque_bp', __name__)

class BackendDeque:
    def __init__(self):
        self.d = deque()

    def add_front(self, val):
        self.d.appendleft(val)

    def add_rear(self, val):
        self.d.append(val)

    def remove_front(self):
        if not self.d:
            return None
        return self.d.popleft()

    def remove_rear(self):
        if not self.d:
            return None
        return self.d.pop()

dq = BackendDeque()

@deque_bp.route('/api/deque', methods=['POST'])
def api_deque():
    req = request.json or {}
    action = req.get('action')
    val = req.get('value', '').strip()

    message = ""
    if action == 'add_front':
        if val:
            dq.add_front(val)
            message = f'Added Front: "{val}"'
        else:
            message = 'Please enter a value!'
    elif action == 'add_rear':
        if val:
            dq.add_rear(val)
            message = f'Added Rear: "{val}"'
        else:
            message = 'Please enter a value!'
    elif action == 'rem_front':
        removed = dq.remove_front()
        message = f'Removed Front: {removed}' if removed is not None else 'Deque is empty!'
    elif action == 'rem_rear':
        removed = dq.remove_rear()
        message = f'Removed Rear: {removed}' if removed is not None else 'Deque is empty!'

    return jsonify({'message': message, 'nodes': list(dq.d)})