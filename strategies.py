import random
import math
from grid import pois

def random_choice(grid, neighbours, occupied):
    return random.choice(list(neighbours))

def poi_first(grid, neighbours, occupied):
    #get list of unoccupied POIs
    poi_coords = []
    for val in pois.values():
        for coord in val:
            if coord not in occupied:
                poi_coords.append(coord)
    
    #find neighbour and POI that are closest to each other
    lowest_dist = float('inf')
    closest_neighbour = None
    
    for neighbour in neighbours:
        for poi in poi_coords:
            dist = math.sqrt((neighbour[0] - poi[0])**2 + (neighbour[1] - poi[1])**2)
            if dist < lowest_dist:
                lowest_dist = dist
                closest_neighbour = neighbour

    if closest_neighbour == None:
        return random_choice(grid, neighbours, occupied)

    return closest_neighbour
        

def breadth_first(grid, neighbours):
    pass


