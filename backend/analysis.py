import simulator as sim
import strategies as strat
import ducks
from grid import print_grid as grid_print
from copy import deepcopy

def run_sim(ducks, x=0, y=0, trials = 10, iters = 100, print_stats = True, print_grid = False):
    total_occupy = 0
    total_ducks = 0
    

    for i in range(trials):
        d = deepcopy(ducks)
        s = sim.Simulator(d, x, y)
        # d = deepcopy(ducks)
        strat.reset_breadth_first()
        for _ in range(iters):
            s.simulate_step()

        if print_grid:
            grid_print(s.grid, s.occupied)
            print("|" * 40)

        total_occupy += len(s.occupied)
        total_ducks += s.ducks.number
        del s, d

    average_occupy = total_occupy / trials
    average_ducks = total_ducks / trials

    if print_stats:
        print("Average occupied: ", average_occupy)
        print("No. of Ducks: ", average_ducks)

    return [average_occupy, average_ducks]


def make_duck(strategy,n=100, happiness=20,food_supply=20,intelligence=5,strength=20):
    return ducks.Ducks(n,happiness,food_supply,intelligence,strength,strategy)

def print_stats(o, strategy=None, comment = ""):
    if strategy:
        print(strategy.__name__, end = "\t")
    print(comment)
    print("Occupied:",o[0])
    print("No. ducks:",o[1])

def compare_strategy(strategy1, strategy2, x=0,y=0, trials=10, iters=100, num_ducks=100, happiness=20,food_supply=20,intelligence=5,strength=20):
    o1 = run_sim(make_duck(strategy1,num_ducks,happiness,food_supply,intelligence,strength),x=x,y=y,trials=trials,iters=iters, print_stats= False)
    o2 = run_sim(make_duck(strategy2,num_ducks,happiness,food_supply,intelligence,strength),x=x,y=y,trials=trials,iters=iters, print_stats= False)
                 
    print_stats(o1,strategy1)
    print_stats(o2,strategy2)

#conditional choice: 0 is happiness, 1 is food_supply, 2 is intelligence, 3 is strength

def run_switch_sim(strategy1, strategy2, conditional_choice, threshold, x=0, y=0, trials = 10, iters = 100, print_stats = True, print_grid = False):
    duck = make_duck(strategy1)
    total_occupy = 0
    total_ducks = 0
    for i in range(trials):
        d = deepcopy(duck)
        s = sim.Simulator(d, x, y, conditional_choice, threshold, strategy2)
        # d = deepcopy(ducks)
        strat.reset_breadth_first()
        for _ in range(iters):
            s.simulate_step()

        if print_grid:
            grid_print(s.grid, s.occupied)
            print("|" * 40)

        total_occupy += len(s.occupied)
        total_ducks += s.ducks.number
        del s, d

    average_occupy = total_occupy / trials
    average_ducks = total_ducks / trials

    if print_stats:
        print("Average occupied: ", average_occupy)
        print("No. of Ducks: ", average_ducks)

    return [average_occupy, average_ducks]

def run_switch_sim_food(ducks,strategy, threshold=15, x=0, y=0, trials = 10, iters = 100, print_stats = True, print_grid = False):
    total_occupy = 0
    total_ducks = 0

    for i in range(trials):
        d = deepcopy(ducks)
        s = sim.Simulator(d, x, y)
        # d = deepcopy(ducks)
        strat.reset_breadth_first()
        for _ in range(iters):
            if d.food_supply >= threshold:
                d.strategy = strategy
            s.simulate_step()

        if print_grid:
            grid_print(s.grid, s.occupied)
            print("|" * 40)

        total_occupy += len(s.occupied)
        total_ducks += s.ducks.number
        del s, d

    average_occupy = total_occupy / trials
    average_ducks = total_ducks / trials

    if print_stats:
        print("Average occupied: ", average_occupy)
        print("No. of Ducks: ", average_ducks)

    return [average_occupy, average_ducks]

# o1 = run_switch_sim_food(make_duck(strat.bread_first_search,food_supply=10),strat.poi_first_bfs,threshold=15,x=10,y=10, print_stats= False)
# o2 = run_sim(make_duck(strat.poi_first_bfs,food_supply=10),x=10,y=10, print_stats= False)

o1 = run_switch_sim(strat.bread_first_search, strat.poi_first_random, threshold=25, conditional_choice=1)
o2 = run_sim(make_duck(strat.poi_first_random))


print_stats(o1)
print_stats(o2)


#Bread first and then poi seems to optimise?

# compare_strategy(strat.bread_first_search, strat.poi_first_bfs, x=10,y=10,food_supply=10,intelligence=10)

# d = ducks.Ducks(100, 20, 20, 5, 20, strat.breadth_first)
# run_sim(d, x=5,y=10,print_stats=True,print_grid=True)