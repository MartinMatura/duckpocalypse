class simulator:
    def __init__(self, ducks, grid):
        self.ducks = ducks
        self.grid = grid
        self.occupied = []

    #Starting is in the form [i,j]
    def simulate(self, starting):
        occupied += grid.get_all_neighbours(starting)

    def add_new_neighbours(self, point, grid):
        occupied_set = set(self.occupied)
        for square in grid.get_all_neighbours(point):
            if not square.occupied and square not in occupied_set:
                self.occupied.append(square)
            