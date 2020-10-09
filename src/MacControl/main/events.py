from MacControl.utilities.utils import get_volume, volume_up, volume_down, brightness_up, brightness_down, play_pause, sleep
from flask_socketio import send
from .. import socketio


@socketio.on('message')
def handleMessage(msg):
	"""
	Handles the message coming back from the client to decide what to do.
	Note: please break this up to unto functions.
	:param msg: string from the client
	:return: N/A
	"""
	print(f'Message: {msg}')
	if msg == "VolDown":
		volume_down()
		print(get_volume())
		send(get_volume(), broadcast=True)
	elif msg == "VolUp":
		volume_up()
		print(get_volume())
		send(get_volume(), broadcast=True)
	elif msg == "BrDown":
		brightness_down()
	elif msg == "BrUp":
		brightness_up()
	elif msg == "PP":
		play_pause()
	elif msg == "Sleep":
		sleep()