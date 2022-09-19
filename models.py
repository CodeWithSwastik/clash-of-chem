from pydantic import BaseModel, HttpUrl


class ProblemSet(BaseModel):
    start_substrate: str
    end_substrate: str
    start_substrate_image_url: HttpUrl
    end_substrate_image_url: HttpUrl
    svk: int
    solution_set: list

class ValidationSet(BaseModel):
	svk: int
	solution : str

class ValidationResult(BaseModel):
	result : bool