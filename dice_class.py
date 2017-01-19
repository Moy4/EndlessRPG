from random import randint


class Dice:

    def k20_roll(self):
        return randint(0, 20)

    def k4_roll(self):
        return randint(0, 4)

    def k6_roll(self):
        return randint(0, 6)
