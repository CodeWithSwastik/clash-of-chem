from pydantic import BaseModel

class ProblemSet(BaseModel):
	start_substrate : str
	end_substrate : str
	start_substrate_image_url : str
	end_substrate_image_url : str
	solution : str
	solution_set : list