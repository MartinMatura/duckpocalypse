from backend import grid_square
from backend.grid import *
from backend.ducks import *
from backend.simulator import *
from backend.strategies import *

if __name__ == "__main__":
    grid = set_up_grid()
    ducks = Ducks(100, 20, 20, 10, 20, poi_first_bfs)
    s1 = Simulator(ducks, 0, 0)
    for i in range(100):
        s1.simulate_step()
        input("press enter")
        print_grid(s1.grid, s1.occupied)
    print_grid(s1.grid, s1.occupied)
    print("Occupied: ", len(s1.occupied))