from flask import Flask



app = Flask(__name__)

@app.route('/')
def index():
	return 'asdasd'
	
	
	
if __name__ == '__main__':
	app.run(debug = True, host = '192.168.0.3')
