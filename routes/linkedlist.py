from flask import Blueprint, request, jsonify

linkedlist_bp = Blueprint('linkedlist_bp', __name__)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class BackendLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove_beginning(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return data

    def remove_at_end(self):
        if not self.head:
            return None
        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            return data
        current = self.head
        while current.next != self.tail:
            current = current.next
        data = self.tail.data
        current.next = None
        self.tail = current
        return data

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def remove_at(self, data):
        if not self.head:
            return None
        if self.head.data == data:
            return self.remove_beginning()
        current = self.head
        while current.next:
            if current.next.data == data:
                removed_data = current.next.data
                current.next = current.next.next
                if not current.next:
                    self.tail = current
                return removed_data
            current = current.next
        return None

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

# Linked List State
ll = BackendLinkedList()
ll.insert_at_end("10")
ll.insert_at_end("20")
ll.insert_at_end("30")

@linkedlist_bp.route('/api/linkedlist', methods=['POST'])
def api_linkedlist():
    req = request.json or {}
    action = req.get('action')
    val = req.get('value', '').strip()

    message = ""
    if action == 'add_start':
        if val:
            ll.insert_at_beginning(val)
            message = f'Added "{val}" to head'
        else:
            message = 'Please enter a value!'
    elif action == 'add_end':
        if val:
            ll.insert_at_end(val)
            message = f'Added "{val}" to tail'
        else:
            message = 'Please enter a value!'
    elif action == 'rem_start':
        removed = ll.remove_beginning()
        message = f'Removed head: {removed}' if removed is not None else 'List is empty'
    elif action == 'rem_end':
        removed = ll.remove_at_end()
        message = f'Removed tail: {removed}' if removed is not None else 'List is empty'
    elif action == 'search':
        if val:
            found = ll.search(val)
            message = f'Found "{val}" in list!' if found else f'"{val}" not found'
        else:
            message = 'Please enter a value!'
    elif action == 'rem_val':
        if val:
            removed = ll.remove_at(val)
            message = f'Removed: {removed}' if removed is not None else f'"{val}" not found'
        else:
            message = 'Please enter a value!'

    return jsonify({'message': message, 'nodes': ll.to_list()})