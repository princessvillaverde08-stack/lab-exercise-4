from flask import Blueprint, request, jsonify

queue_bp = Blueprint('queue_bp', __name__)

class BackendQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)

q = BackendQueue()

@queue_bp.route('/api/queue', methods=['POST'])
def api_queue():
    req = request.json or {}
    action = req.get('action')
    val = req.get('value', '').strip()

    message = ""
    if action == 'enqueue':
        if val:
            q.enqueue(val)
            message = f'Enqueued "{val}"'
        else:
            message = 'Please enter a value!'
    elif action == 'dequeue':
        removed = q.dequeue()
        message = f'Dequeued: {removed}' if removed is not None else 'Queue is empty!'

    return jsonify({'message': message, 'nodes': q.items})