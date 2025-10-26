from typing import Union
from typing_extensions import Literal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ducks import Ducks
import strategies
from simulator import Simulator
import uvicorn

class DuckInfo(BaseModel):
    happiness: int
    food_supply: int 
    intelligence: int
    strength: int
    strategy: Literal["random_choice", "poi_first_random", "breadth_first", "poi_first_bfs", "gym_first", "pub_first", "library_first", "bread_first"]
    starting_x: int
    starting_y: int

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


no_ducks = 100
strat = {"random_choice": strategies.random_choice, "poi_first_random": strategies.poi_first_random, "breadth_first": strategies.breadth_first, "poi_first_bfs": strategies.poi_first_bfs, "gym_first": strategies.gym_first, "pub_first": strategies.pub_first, "library_first": strategies.library_first, "bread_first": strategies.bread_first_search}
active_simulation = None

@app.post("/start-conditions/")
async def start(duck_info: DuckInfo):
    ducks = Ducks(no_ducks, duck_info.happiness, duck_info.food_supply, duck_info.intelligence, duck_info.strength, strat[duck_info.strategy])
    global active_simulation
    active_simulation = Simulator(ducks, duck_info.starting_x, duck_info.starting_y)
    return {"status": "Simulation started"}

@app.get("/get-next-step/")
def get_next_step():
    global active_simulation
    if active_simulation is None:
        print("No active simulation found")
        return {"error": "No active simulation"}
    
    step_result = active_simulation.simulate_step()
    print("Step result:", step_result)
    return step_result


@app.delete("/end-simulation/")
def end_simulation():
    global active_simulation
    if active_simulation is None:
        return {"error": "No active simulation to end"}
    active_simulation = None
    return {"status": "Simulation ended"}

@app.get("/grid/")
def get_grid():
    global active_simulation
    if active_simulation is None:
        # no simulation yet → show blank grid
        grid = [[{"owner": None} for _ in range(20)] for _ in range(20)]
        return {"grid": grid}

    size_y = active_simulation.y_size
    size_x = active_simulation.x_size
    owned = active_simulation.occupied

    grid = []
    for i in range(size_y):
        row = []
        for j in range(size_x):
            if (i, j) in owned:
                row.append({"owner": "duck"})  # claimed tile
            else:
                row.append({"owner": None})     # unclaimed tile
        grid.append(row)

    return {"grid": grid}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)