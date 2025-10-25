import random
import math

pois = {"gym": [(0, 10), (8, 10), (9, 4), (10, 14), (14, 18), (16, 3), (17, 9)],
        "shop": [(3, 2), (3, 10), (11, 17), (12, 6), (15, 9), (15, 15), (17, 2)],
        "pub": [(3, 18), (6, 5), (7, 0), (10, 11), (14, 8), (14, 14), (18, 3)],
        "library": [(5, 3), (8, 3), (8, 11), (8, 18), (10, 9), (13, 17), (14, 1)]}

def random_choice(grid, neighbours):
    return random.choice(neighbours)

def poi_first(grid, neighbours, occupied):
    #get list of unoccupied POIs
    poi_coords = []
    for val in pois.values():
        for coord in val:
            if coord not in occupied:
                poi_coords.append(coord)
    
    #find neighbour and POI that are closest to each other
    lowest_dist = 1000
    closest_neighbour = None
    
    for neighbour in neighbours:
        for poi in poi_coords:
            dist = math.sqrt((neighbour[0] - poi[0])**2 + (neighbour[1] - poi[1])**2)
            if dist < lowest_dist:
                closest_neighbour = neighbour

    return closest_neighbour
        

def breadth_first(grid, neighbours):
    pass


