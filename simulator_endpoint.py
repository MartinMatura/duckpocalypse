from typing import Union
from typing_extensions import Literal
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
    strategy: Literal["random_choice", "poi_first", "breadth_first"]
    starting_x: int
    starting_y: int

app = FastAPI()
no_ducks = 100
strat = {"random_choice": strategies.random_choice, "poi_first": strategies.poi_first, "breadth_first": strategies.breadth_first}
active_simulation = None

@app.post("/start-conditions/")
async def start(duck_info: DuckInfo):
    ducks = Ducks(no_ducks, duck_info.happiness, duck_info.food_supply, duck_info.intelligence, duck_info.strength, strat[duck_info.strategy])
    global active_simulation
    active_simulation = Simulator(ducks, duck_info.starting_x, duck_info.starting_y)
    return {"status": "Simulation started"}

@app.get("/get-next-step/")
def get_next_step():
    if active_simulation is None:
        return {"error": "No active simulation"}
    return active_simulation.simulate_step()

@app.delete("/end-simulation/")
def end_simulation():
    if active_simulation is None:
        return {"error": "No active simulation to end"}
    global active_simulation
    active_simulation = None
    return {"status": "Simulation ended"}