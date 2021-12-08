from flask import Flask, redirect, url_for 
from flask_socketio import SocketIO, send
from flask.templating import render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

# @app.route('/')
# def index():
#     return render_template(redirect(url_for("/<user>")))

@app.route('/<user>')
def index(user):
    return render_template("index.html",user=user)

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

if __name__ == '__main__':
	socketio.run(app)
