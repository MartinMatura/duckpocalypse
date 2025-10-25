class Simulator:
    def __init__(self, ducks, grid):
        self.ducks = ducks
        self.grid = grid
        self.x_size = len(grid[0])
        self.y_size = len(grid)
        self.occupied = set()
        self.neighbours = []

    #Starting is in the form [i,j]
    def simulate(self, starting):
        self.add_new_neighbours(starting)
        for target in self.ducks.choose_square(self.neighbours).attack:
            target.attack
        self.ducks.reproduce()


    def add_new_neighbours(self, point):
        for points in self.get_all_neighbours(point):
            if points not in self.neighbours and self.grid_get(points) :
                self.neighbours.append(points)

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