from flask import Flask

import rccar

app = Flask(__name__)

@app.route('/')
def mainpage():
 return '''<form action="http://192.168.4.1:5000/f">\n <input type="submit" value="Move forward" />\n</form>\n
           <form action="http://192.168.4.1:5000/b">\n <input type="submit" value="Move backward" />\n</form>\n
           <form action="http://192.168.4.1:5000/l">\n <input type="submit" value="Move left" />\n</form>\n
           <form action="http://192.168.4.1:5000/r">\n <input type="submit" value="Move right" />\n</form>'''

@app.route('/c')
def clean():
 rccar.cleanup()
 return 'Clean successful'

@app.route('/f')
def moveforward():
 rccar.move_forward(1, 70)
 return 'Moved forward\n<meta http-equiv="Refresh" content="0; url=http://192.168.4.1:5000/" />'

@app.route('/b')
def movebackward():
 rccar.move_backward(1, 70)
 return 'Moved backward\n<meta http-equiv="Refresh" content="0; url=http://192.168.4.1:5000/" />'

@app.route('/r')
def moveright():
 rccar.turn_right(1, 70)
 return 'Moved right\n<meta http-equiv="Refresh" content="0; url=http://192.168.4.1:5000/" />'

@app.route('/l')
def moveleft():
 rccar.turn_left(1, 70)
 return 'Moved left\n<meta http-equiv="Refresh" content="0; url=http://192.168.4.1:5000/" />'
