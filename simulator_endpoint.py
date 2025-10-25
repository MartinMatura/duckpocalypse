from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from ducks import Ducks
import strategies
from simulator import Simulator

class DuckInfo(BaseModel):
    happiness: int
    food_supply: int 
    intelligence: int
    strength: int
    strategy: str

app = FastAPI()
no_ducks = 100
strat = {"random_choice": strategies.random_choice, "poi_first": strategies.poi_first, "breadth_first": strategies.breadth_first}

@app.post("/start-conditions/")
async def start(duck_info: DuckInfo):
    ducks = Ducks(no_ducks, duck_info.happiness, duck_info.food_supply, duck_info.intelligence, duck_info.strength, strat[duck_info.strategy])
    

@app.get("/get_next_step/")
def get_next_step():
    return "Hello World"

