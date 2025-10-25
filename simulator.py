import grid
import strategies

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
        if len(self.occupied) > 15:
            print(self.lose_ducks())


        #Choose new targets
        for _ in range(int(self.ducks.intelligence / 5)):
            target = self.ducks.choose_square(self.grid, self.neighbours, self.occupied)
            if self.grid_get(target).attack(self.ducks):
                self.occupied.add(target)
                self.neighbours.remove(target)
                self.add_new_neighbours(target)

        self.ducks.reproduce()
        # print(list(self.occupied))
        return self.status_api_formatter()

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
        spread =  self.ducks.number / len(self.occupied)
        print(spread)
        if spread < 50:
            neighbour_freq = dict()
            #frequency of all neighbours
            for neighbour in self.neighbours:
                for adjacent in self.get_all_neighbours(neighbour):
                    neighbour_freq[adjacent] = neighbour_freq.get(adjacent, 0) + 1
            
            maxi = max(neighbour_freq, key=neighbour_freq.get)
            while maxi not in self.occupied:
                neighbour_freq.pop(maxi)
                maxi = max(neighbour_freq, key=neighbour_freq.get)
            
            self.occupied.pop(maxi)
            self.neighbours.add(maxi)
            return True
        return False

    def grid_get(self, points):
        return self.grid[points[0]][points[1]]
