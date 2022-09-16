from pydantic import BaseModel, HttpUrl


class ProblemSet(BaseModel):
    start_substrate: str
    end_substrate: str
    start_substrate_image_url: HttpUrl
    end_substrate_image_url: HttpUrl
    solution: str
    solution_set: list
