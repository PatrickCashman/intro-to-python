import random

class Dice:
    def __init__(self, sides) -> None:
        self.sides = sides
        
    def roll(self):
        return (random.randint(1, self.sides), random.randint(1, self.sides))
        

dice_six_sides = Dice(10)

print(dice_six_sides.roll())