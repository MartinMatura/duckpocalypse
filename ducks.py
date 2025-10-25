import math

class Ducks:

    def __init__(self, number, happiness, food_supply, intelligence, strength, strategy):
        self.number = number
        self.happiness = happiness
        self.food_supply = food_supply
        self.intelligence = intelligence # amount of squares that can be attacked
        self.strength = strength # probability of capturing a square
        self.strategy = strategy

    # Increase in food and happiness will lead to more reproduction, more intelligence will lead to less
    def reproduce(self):
        new_amount = round(self.number * (1 + ((self.happiness + self.food_supply) / (self.happiness + self.food_supply + self.intelligence))))
        if new_amount < self.food_supply * 50:
            self.number = new_amount
        else:
            # Max ducks for food supply
            self.number = self.food_supply * 50

    def choose_square(self, grid):
        pass

ducks = Ducks(100, 40, 25, 50, 100, None)
ducks.reproduce()
print(ducks.number)