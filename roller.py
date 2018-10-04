import random

class Dice:
    pass

    def __init__(self):
        self = self
        pass

    def roll(self, dice)
        return random.randint(1,dice)



TotalDice = int(input("Home many Dice would you like to roll:"))
TotalSides = int(input("How many sides on the Dice:"))
Sum = 0
x = 0
while x != TotalDice:
    Sum = Sum + random.randint(0, TotalSides)
    print("{} Dice Rolled".format(x+1))
    x = x + 1
print(Sum)
