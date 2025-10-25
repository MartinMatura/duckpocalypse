class Ducks:

    def __init__(self, number, happiness, food_supply, intelligence, strength, strategy):
        self.number = number
        self.happiness = happiness
        self.food_supply = food_supply
        self.intelligence = intelligence # amount of squares that can be attacked
        self.strength = strength # probability of capturing a square
        self.strategy = strategy

    # Increase in food and happiness -> reproduction, Increase in intelligence less
    def reproduce(self):
        growth = (self.happiness + self.food_supply - 1.5 * self.intelligence)
        growth = max(-1, min(1, growth / 100))
        self.number = round(self.number * (1 + growth))

    # Chosen strategy method
    def choose_square(self, grid, neighbours):
        return self.strategy(grid, neighbours)