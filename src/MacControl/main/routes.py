from flask import render_template
from . import main
from ..utilities import get_volume, load_settings


@main.route('/')
def home():
	volume = get_volume()
	settings = load_settings()
	web = settings['WEB']
	return render_template('index.html', volume=volume, web=web)


@main.route('/options')
def options():
	settings = load_settings()
	web = settings['WEB']
	api = settings['API']
	if web:
		web = "checked"
	else:
		web = ""
	if api:
		api = "checked"
	else:
		api = ""
	return render_template('options.html', web=web, api=api)
