import json

from subprocess import run
from pynput.keyboard import Key, Controller, KeyCode

keyboard = Controller()


def volume_up():
	utfvolume = run(["osascript -e 'output volume of (get volume settings)'"], shell=True, capture_output=True)
	volume = int(utfvolume.stdout.decode('utf-8'))
	volume += 5
	run([f"osascript -e 'set volume output volume {volume}'"], shell=True)


def volume_down():
	utfvolume = run(["osascript -e 'output volume of (get volume settings)'"], shell=True, capture_output=True)
	volume = int(utfvolume.stdout.decode('utf-8'))
	volume -= 5
	run([f"osascript -e 'set volume output volume {volume}'"], shell=True)


def brightness_up():
	keyboard.tap(KeyCode(113))


def brightness_down():
	keyboard.tap(KeyCode(107))


def play_pause():
	keyboard.tap(Key.media_play_pause)


def get_volume():
	utfvolume = run(["osascript -e 'output volume of (get volume settings)'"], shell=True, capture_output=True)
	volume = int(utfvolume.stdout.decode('utf-8'))
	return volume


def vol_change(direction):
	if direction == "up":
		utfvolume = run(["osascript -e 'output volume of (get volume settings)'"], shell=True, capture_output=True)
		volume = int(utfvolume.stdout.decode('utf-8'))
		volume += 5
		run([f"osascript -e 'set volume output volume {volume}'"], shell=True)
	elif direction == "down":
		utfvolume = run(["osascript -e 'output volume of (get volume settings)'"], shell=True, capture_output=True)
		volume = int(utfvolume.stdout.decode('utf-8'))
		volume -= 5
		run([f"osascript -e 'set volume output volume {volume}'"], shell=True)


def sleep():
	run(['pmset displaysleepnow'], shell=True)


def load_settings():
	with open('MacControl/utilities/settings.json', 'r') as file:
		settings = file.readline()
	return json.loads(settings)


def save_settings(data):
	with open('MacControl/utilities/settings.json', 'w') as file:
		file.write(json.dumps(data))
