import conversions as conv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import models
import random

api = FastAPI(title="Clash of Chemists Backend Api")
api.add_middleware(CORSMiddleware, allow_origins=["*"])

# Globals
SvkMap = {}


def substrate_image(substrate_name):
    """
    Generate image url for a given substrate.
    """
    return f"https://opsin.ch.cam.ac.uk/opsin/{substrate_name.strip()}.png"


@api.get("/api/problem/generate", response_model=models.ProblemSet, tags=["Problem"])
def generate_problem_set():
    """
    Generate a problem and return a json response containg start and end substrate, svk and 				solution set, substrate image urls.
    """
    problem = conv.generate_problem()
    while True:
        svk = random.randint(1000, 9999)
        if svk not in list(SvkMap.keys()):
            SvkMap[svk] = problem[2]
            break
    result = models.ProblemSet(
        start_substrate=problem[0],
        end_substrate=problem[1],
        start_substrate_image_url=substrate_image(problem[0]),
        end_substrate_image_url=substrate_image(problem[1]),
        svk=svk,
        solution_set=problem[3],
    )
    return result


@api.post(
    "/api/problem/validate", response_model=models.ValidationResult, tags=["Problem"]
)
def validate_solution(solution: str, svk: int):
    """
    Validate a solution against a problem using a svk(Solution Validation Key).
    """
    try:
        if SvkMap[svk] == solution:
            return models.ValidationResult(result=True)
        else:
            return models.ValidationResult(result=False)
        del SvkMap[svk]
    except KeyError:
        raise HTTPException(status_code=404, detail="svk doesn't exist")
