class Monster():

    won_ini = "Monster is attacking first!"

    attribute_dict = {
        'Strength': 30,
        'Agility': 40,
        'Wisdom': 30,
        'Charisma': 30,
        'Perception': 30,
        'Luck': 30,
    }

    stat_dict = {
        'HP': 20,
        'Mana': 5,
        }

    def attack(self, dice):
        return self.attribute_dict['Strength'] + dice.k20_roll()
