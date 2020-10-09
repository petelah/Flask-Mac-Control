from flask import Flask
from flask_socketio import SocketIO
socketio = SocketIO()


def create_app(debug=False):
	app = Flask(__name__)
	app.debug = debug
	app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

	from MacControl.main import main
	app.register_blueprint(main)

	socketio.init_app(app)

	return app