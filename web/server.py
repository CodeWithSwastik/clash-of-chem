import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Clash of Chemists Backend API")
app.add_middleware(CORSMiddleware, allow_origins=["*"])

lobbies = {}

def substrate_image(substrate_name):
    """
    Generate image url for a given substrate.
    """
    return f"https://opsin.ch.cam.ac.uk/opsin/{substrate_name.strip()}.png"


@app.get("/api/create_lobby")
def create_lobby():
    lobby_id = uuid.uuid4().hex
    data = {"id": lobby_id, "players": []}
    lobbies[lobby_id] = data
    return lobby_id

