# from typing import Union

from fastapi import FastAPI
from robot import run

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/test", status_code=201)
async def run_test():
    run("self.robot")
