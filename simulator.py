import grid
import random

class Simulator:
    def __init__(self, ducks, x, y):
        self.ducks = ducks
        self.grid = grid.set_up_grid()
        self.x_size = len(self.grid[0])
        self.y_size = len(self.grid)
        self.occupied = set()
        self.occupied.add((x,y))
        self.neighbours = set()

        self.add_new_neighbours((x,y))
    
    def simulate_step(self):
        self.lose_ducks()
        #Choose new targets
        for _ in range(int(self.ducks.intelligence / 5)):
            target = self.ducks.choose_square(self.grid, self.neighbours, self.occupied)
            if self.grid_get(target).attack(self.ducks):
                self.occupied.add(target)
                self.neighbours.remove(target)
                self.add_new_neighbours(target)

        self.ducks.reproduce()
        # print(list(self.occupied))
        self.print_duck_stats()
        return self.status_api_formatter()

    def print_duck_stats(self):
        print("number: ",self.ducks.number, "   strength: ",self.ducks.strength,
              " happiness:",self.ducks.happiness, " food_supply: ", self.ducks.food_supply, " intelligence: ", self.ducks.intelligence)

    def status_api_formatter(self):
        return {"number":self.ducks.number, "happiness":self.ducks.happiness,
                   "food_supply":self.ducks.food_supply, "intelligence":self.ducks.intelligence,
                   "strength":self.ducks.strength, "occupied":list(self.occupied)}

    def add_new_neighbours(self, point):
        for points in self.get_all_neighbours(point):
            if points not in self.neighbours and points not in self.occupied:
                self.neighbours.add(points)

    def get_all_neighbours(self, point):
        neighbours = []
        i = point[0] - 1
        for _ in range(3):
            j = point[1] - 1
            if i >= 0 and i < self.x_size:
                for __ in range(3):
                    if j >= 0 and j < self.y_size:
                        if not (i == point[0] and j == point[1]):
                            neighbours.append((i,j))
                    j += 1
            i += 1
        return neighbours


    def lose_ducks(self):
        if len(self.occupied) > 15:
            neighbour_freq = dict()
            #frequency of all neighbours
            for neighbour in self.neighbours:
                for adjacent in self.get_all_neighbours(neighbour):
                    if adjacent in self.occupied:
                        neighbour_freq[adjacent] = neighbour_freq.get(adjacent, 0) + 1
            
            for k in neighbour_freq.keys():
                if neighbour_freq[k] >=3 and (random.random() * neighbour_freq[k] / 16) > (self.ducks.food_supply/50):
                    self.grid_get(k).deoccupy(self.ducks)
                    self.occupied.remove(k)
                    self.neighbours.add(k)




    def grid_get(self, points):
        return self.grid[points[0]][points[1]]
