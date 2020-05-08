import random

#Simulates a roll of a die
def dice():
    diceRoll = random.randrange(1,7)
    return diceRoll

print(dice())
