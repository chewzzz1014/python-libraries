from random import randint

class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        # any number x such that 1<= x <= num_sides
        return randint(1, self.num_sides)
