from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)

@app.route('/')
def mainpage():
    return str(open('index.html', 'r').read())

if __name__ == '__main__':
    app.run(host='0.0.0.0',  port=5001)
