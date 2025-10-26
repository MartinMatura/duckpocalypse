from random import random

class GridSquare:
    def __init__(self, POI = None):
        self.POI = POI
        # self.captured = False

    def attack(self, duck_stats):
        probability = duck_stats.strength/60 #+ some function of number of ducks and hunger of ducks

        if probability > random():
            self.capture(duck_stats)
            return True
        return False

    def capture(self, duck_stats):
        if self.POI:
            if self.POI == "gym":
                duck_stats.strength += 5
            elif self.POI == "pub":
                duck_stats.happiness += 5
            elif self.POI == "library":
                duck_stats.intelligence += 5
            elif self.POI == "shop":
                duck_stats.food_supply += 5
        # self.captured = True   

    def deoccupy(self, duck_stats):
        if self.POI:
            if self.POI == "gym":
                duck_stats.strength -= 5
            elif self.POI == "pub":
                duck_stats.happiness -= 5
            elif self.POI == "library":
                duck_stats.intelligence -= 5
            elif self.POI == "shop":
                duck_stats.food_supply -= 5