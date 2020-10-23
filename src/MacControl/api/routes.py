from flask import request, jsonify, abort
from . import api
from ..utilities import get_volume, volume_up, volume_down, brightness_up, brightness_down, play_pause, sleep, load_settings, save_settings


def check_auth():
	auth = load_settings()
	if auth['API']:
		return True
	else:
		return False


@api.route('/api', methods=['GET'])
def api_home():
	return "<h1>API HOME</h1>"


@api.route('/api/controller', methods=['GET'])
def api_commands():
	volume = get_volume()
	if check_auth():
		if 'id' in request.args:
			id = request.args['id']
			if id == 'VolUp':
				volume_up()
				return jsonify({"vol": volume}), 200
			elif id == 'VolDwn':
				return jsonify({"vol": volume}), 200
			elif id == 'BrUp':
				brightness_up()
				return 200
			elif id == 'BrDwn':
				brightness_down()
				return 200
			elif id == 'PP':
				play_pause()
				return 200
			else:
				abort(404, description="Resource not found")
	else:
		abort(403, description="No Authorization")
