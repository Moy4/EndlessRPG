from random import randint

from monster_class import Monster
from dice_class import Dice
from static_settings import *


class Interface:
    """
    This class will contain three major screens
    First One: Traveling Screen
    Second One: Fight Screen
    Third One:
    """

    def __init__(self, instance):
        self.choosen_hero = instance

    def display_text_animation(self, string, dupa):
        """
        For now this function is not in use
        maybe it will be used further in front end develeopment
        """
        text = ''
        while dupa:
            for i in range(len(string)):
                print i
                gameDisplay.fill(white)
                text += string[i]
                print text
                text_surface = font.render(text, True, black)
                text_rect = text_surface.get_rect()
                text_rect.center = (display_width/2, display_height/2)
                gameDisplay.blit(text_surface, text_rect)
                pygame.display.update()
                pygame.time.wait(200)
                if i == len(string)-1:
                    self.dupa = False

    def traveling_screen(self):
        displayloop = True
        while displayloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or pygame.K_a or pygame.K_d:
                        setter = randint(0, 99)
                        if setter <= 33:
                            self.fighting_screen()
                        if 33 < setter <= 66:
                            self.fighting_screen()
                        if setter > 66:
                            self.fighting_screen()

            smallText = pygame.font.Font(None, 30)
            gameDisplay.fill(black)
            pygame.draw.rect(gameDisplay, white, (0, 400, 800, 200))
            firstsurf, firstrect = text_objects("Press w to: Travel North", smallText, red)
            firstrect.center = (130, 430)
            gameDisplay.blit(firstsurf, firstrect)
            seconfsurf, seconfrect = text_objects("Press d to: Travel East", smallText, red)
            seconfrect.center = (122, 460)
            gameDisplay.blit(seconfsurf, seconfrect)
            thirdsurf, thirdrect = text_objects("Press a to: Travel West", smallText, red)
            thirdrect.center = (126, 490)
            gameDisplay.blit(thirdsurf, thirdrect)
            space_counters = 0
            for field, value in self.choosen_hero.stat_dict.iteritems():
                space_counters += 20
                row = field, str(value)
                makelist = list(row)
                makestring = ': '.join(makelist)
                statsurf, statrect = text_objects(makestring, smallText, red)
                statrect.center = (750, (400 + space_counters))
                gameDisplay.blit(statsurf, statrect)
            pygame.display.update()

    def fighting_screen(self):
        print "figthing screen"
        dice_instance = Dice()
        monster_class = Monster()
        if monster_class.attribute_dict["Agility"] > self.choosen_hero.attribute_dict["Agility"]:
            self.counting_monster_attack(monster_class, self.choosen_hero, dice_instance)
        else:
            self.hero_acttion()

    def counting_monster_attack(self, monster, hero, dice):
        print "wywolalem"
        displaaayloop = True
        attack_value = monster.attack(dice)
        stringvalue = str(attack_value)
        hero.stat_dict["HP"] -= attack_value
        while displaaayloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            pygame.draw.rect(gameDisplay, white, (0, 400, 800, 200))
            smallText = pygame.font.Font(None, 30)
            firstsurf, firstrect = text_objects(monster.won_ini, smallText, red)
            firstrect.center = (130, 430)
            gameDisplay.blit(firstsurf, firstrect)
            seconfsurf, seconfrect = text_objects(stringvalue + "dmg", smallText, red)
            seconfrect.center = (122, 460)
            gameDisplay.blit(seconfsurf, seconfrect)
            space_counters = 0
            for field, value in self.choosen_hero.stat_dict.iteritems():
                space_counters += 20
                row = field, str(value)
                makelist = list(row)
                makestring = ': '.join(makelist)
                statsurf, statrect = text_objects(makestring, smallText, red)
                statrect.center = (750, (400 + space_counters))
                gameDisplay.blit(statsurf, statrect)
            pygame.display.update()

    def hero_acttion(self):
        print "hero action"
        displaaaayloop = True
        while displaaaayloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        print "dupa"
                    elif event.key == pygame.K_a:
                        print "sraka"
                    elif event.key == pygame.K_d:
                        print "dupaka"
            gameDisplay.fill(black)
            pygame.draw.rect(gameDisplay, white, (0, 400, 800, 200))
            smallText = pygame.font.Font(None, 30)
            firstsurf, firstrect = text_objects("a) Attack", smallText, red)
            firstrect.center = (130, 430)
            gameDisplay.blit(firstsurf, firstrect)
            seconfsurf, seconfrect = text_objects("b) Def", smallText, red)
            seconfrect.center = (122, 460)
            gameDisplay.blit(seconfsurf, seconfrect)
            thirdsurf, thirdrect = text_objects("c) RUN!", smallText, red)
            thirdrect.center = (126, 490)
            gameDisplay.blit(thirdsurf, thirdrect)
            pygame.display.update()

