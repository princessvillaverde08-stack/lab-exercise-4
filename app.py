from flask import Flask, render_template

# Import individual route blueprints from the routes folder
from routes.uppercase import uppercase_bp
from routes.circle import circle_bp
from routes.triangle import triangle_bp
from routes.linkedlist import linkedlist_bp
from routes.infix import infix_bp
from routes.queue import queue_bp
from routes.deque import deque_bp

app = Flask(__name__)

# Register Blueprints for each work
app.register_blueprint(uppercase_bp)
app.register_blueprint(circle_bp)
app.register_blueprint(triangle_bp)
app.register_blueprint(linkedlist_bp)
app.register_blueprint(infix_bp)
app.register_blueprint(queue_bp)
app.register_blueprint(deque_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)