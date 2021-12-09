# add names in the input and restart and then  

from flask import Flask, request
from flask_socketio import SocketIO, send
from flask.templating import render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

# for debuging purpose
socketio = SocketIO(app, logger=True, engineio_logger=True, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template("index.html")

clients = list()

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	print("-"*10)
	# print("request.namespace.socket.sessid", request.namespace.socket.sessid)
	print("request.sid", request.sid)
	clients.append(request.sid)
	print(clients)
	print("-"*10)
	send(msg, broadcast=True)

	# socketio.emit(msg, broadcast=True)
@socketio.on('chat_message')
def handleChat(data):
	print(data)
	print("-"*10)
	# print("request.namespace.socket.sessid", request.namespace.socket.sessid)
	print("request.sid", request.sid)
	print(clients)
	print("-"*10)
	clients.append(request.sid)
	clients[0].emit(data, broadcast=True)


if __name__ == '__main__':
	socketio.run(app)
# 7YdPWbY5BmP5K9VPAAAA
# VqYjL--_AOZfbIHSAAAL


