from ..cli import conversions as conv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI(title="Clash of Chemists Backend API")
api.add_middleware(CORSMiddleware, allow_origins=["*"])


def substrate_image(substrate_name):
    """
    Generate image url for a given substrate.
    """
    return f"https://opsin.ch.cam.ac.uk/opsin/{substrate_name.strip()}.png"