from random import randint
import time
import sys

from item_class import Sword, Armor, Potion
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

    def minus_lvl_up(self, ins, value, ):
        time.sleep(0.25)
        if self.choosen_hero.const_dict[value] == self.choosen_hero.attribute_dict[value]:
            allow_flag = False
        else:
            allow_flag = True

        if allow_flag and self.choosen_hero.lvl_points != 3:
            self.choosen_hero.attribute_dict[value] -= 1
            self.choosen_hero.lvl_points += 1

    def plus_lvl_up(self, ins, value):
        time.sleep(0.25)
        if self.choosen_hero.lvl_points != 0:
            allow_flag = True
        else:
            allow_flag = False
        if allow_flag:
            self.choosen_hero.lvl_points -= 1
            self.choosen_hero.attribute_dict[value] += 1

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

    def random_screen(self, instanc):
        setter = randint(1, 100)
        if setter <= 70:
            self.fighting_screen(instanc)
        elif setter > 30:
            self.item_found()

    def traveling_screen(self):
        monster = Monster()
        print "Instancje w Travelingu:" + str(sys.getrefcount(monster))
        displayloop = True
        setter = randint(0, 99)
        while displayloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.random_screen(monster)
                    elif event.key == pygame.K_a:
                        self.random_screen(monster)
                    elif event.key == pygame.K_d:
                        self.random_screen(monster)
                    elif event.key == pygame.K_i:
                        self.inventory_screen()


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
            forthsurf, forthrect = text_objects("[i] Inventory", smallText, red)
            forthrect.center = (740, 500)
            gameDisplay.blit(forthsurf, forthrect)
            self.hero_stats(smallText)
            pygame.display.update()

    def fighting_screen(self, monster_class):

        print "Instancje w fightingu:" + str(sys.getrefcount(monster_class))
        if monster_class.attribute_dict["Agility"] > self.choosen_hero.attribute_dict["Agility"]:
            self.counting_monster_attack(monster_class)
        else:
            self.hero_action(monster_class)

    def counting_monster_attack(self, monster):
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
                del self.choosen_hero
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
        attack_value = self.choosen_hero.attack(self.dice)
        stringvalue = str(attack_value)
        monster.stat_dict["HP"] -= attack_value
        print monster.stat_dict['HP']
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
        if monster.stat_dict['HP'] <= 0:
            seconfsurfe, seconfrecte = text_objects("Wygrales Walke", smallText, red)
            seconfrecte.center = (122, 460)
            gameDisplay.blit(seconfsurfe, seconfrecte)
            pygame.display.update()
        pygame.display.update()
        time.sleep(3)
        print monster
        if monster.stat_dict['HP'] > 0:
            self.counting_monster_attack(monster)
        else:
            print "TYLE JEST TYCH KUREW:" + str(sys.getrefcount(monster))
            del monster
            self.choosen_hero.stat_dict['XP'] += 25
            if self.choosen_hero.stat_dict['XP'] == 100:
                self.lvl_up()
            else:
                self.traveling_screen()

    def on_losing(self):
        from main import Main
        main = Main()
        dupsztal = True
        while dupsztal:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
            gameDisplay.fill(black)
            largeText = pygame.font.Font('OldLondon.ttf', 80)
            TextSurf, TextRect = text_objects('You Lose! Start Again?', largeText, red)
            TextRect.center = ((display_width/2), (70))
            gameDisplay.blit(titleImg, (175, 150))
            gameDisplay.blit(TextSurf, TextRect)
            button("Start Again", 150, 450, 150, 50, black, dark_gray, main.choose_hero)
            button("Quit", 550, 450, 100, 50, black, dark_gray, main.quitgame)
            pygame.display.update()

    def lvl_up(self):
        choose = True
        self.choosen_hero.lvl_points = 3
        self.choosen_hero.stat_dict["LVL"] += 1
        self.choosen_hero.stat_dict["XP"] = 0
        while choose:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            pygame.draw.rect(gameDisplay, black, (20, 20, 760, 560))
            smallText = pygame.font.Font('OldLondon.ttf', 30)
            meciumText = pygame.font.Font('OldLondon.ttf', 40)
            textSurf, textRect = text_objects('Statistics', meciumText, red)
            textRect.center = (80, 40)
            gameDisplay.blit(textSurf, textRect)
            space_counter = 0
            for field, value in self.choosen_hero.attribute_dict.items():
                space_counter += 70
                add_button("<", 7, (10 + space_counter), 25, 25, black, dark_gray, self.choosen_hero, field, self.minus_lvl_up)
                add_button(">", 190, (10 + space_counter), 25, 25, black, dark_gray, self.choosen_hero, field, self.plus_lvl_up)
                row = field, str(value)
                makelist = list(row)
                makestring = ': '.join(makelist)
                textSurf, textRect = text_objects(makestring, smallText, red)
                textRect.center = (110, (22 + space_counter))
                gameDisplay.blit(textSurf, textRect)
            button("Apply", 680, 20, 100, 50, black, dark_gray, self.traveling_screen)
            textSurf, textRect = text_objects(str(self.choosen_hero.lvl_points), smallText, red)
            textRect.center = (190, 550)
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects('Points: ', meciumText, red)
            textRect.center = (120, 550)
            gameDisplay.blit(textSurf, textRect)
            gameDisplay.blit(lvl_upImg, (400, 300))

            pygame.display.update()

    def random_item(self):
        armor = Armor()
        sword = Sword()
        potion = Potion()
        setter = randint(1, 100)
        print "taki roll na item: "
        print setter

        if setter <= 30:
            return sword
        elif 30 < setter < 60:
            return armor
        elif setter >= 60:
            return potion

    def item_found(self):
        item_loop = True
        item = self.random_item()
        self.choosen_hero.item_list.append(item)
        while item_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            smallText = pygame.font.Font('OldLondon.ttf', 30)
            if item.name == "Super Miecz ":
                textSurf, textRect = text_objects("You'v found Sword!", smallText, red)
                textRect.center = (400, 100)
                gameDisplay.blit(textSurf, textRect)
                secSurf, secRect = text_objects(item.name, smallText, red)
                secRect.center = (400, 450)
                gameDisplay.blit(secSurf, secRect)
                thiSurf, thiRect = text_objects(item.info, smallText, red)
                thiRect.center = (400, 500)
                gameDisplay.blit(thiSurf, thiRect)
                button("Apply", 680, 20, 100, 50, black, dark_gray, self.traveling_screen)
                pygame.display.update()

            elif item.name == "Fajna Zbroja ":
                textSurf, textRect = text_objects("You'v found Armor!", smallText, red)
                textRect.center = (400, 100)
                gameDisplay.blit(textSurf, textRect)
                secSurf, secRect = text_objects(item.name, smallText, red)
                secRect.center = (400, 450)
                gameDisplay.blit(secSurf, secRect)
                thiSurf, thiRect = text_objects(item.info, smallText, red)
                thiRect.center = (400, 500)
                gameDisplay.blit(thiSurf, thiRect)
                button("Apply", 680, 20, 100, 50, black, dark_gray, self.traveling_screen)
                pygame.display.update()

            elif item.name == "Mikstura ":
                textSurf, textRect = text_objects("You'v found Potion!", smallText, red)
                textRect.center = (400, 100)
                gameDisplay.blit(textSurf, textRect)
                secSurf, secRect = text_objects(item.name, smallText, red)
                secRect.center = (400, 450)
                gameDisplay.blit(secSurf, secRect)
                thiSurf, thiRect = text_objects(item.info, smallText, red)
                thiRect.center = (400, 500)
                gameDisplay.blit(thiSurf, thiRect)
                button("Apply", 680, 20, 100, 50, black, dark_gray, self.traveling_screen)
                pygame.display.update()

    def inventory_screen(self):
        inv_loop = True
        while inv_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            button("Back", 680, 20, 100, 50, black, dark_gray, self.traveling_screen)
            space_down = 0
            for item in self.choosen_hero.item_list:
                space_down += 70
                row = str(item.name + item.info)
                button(row, 20, (20 + space_down), 400, 50, black, dark_gray, self.traveling_screen)
            pygame.display.update()
