from flask import Blueprint, request, jsonify

infix_bp = Blueprint('infix_bp', __name__)

@infix_bp.route('/api/infix', methods=['POST'])
def api_infix():
    data = request.json or {}
    infix = data.get('expression', '').strip()
    
    def get_precedence(op):
        if op in ('+', '-'): return 1
        if op in ('*', '/'): return 2
        if op in ('^',): return 3
        return 0

    try:
        stack = []
        postfix = ""
        i = 0
        while i < len(infix):
            c = infix[i]
            if c == ' ':
                i += 1
                continue
            if c.isalnum():
                postfix += c
            elif c == '(':
                stack.append(c)
            elif c == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                if stack and stack[-1] == '(':
                    stack.pop()
            else:
                while stack and get_precedence(c) <= get_precedence(stack[-1]):
                    postfix += stack.pop()
                stack.append(c)
            i += 1
        while stack:
            postfix += stack.pop()
        return jsonify({'result': postfix if postfix else 'Invalid Expression!'})
    except Exception:
        return jsonify({'result': 'Invalid Expression!'})