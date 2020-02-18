from flask import Flask
from flask_socketio import SocketIO

import rccar

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('command')
def on_command(cmd, power):
    print("Woot")
    cmd_dict = {'left':rccar.turn_left,
                'right':rccar.turn_right}
    cmd_dict[cmd](1, float(power))

@app.route('/')
def mainpage():
    return str(open('index.html', 'r').read())

@app.route('/socket.io.js')
def socketjs():
    return str(open('socket.io.js', 'r').read())

@app.route('/virtualjoystick.js')
def virtualjoystickjs():
    return str(open('virtualjoystick.js', 'r').read())

if __name__ == '__main__':
    socketio.run(app, port=5000, host='0.0.0.0')
