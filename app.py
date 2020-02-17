from flask import Flask
from flask_socketio import SocketIO

import rccar

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('command')
def on_command(cmd):
    print("Woot")
    rccar.turn_left(1, 70)

@app.route('/')
def mainpage():
    return str(open('index.html', 'r').read())

@app.route('/socket.io.js')
def socketjs():
    return str(open('socket.io.js', 'r').read())

if __name__ == '__main__':
    socketio.run(app, port=5000, host='0.0.0.0')
