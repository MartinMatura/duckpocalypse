import random
import math
import grid as gr

pois = {"gym": [(0, 10), (8, 10), (9, 4), (10, 14), (14, 18), (16, 3), (17, 9)],
        "shop": [(3, 2), (3, 10), (11, 17), (12, 6), (15, 9), (15, 15), (17, 2)],
        "pub": [(3, 18), (6, 5), (7, 0), (10, 11), (14, 8), (14, 14), (18, 3)],
        "library": [(5, 3), (8, 3), (8, 11), (8, 18), (10, 9), (13, 17), (14, 1)]}

def random_choice(grid, neighbours, occupied):
    return random.choice(list(neighbours))

def poi_first(grid, neighbours, occupied):
    #get list of unoccupied POIs
    poi_coords = []
    for val in pois.values():
        for coord in val:
            if coord not in occupied:
                poi_coords.append(coord)

    if len(poi_coords) > 0:
        #find neighbour that is closest to a POI
        lowest_dist = float('inf')
        closest_neighbour = None
        for neighbour in neighbours:
            for poi in poi_coords:
                dist = math.sqrt((neighbour[0] - poi[0])**2 + (neighbour[1] - poi[1])**2)
                if dist < lowest_dist:
                    lowest_dist = dist
                    closest_neighbour = neighbour
        return closest_neighbour
    else:
        return random_choice(grid, neighbours, occupied)

def gym_first(grid, neighbours, occupied):
    #get list of unoccupied gyms
    gym_coords = []
    for coord in pois["gym"]:
        if coord not in occupied:
            gym_coords.append(coord)

    if len(gym_coords) > 0:
        #find neighbour that is closest to a gym
        lowest_dist = float('inf')
        closest_neighbour = None
        for neighbour in neighbours:
            for gym in gym_coords:
                dist = math.sqrt((neighbour[0] - gym[0])**2 + (neighbour[1] - gym[1])**2)
                if dist < lowest_dist:
                    lowest_dist = dist
                    closest_neighbour = neighbour
        return closest_neighbour
    else:
        return random_choice(grid, neighbours, occupied)

#shop_first()
def bread_first_search(grid, neighbours, occupied):
    #get list of unoccupied shops
    shop_coords = []
    for coord in pois["shop"]:
        if coord not in occupied:
            shop_coords.append(coord)
    
    if len(shop_coords) > 0:
        #find neighbour that is closest to a shop
        lowest_dist = float('inf')
        closest_neighbour = None
        for neighbour in neighbours:
            for shop in shop_coords:
                dist = math.sqrt((neighbour[0] - shop[0])**2 + (neighbour[1] - shop[1])**2)
                if dist < lowest_dist:
                    lowest_dist = dist
                    closest_neighbour = neighbour
        return closest_neighbour
    else:
        return random_choice(grid, neighbours, occupied)

def pub_first(grid, neighbours, occupied):
    #get list of unoccupied pubs
    pub_coords = []
    for coord in pois["pub"]:
        if coord not in occupied:
            pub_coords.append(coord)
    
    if len(pub_coords) > 0:
        #find neighbour that is closest to a pub
        lowest_dist = float('inf')
        closest_neighbour = None
        for neighbour in neighbours:
            for pub in pub_coords:
                dist = math.sqrt((neighbour[0] - pub[0])**2 + (neighbour[1] - pub[1])**2)
                if dist < lowest_dist:
                    lowest_dist = dist
                    closest_neighbour = neighbour
        return closest_neighbour    
    else:
        return random_choice(grid, neighbours, occupied)

def library_first(grid, neighbours, occupied):
    #get list of unoccupied libraries
    library_coords = []
    for coord in pois["library"]:
        if coord not in occupied:
            library_coords.append(coord)
    
    if len(library_coords) > 0:
        #find neighbour that is closest to a library
        lowest_dist = float('inf')
        closest_neighbour = None
        for neighbour in neighbours:
            for library in library_coords:
                dist = math.sqrt((neighbour[0] - library[0])**2 + (neighbour[1] - library[1])**2)
                if dist < lowest_dist:
                    lowest_dist = dist
                    closest_neighbour = neighbour 
        return closest_neighbour
    else:
        return random_choice(grid, neighbours, occupied)

def breadth_first(grid, neighbours):
    pass


