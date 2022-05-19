import random

print(0 % 3)


# Random variables - using builtin module
# Exercise

class Dice:

    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
print(dice.roll())
print(dice.roll())
