class Monster():

    won_ini = "Monster hit you with: "

    attribute_dict = {
        'Strength': 30,
        'Agility': 40,
        'Wisdom': 30,
        'Charisma': 30,
        'Perception': 30,
        'Luck': 30,
    }

    stat_dict = {
        'HP': 50,
        'Mana': 5,
        }

    def attack(self, dice):
        return self.attribute_dict['Strength'] + dice.k4_roll()
