from random import randint


class BaseCharacter:
    """
    Base Hero Class, with random atributes and specified information
    This class must evolve into sht more specified for
    diffrent classes under this one for example:
    Barbarian must have more srength than mage.
    Strength must affect HP in stat_dict
    Wisdom must affect Mana in stat_dict

    """
    def __init__(self):
        for attribute in self.attribute_dict:
            self.attribute_dict[attribute] = randint(25, 50)

    info_dict = {'CLASS NAME': '', 'NAME': '', 'BIO': ''}

    attribute_dict = {
        'Strength': 0,
        'Agility': 0,
        'Wisdom': 0,
        'Charisma': 0,
        'Perception': 0,
        'Luck': 0,
    }

    stat_dict = {
        'HP': 20,
        'Mana': 5,
        'XP': 0,
        "LVL": 1,
    }

    # behaviour that every character will have

    def attack(self, attribute, dice):
        return attribute + dice.k20_roll()

    def count_resistance(self, attribute, dice):
        return attribute + dice.k4_roll()

    def set_name(self, name_string):
        self.info_dict['name'] = name_string


class Barbarian(object, BaseCharacter):
    def __init__(self):
        BaseCharacter.__init__(self)
    info_dict = {'CLASS NAME': 'Barbarian', 'NAME': 'Socrates'}
    bio = 'A barbarian is a human who is perceived to be uncivilised or primitive. The designation is usually applied as generalization based on a popular stereotype; barbarians can be any member of a nation judged by some to be less civilised or orderly (such as a tribal society), but may also be part of a certain "primitive" cultural group (such as nomads) or social class (such as bandits) both within and outside ones own nation'

    stat_dict = {
        'HP': 30,
        'Mana': 10,
        'XP': 0,
        "LVL": 1,
    }


class Hunter(object, BaseCharacter):
    def __init__(self):
        BaseCharacter.__init__(self)
    info_dict = {'CLASS NAME': 'Hunter', 'NAME': 'Jacke'}
    bio = 'Hunters are usually associated with the wisdom of nature. Rangers tend to be wise, hardy, cunning, and perceptive in addition to being skilled woodsmen. Many are skilled in woodcraft, stealth, wilderness survival, beast-mastery, herbalism, tracking, and sometimes "nature magic" or have a resistance to magic.'

    stat_dict = {
        'HP': 20,
        'Mana': 10,
        'XP': 0,
        "LVL": 1,
    }


class Mage(object, BaseCharacter):
    def __init__(self):
        BaseCharacter.__init__(self)
    info_dict = {'CLASS NAME': 'Mage', 'NAME': 'Elendinr'}
    bio = 'Mage is someone who uses or practices magic derived from supernatural or occult sources. Magicians are common figures in works of fantasy, such as fantasy literature and role-playing games, and enjoy a rich history in mythology, legends, fiction, and folklore.'
    stat_dict = {
        'HP': 15,
        'Mana': 25,
        'XP': 0,
        "LVL": 1,
    }
