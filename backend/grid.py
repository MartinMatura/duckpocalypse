import grid_square

pois = {
    "gym": [(0, 10), (8, 10), (9, 4), (10, 14), (14, 18), (16, 3), (17, 9)],
<<<<<<< HEAD
    "shop": [(3, 2), (3, 10), (11, 17), (12, 6), (15, 9), (15, 15), (17,2)],
=======
    "shop": [(3, 2), (3, 10), (11, 17), (12, 6), (15, 9), (15, 15), (17, 2)],
>>>>>>> 909591ca4acb84726a22ddae7e2f8d3de94e8b85
    "pub": [(3, 18), (6, 5), (7, 0), (10, 11), (14, 8), (14, 14), (18, 3)],
    "library": [(5, 3), (8, 3), (8, 11), (8, 18), (10, 9), (13, 17), (14, 1)]
}

def set_up_grid():
    grid = [[grid_square.GridSquare(None) for _ in range(20)] for _ in range(20)]

    for poi, coords in pois.items():
        for row, col in coords:
            grid[row][col].POI = poi

    return grid


def print_grid(grid, occupied):
    for i in range(len(grid)):
        line = ""
        for j in range(len(grid[0])):
            if (i,j) in occupied:
                if grid[i][j].POI:
                    line += "X "
                else:
                    line += "O "
            else:
                if grid[i][j].POI:
                    line += "+ "
                else:
                    line += "_ "
        print(line)
