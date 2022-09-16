import conversions as conv
from fastapi import FastAPI
import models

api = FastAPI(title = 'Clash of Chemists Backend Api')


def substrate_image(substrate_name):
	'''
	Generate image url for a given substrate.
	'''
	return f'https://opsin.ch.cam.ac.uk/opsin/{substrate_name}.png'

@api.get('/api/problem', response_model=models.ProblemSet,tags=['Api'])
def generate_problem_set():
	'''
	Generate a problem and return a json response containg start and end substrate, solution and 		solution set, substrate image urls.
	'''
	problem = conv.generate_problem()
	result =  models.ProblemSet(
	start_substrate= problem[0],
	end_substrate= problem[1], 
	start_substrate_image_url = substrate_image(problem[0]), 
	end_substrate_image_url = substrate_image(problem[1]),
	solution = problem[2],
	solution_set = problem[3])
	return result