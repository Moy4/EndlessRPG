from random import randint


class Item:

    defens = 0
    attack = 0
    heal = 0
    name = ''


class Sword(Item):
    def __init__(self):
        self.name = "Super Miecz "
        self.attack = randint(1, 5)
        self.info = "+" + str(self.attack) + " to base damage"


class Armor(Item):
    def __init__(self):
        self.name = "Fajna Zbroja "
        self.defense = randint(1, 5)
        self.info = "+" + str(self.defense) + " to base damage"


class Potion(Item):
    def __init__(self):
        self.name = "Mikstura "
        self.heal = 10
        self.info = "+" + str(self.heal) + " to HP when used"

