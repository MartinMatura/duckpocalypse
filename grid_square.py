from random import random

class grid_square:
    def __init__(self, POI = None):
        self.POI = POI
        self.captured = False

    def attack(self, duck_stats):
        probability = duck_stats.strength/100 #+ some function of number of ducks and hunger of ducks

        if probability > random():
            return True
        return False

    def capture(self, duck_stats):
        if self.POI:
            self.POI = None
        self.captured = True