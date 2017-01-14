from random import randint
import time
import gc
import sys

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
        self.dice = Dice()

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

    def hero_stats(self, text):
        space_counters = 0
        for field, value in self.choosen_hero.stat_dict.iteritems():
            space_counters += 20
            row = field, str(value)
            makelist = list(row)
            makestring = ': '.join(makelist)
            statsurf, statrect = text_objects(makestring, text, red)
            statrect.center = (750, (400 + space_counters))
            gameDisplay.blit(statsurf, statrect)

    def traveling_screen(self):

        monster = Monster()
        print "Instancje w Travelingu:" + str(sys.getrefcount(monster))
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
                            self.fighting_screen(monster)
                            del monster
                        if 33 < setter <= 66:
                            self.fighting_screen(monster)
                        if setter > 66:
                            self.fighting_screen(monster)

            smallText = pygame.font.Font(None, 30)
            gameDisplay.fill(black)
            pygame.draw.rect(gameDisplay, white, (0, 400, 800, 200))
            firstsurf, firstrect = text_objects("[w] Travel North", smallText, red)
            firstrect.center = (130, 430)
            gameDisplay.blit(firstsurf, firstrect)
            seconfsurf, seconfrect = text_objects("[d] Travel East", smallText, red)
            seconfrect.center = (122, 460)
            gameDisplay.blit(seconfsurf, seconfrect)
            thirdsurf, thirdrect = text_objects("[a] Travel West", smallText, red)
            thirdrect.center = (126, 490)
            gameDisplay.blit(thirdsurf, thirdrect)
            self.hero_stats(smallText)
            pygame.display.update()

    def fighting_screen(self, monster_class):

        print "Instancje w fightingu:" + str(sys.getrefcount(monster_class))
        if monster_class.attribute_dict["Agility"] > self.choosen_hero.attribute_dict["Agility"]:
            self.counting_monster_attack(monster_class)
        else:
            self.hero_action(monster_class)

    def counting_monster_attack(self, monster):

        print "Instancje w monster action:" + str(sys.getrefcount(monster))
        displaaayloop = True
        attack_value = monster.attack(self.dice) - self.choosen_hero.count_resistance(self.dice)
        stringvalue = str(attack_value)
        self.choosen_hero.stat_dict["HP"] -= attack_value
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
            self.hero_stats(smallText)
            pygame.display.update()
            time.sleep(3)
            if self.choosen_hero.stat_dict['HP'] <= 0:
                print "Instancje Hero przy przegranej:" + str(sys.getrefcount(self.choosen_hero))
                self.on_losing()
            else:
                self.hero_action(monster)

    def hero_action(self, monster):
        print "Instancje w hero action:" + str(sys.getrefcount(monster))
        displaaaayloop = True
        while displaaaayloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.attacking(monster)
                    elif event.key == pygame.K_d:
                        print "sraka"
                    elif event.key == pygame.K_a:
                        print "dupaka"
            gameDisplay.fill(black)
            pygame.draw.rect(gameDisplay, white, (0, 400, 800, 200))
            smallText = pygame.font.Font(None, 30)
            firstsurf, firstrect = text_objects("[w] Attack", smallText, red)
            firstrect.center = (130, 430)
            gameDisplay.blit(firstsurf, firstrect)
            seconfsurf, seconfrect = text_objects("[d] Def", smallText, red)
            seconfrect.center = (122, 460)
            gameDisplay.blit(seconfsurf, seconfrect)
            thirdsurf, thirdrect = text_objects("[a] RUN!", smallText, red)
            thirdrect.center = (126, 490)
            gameDisplay.blit(thirdsurf, thirdrect)
            self.hero_stats(smallText)
            pygame.display.update()

    def attacking(self, monster):
        print "Instancje attackingu " + str(sys.getrefcount(monster))
        print monster.stat_dict['HP']
        print monster
        attack_value = self.choosen_hero.attack(self.dice)
        stringvalue = str(attack_value)
        monster.stat_dict["HP"] -= attack_value
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, white, (0, 400, 800, 200))
        smallText = pygame.font.Font(None, 30)
        firstsurf, firstrect = text_objects(self.choosen_hero.hero_ini, smallText, red)
        firstrect.center = (130, 430)
        gameDisplay.blit(firstsurf, firstrect)
        seconfsurf, seconfrect = text_objects(stringvalue + "dmg", smallText, red)
        seconfrect.center = (122, 460)
        gameDisplay.blit(seconfsurf, seconfrect)
        self.hero_stats(smallText)
        pygame.display.update()
        time.sleep(3)
        print monster
        if monster.stat_dict['HP'] > 0:
            self.counting_monster_attack(monster)
        else:
            print "TYLE JEST TYCH KUREW:" + str(sys.getrefcount(monster))
            del monster
            self.choosen_hero.stat_dict['XP'] += 25
            self.traveling_screen()

    def on_losing(self):
        from main import Main
        del self.choosen_hero
        dupsztal = True
        while dupsztal:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
            gameDisplay.fill(black)
            largeText = pygame.font.Font('OldLondon.ttf', 115)
            TextSurf, TextRect = text_objects('You Lose! Start Again?', largeText, red)
            TextRect.center = ((display_width/2), (70))
            gameDisplay.blit(titleImg, (175, 150))
            gameDisplay.blit(TextSurf, TextRect)
            button("Start Again", 150, 450, 100, 50, black, dark_gray, Main.choose_hero)
            button("Quit", 550, 450, 100, 50, black, dark_gray, Main.quitgame)
            pygame.display.update()
