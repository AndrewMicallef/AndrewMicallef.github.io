from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def hello():
    return "Hello World!"


@socketio.on('SVGLoad')
# Decorator to catch an event called "my event":
def test_message(message):
# test_message() is the event callback function.
    emit('my response', {'data': 'got it!'})
# Trigger a new event called "my response"
# that can be caught by another callback later in the program.

if __name__ == "__main__":
    socketio.run(app)
