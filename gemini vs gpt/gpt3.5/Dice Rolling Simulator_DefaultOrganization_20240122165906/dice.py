'''
This file contains the Dice class which represents a dice object.
'''
import random
class Dice:
    def roll(self, sides):
        return random.randint(1, sides)