import conversions as conv
from flask import Flask
from flask.json import jsonify as json

api = Flask('Clash of Chemists Api')


def substrate_image(substrate_name):
	'''
	Generate image url for a given substrate.
	'''
	return f'https://opsin.ch.cam.ac.uk/opsin/{substrate_name}.png'

@api.route('/api/problem')
def generate_problem_route():
	'''
	Generate a problem set and return a json response containg start and end substrate, solution 		and solution set, substrate image urls.
	'''
	problem = conv.generate_problem()
	result = {
	'start_substrate': problem[0],
	'end_substrate':problem[1],
	'start_substrate_image_url': substrate_image(problem[0]),
	'end_substrate_image_url': substrate_image(problem[1]),
	'solution':problem[2],
	'solution_set':problem[3]}
	return json(result)
	
api.run()