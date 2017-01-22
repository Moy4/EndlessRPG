from random import randint


class Monster:

    def __init__(self):
        for attribute in self.attribute_dict:
            self.attribute_dict[attribute] = randint(25, 50)
        self.stat_dict['HP'] = 50
        self.stat_dict['Mana'] = 5
        choice = 0
        self.monster_img = self.img_list[choice]

    won_ini = "Monster hit you with: "
    img_list = ['monster.jpg']
    monster_img = ''
    attribute_dict = {
        'Strength': 0,
        'Agility': 0,
        'Wisdom': 0,
        'Charisma': 0,
        'Perception': 0,
        'Luck': 0,
    }

    stat_dict = {
        'HP': 0,
        'Mana': 0,
        }

    def attack(self, dice):
        return self.attribute_dict['Strength'] + dice.k6_roll()
