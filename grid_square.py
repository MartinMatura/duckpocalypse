class GridSquare:
    humans = 100
    def __init__(self, dif_iq, dif_strength, POI = None, ducks = 0):
        self.dif_iq = dif_iq
        self.dif_strength = dif_strength
        self.POI = POI
        self.ducks = ducks


    def attack(self, num_ducks, duck_stats, adjacent):
        adjacent_modifier = 50 * adjacent #number of adjacent tiles

        hunger_modifier = duck_stats.food/100 #Debuff from hunger

        strength_attack = (num_ducks * duck_stats.strength) * hunger_modifier + adjacent_modifier

        iq_attack = duck_stats.intelligence/self.humans * hunger_modifier + adjacent_modifier

        
        if strength_attack > self.dif_strength or iq_attack > self.dif_iq: 
            return True
        return False

    def capture(self, num_ducks):
        if self.POI:
            #increase ducks variable
            self.POI = None
            #Unless its food?
        self.ducks = num_ducks
    