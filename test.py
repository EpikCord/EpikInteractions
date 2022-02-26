from EpikInteractions import Interaction
from json import loads, dumps
from fastapi import FastAPI

app = FastAPI()

@app.post("/interactions")
async def root(interaction: Interaction):
    ...
