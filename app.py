from flask import Flask
import socket

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def instance_id():
	instance_id = socket.gethostname()
	return {'instance_id' : instance_id}, 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000) 
