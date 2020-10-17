from flask import render_template
from . import main
from ..utilities import get_volume


@main.route('/')
def home():
	volume = get_volume()
	return render_template('index.html', volume=volume)


@main.route('/options')
def options():
	return render_template('options.html')