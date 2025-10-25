class Simulator:
    def __init__(self, ducks, grid):
        self.ducks = ducks
        self.grid = grid
        self.x_size = len(grid[0])
        self.y_size = len(grid)
        self.occupied = set()
        self.neighbours = set()

        self.started = False

    #Starting is in the form [i,j]
    def start_simulation(self, starting):
        self.started = True
        self.occupied.add(starting)
        self.add_new_neighbours(starting)
    
    def simulate_step(self):
        for _ in range(self.ducks.intelligence):
            target = self.ducks.choose_square(self.grid, self.neighbours)
            if self.grid_get(target).attack(self.ducks):
                self.occupied.add(target)
                self.neighbours.remove(target)
                self.add_new_neighbours(target)

        # print(self.occupied)
        self.ducks.reproduce()
        # print(self.ducks.number)


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


    def grid_get(self, points):
        return self.grid[points[0]][points[1]]