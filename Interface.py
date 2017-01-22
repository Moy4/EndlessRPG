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
            statrect.center = (710, (450 + space_counters))
            gameDisplay.blit(statsurf, statrect)

    def random_screen(self, instanc):
        print "WYBIERAM EKRAN"
        setter = randint(1, 100)
        if setter <= 70:
            self.fighting_screen(instanc)
        elif 70 < setter <= 100:
            self.item_found()

    def traveling_screen(self):
        monster = Monster()
        hero_back = pygame.image.load(self.choosen_hero.back_img)
        displayloop = True
        while displayloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        print "KLIKNALEM w"
                        self.random_screen(monster)
                    elif event.key == pygame.K_a:
                        self.random_screen(monster)
                    elif event.key == pygame.K_d:
                        self.random_screen(monster)
                    elif event.key == pygame.K_i:
                        self.inventory_screen()


            smallText = pygame.font.Font("Pixeled.ttf", 12)
            gameDisplay.fill(black)
            gameDisplay.blit(hud, (0, 400))

            gameDisplay.blit(hero_back, (50, 200))
            firstsurf, firstrect = text_objects("[w] Travel North", smallText, red)
            firstrect.center = (150, 470)
            gameDisplay.blit(firstsurf, firstrect)
            seconfsurf, seconfrect = text_objects("[d] Travel East", smallText, red)
            seconfrect.center = (150, 500)
            gameDisplay.blit(seconfsurf, seconfrect)
            thirdsurf, thirdrect = text_objects("[a] Travel West", smallText, red)
            thirdrect.center = (150, 530)
            gameDisplay.blit(thirdsurf, thirdrect)
            forthsurf, forthrect = text_objects("[i] Inventory", smallText, red)
            forthrect.center = (570, 470)
            gameDisplay.blit(forthsurf, forthrect)
            self.hero_stats(smallText)
            pygame.display.update()

    def mag(self):
        displayloop = True
        while displayloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            winkszy_barb = pygame.image.load(self.choosen_hero.img)
            gameDisplay.blit(winkszy_barb, (500, 100))
            pygame.display.update()

    def fighting_screen(self, monster_class):
        print "Instancje w fightingu:" + str(sys.getrefcount(monster_class))
        if monster_class.attribute_dict["Agility"] > self.choosen_hero.attribute_dict["Agility"]:
            self.monster_strike_first(monster_class)
        else:
            self.monster_encoutered(monster_class)



    def counting_hero_defence(self):
        if len(self.choosen_hero.item_list) != 0:
            for item in self.choosen_hero.item_list:
                if item.name == "Fajna Zbroja ":
                    bonus = item.defense
                    print "bonus oborny: " + str(bonus)
                    return bonus + self.choosen_hero.count_resistance(self.dice)
                else:
                    return self.choosen_hero.attack(self.dice)
        else:
            return self.choosen_hero.attack(self.dice)

    def counting_monster_attack(self, monster):
        displaaayloop = True
        attack_value = monster.attack(self.dice) - self.counting_hero_defence()
        if attack_value <= 0:
            attack_value = 0
        stringvalue = str(attack_value)
        self.choosen_hero.stat_dict["HP"] -= attack_value
        while displaaayloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            gameDisplay.blit(hud, (0, 400))
            hero_back = pygame.image.load(self.choosen_hero.back_img)
            gameDisplay.blit(hero_back, (50, 200))
            smallText = pygame.font.Font("Pixeled.ttf", 10)
            firstsurf, firstrect = text_objects(monster.won_ini, smallText, red)
            firstrect.center = (170, 470)
            gameDisplay.blit(firstsurf, firstrect)
            seconfsurf, seconfrect = text_objects(stringvalue + "dmg", smallText, red)
            seconfrect.center = (130, 500)
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

    def counting_parry(self, monster):
        self.choosen_hero.parry_bonus = 3
        gameDisplay.fill(black)
        gameDisplay.blit(hud, (0, 400))
        smallText = pygame.font.Font("Pixeled.ttf", 10)
        seconfsurfe, seconfrecte = text_objects("Obrona zwieksza sie o 3 na jedna ture!", smallText, red)
        seconfrecte.center = (200, 470)
        gameDisplay.blit(seconfsurfe, seconfrecte)
        pygame.display.update()
        time.sleep(3)
        self.counting_monster_attack(monster)

    def use_potion(self, monster):
        if len(self.choosen_hero.item_list) != 0:
            for item in self.choosen_hero.item_list:
                if item.name == "Mikstura ":
                    if self.choosen_hero.stat_dict["HP"] == self.choosen_hero.const_stat_dict["HP"]:
                        gameDisplay.fill(black)
                        gameDisplay.blit(hud, (0, 400))
                        smallText = pygame.font.Font("Pixeled.ttf", 10)
                        seconfsurfe, seconfrecte = text_objects("Masz maksymalna ilosc zycia", smallText, red)
                        seconfrecte.center = (200, 460)
                        gameDisplay.blit(seconfsurfe, seconfrecte)
                        pygame.display.update()
                        time.sleep(3)
                        self.hero_action(monster)
                    else:
                        self.choosen_hero.item_list.remove(item)
                        hp_difference = self.choosen_hero.const_stat_dict["HP"] - self.choosen_hero.stat_dict["HP"]
                        if hp_difference < 10:
                            print "dodalem tyle: " + str(hp_difference)
                            self.choosen_hero.stat_dict["HP"] += hp_difference
                            gameDisplay.fill(black)
                            gameDisplay.blit(hud, (0, 400))
                            smallText = pygame.font.Font("Pixeled.ttf", 10)
                            seconfsurfe, seconfrecte = text_objects("Leczysz sie o 10 pkt!", smallText, red)
                            seconfrecte.center = (200, 460)
                            gameDisplay.blit(seconfsurfe, seconfrecte)
                            pygame.display.update()
                            time.sleep(3)
                            self.counting_monster_attack(monster)
                        elif hp_difference >= 10:
                            self.choosen_hero.stat_dict["HP"] += 10
                            print "dodalem tyle: 10"
                            gameDisplay.fill(black)
                            gameDisplay.blit(hud, (0, 400))
                            smallText = pygame.font.Font(None, 30)
                            seconfsurfe, seconfrecte = text_objects("Leczysz sie o 10 pkt!", smallText, red)
                            seconfrecte.center = (200, 460)
                            gameDisplay.blit(seconfsurfe, seconfrecte)
                            pygame.display.update()
                            time.sleep(3)
                            self.counting_monster_attack(monster)
                else:
                    gameDisplay.fill(black)
                    gameDisplay.blit(hud, (0, 400))
                    smallText = pygame.font.Font(None, 30)
                    seconfsurfe, seconfrecte = text_objects("Nie masz mikstur!", smallText, red)
                    seconfrecte.center = (200, 460)
                    gameDisplay.blit(seconfsurfe, seconfrecte)
                    pygame.display.update()
                    time.sleep(3)
                    self.hero_action(monster)
        else:
            gameDisplay.fill(black)
            gameDisplay.blit(hud, (0, 400))
            smallText = pygame.font.Font("Pixeled.ttf", 10)
            seconfsurfe, seconfrecte = text_objects("Nie masz mikstur!", smallText, red)
            seconfrecte.center = (200, 460)
            gameDisplay.blit(seconfsurfe, seconfrecte)
            pygame.display.update()
            time.sleep(3)
            self.hero_action(monster)

    def if_flee(self, monster):
        setter = randint(1, 100)
        if setter <= 50:
            gameDisplay.fill(black)
            gameDisplay.blit(hud, (0, 400))
            smallText = pygame.font.Font("Pixeled.ttf", 10)
            seconfsurfe, seconfrecte = text_objects("Nie udalo Ci sie uciec", smallText, red)
            seconfrecte.center = (300, 50)
            monszter = pygame.image.load(monster.monster_img)
            gameDisplay.blit(monszter, (400, 50))
            gameDisplay.blit(seconfsurfe, seconfrecte)
            pygame.display.update()
            time.sleep(3)
            self.counting_monster_attack(monster)
        elif 50 < setter <= 100:
            gameDisplay.fill(black)
            gameDisplay.blit(hud, (0, 400))
            smallText = pygame.font.Font("Pixeled.ttf", 10)
            seconfsurfe, seconfrecte = text_objects("Udalo Ci sie uciec", smallText, red)
            seconfrecte.center = (200, 460)
            gameDisplay.blit(seconfsurfe, seconfrecte)
            pygame.display.update()
            time.sleep(3)
            self.traveling_screen()

    def monster_strike_first(self, monster_class):
        gameDisplay.fill(black)
        gameDisplay.blit(hud, (0, 400))
        smallText = pygame.font.Font("Pixeled.ttf", 15)
        firstsurf, firstrect = text_objects("Monster Attacked You!", smallText, red)
        firstrect.center = (300, 50)
        gameDisplay.blit(firstsurf, firstrect)
        pygame.display.update()
        time.sleep(3)
        self.counting_monster_attack(monster_class)

    def monster_encoutered(self, monster):
        gameDisplay.fill(black)
        gameDisplay.blit(hud, (0, 400))
        smallText = pygame.font.Font("Pixeled.ttf", 15)
        firstsurf, firstrect = text_objects("Monster Encountered, you will strike first!", smallText, red)
        firstrect.center = (300, 50)
        gameDisplay.blit(firstsurf, firstrect)
        pygame.display.update()
        time.sleep(3)
        self.hero_action(monster)

    def hero_action(self, monster):

        self.choosen_hero.parry_bonus = 0
        hero_back = pygame.image.load(self.choosen_hero.back_img)
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
                        self.counting_parry(monster)
                    elif event.key == pygame.K_a:
                        self.if_flee(monster)
                    elif event.key == pygame.K_s:
                        self.use_potion(monster)

            gameDisplay.fill(black)
            gameDisplay.blit(hud, (0, 400))
            gameDisplay.blit(hero_back, (50, 200))
            smallText = pygame.font.Font('Pixeled.ttf', 10)
            firstsurf, firstrect = text_objects("[w] Attack", smallText, red)
            firstrect.center = (130, 470)
            gameDisplay.blit(firstsurf, firstrect)
            seconfsurf, seconfrect = text_objects("[d] Def", smallText, red)
            seconfrect.center = (130, 500)
            gameDisplay.blit(seconfsurf, seconfrect)
            thirdsurf, thirdrect = text_objects("[a] Flee", smallText, red)
            thirdrect.center = (130, 530)
            gameDisplay.blit(thirdsurf, thirdrect)
            fousurf, fourect = text_objects("[s] Use Potion", smallText, red)
            fourect.center = (300, 470)
            gameDisplay.blit(fousurf, fourect)
            self.hero_stats(smallText)
            pygame.display.update()

    def counting_attack(self):
        if len(self.choosen_hero.item_list) != 0:
            for item in self.choosen_hero.item_list:
                if item.name == "Super Miecz ":
                    bonus = item.attack
                    print"bonus ataku: " + str(bonus)
                    return bonus + self.choosen_hero.attack(self.dice)
                else:
                    return self.choosen_hero.attack(self.dice)
        else:
            return self.choosen_hero.attack(self.dice)

    def attacking(self, monster):
        print monster.stat_dict['HP']
        print self.counting_attack()
        attack_value = self.counting_attack()
        stringvalue = str(attack_value)
        monster.stat_dict["HP"] -= attack_value
        print monster.stat_dict['HP']
        gameDisplay.fill(black)
        gameDisplay.blit(hud, (0, 400))
        smallText = pygame.font.Font(None, 30)
        monszter = pygame.image.load(monster.monster_img)
        gameDisplay.blit(monszter, (400, 50))
        hero_back = pygame.image.load(self.choosen_hero.back_img)
        gameDisplay.blit(hero_back, (50, 200))
        firstsurf, firstrect = text_objects(self.choosen_hero.hero_ini, smallText, red)
        firstrect.center = (170, 470)
        gameDisplay.blit(firstsurf, firstrect)
        seconfsurf, seconfrect = text_objects(stringvalue + "dmg", smallText, red)
        seconfrect.center = (130, 500)
        gameDisplay.blit(seconfsurf, seconfrect)
        self.hero_stats(smallText)
        if monster.stat_dict['HP'] <= 0:
            seconfsurfe, seconfrecte = text_objects("Wygrales Walke", smallText, red)
            seconfrecte.center = (130, 540)
            gameDisplay.blit(seconfsurfe, seconfrecte)
            pygame.display.update()
        pygame.display.update()
        time.sleep(3)
        if monster.stat_dict['HP'] > 0:
            self.counting_monster_attack(monster)
        else:
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
            largeText = pygame.font.Font('Pixeled.ttf', 20)
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
            smallText = pygame.font.Font('Pixeled.ttf', 12)
            meciumText = pygame.font.Font('Pixeled.ttf', 17)
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
            hero_portret = pygame.image.load(self.choosen_hero.img)
            gameDisplay.blit(hero_portret, (400, 100))
            textSurf, textRect = text_objects(str(self.choosen_hero.lvl_points), smallText, red)
            textRect.center = (190, 550)
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects('Points: ', meciumText, red)
            textRect.center = (120, 550)
            gameDisplay.blit(textSurf, textRect)

            pygame.display.update()

    def random_item(self):
        print "DUUUUPAAAA"
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

    # def bag_options(self, instance):
    #     choose = True
    #     while choose:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 quit()
    #         gameDisplay.fill(black)
    #         smallText = pygame.font.Font('OldLondon.ttf', 30)
    #         textSurf, textRect = text_objects("You'v found Item! But you have similar ", smallText, red)
    #         textRect.center = (200, 100)
    #         gameDisplay.blit(textSurf, textRect)
    #         secSurf, secRect = text_objects(instance.name, smallText, red)
    #         secRect.center = (200, 450)
    #         gameDisplay.blit(secSurf, secRect)
    #         thiSurf, thiRect = text_objects(instance.info, smallText, red)
    #         thiRect.center = (200, 500)
    #         gameDisplay.blit(thiSurf, thiRect)
    #         button("Drop", 500, 530, 100, 50, black, dark_gray, self.traveling_screen)
    #         start_button("Equip", 600, 530, 100, 50, black, dark_gray, instance, self.equip_item)
    #
    #         text2Surf, text2Rect = text_objects("In Your Bag: ", smallText, red)
    #         text2Rect.center = (600, 100)
    #         gameDisplay.blit(text2Surf, text2Rect)
    #         sec2Surf, sec2Rect = text_objects(instance.name, smallText, red)
    #         sec2Rect.center = (600, 450)
    #         gameDisplay.blit(sec2Surf, sec2Rect)
    #         thi2Surf, thi2Rect = text_objects(instance.info, smallText, red)
    #         thiRect.center = (600, 500)
    #         gameDisplay.blit(thi2Surf, thi2Rect)
    #         pygame.display.update()
    #
    # def bag_checker(self, instance):
    #     if self.choosen_hero.item_list != 0:
    #         if any(isinstance(item, Sword) == isinstance(instance, Sword) for item in self.choosen_hero.item_list):
    #             self.bag_options(instance)
    #         elif any(isinstance(item, Armor) == isinstance(instance, Armor) for item in self.choosen_hero.item_list):
    #             self.bag_options(instance)
    #         else:
    #             self.equip_item(instance)
    #     else:
    #         self.equip_item(instance)
    #
    # def equip_item(self, instance):
    #     self.choosen_hero.item_list.append(instance)
    #     self.traveling_screen()

    def item_found(self):
        item_loop = True
        item = self.random_item()
        self.choosen_hero.item_list.append(item)
        if len(self.choosen_hero.item_list) == 6:
            self.removing_inventory_screen()
        while item_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            smallText = pygame.font.Font('Pixeled.ttf', 15)
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
                button("Equip", 680, 20, 100, 50, black, dark_gray, self.traveling_screen)
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
                button("Equip", 680, 20, 100, 50, black, dark_gray, self.traveling_screen)
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
                button("Equip", 680, 20, 100, 50, black, dark_gray, self.traveling_screen)
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
                start_button(row, 20, (20 + space_down), 400, 50, black, dark_gray, item, self.single_item_options)
            pygame.display.update()

    def single_item_options(self, item):
        item_loop = True
        item = item
        if len(self.choosen_hero.item_list) == 6:
            self.removing_inventory_screen()
        while item_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            smallText = pygame.font.Font('Pixeled.ttf', 15)

            if item.name == "Super Miecz ":
                secSurf, secRect = text_objects(item.name, smallText, red)
                secRect.center = (400, 350)
                gameDisplay.blit(secSurf, secRect)
                thiSurf, thiRect = text_objects(item.info, smallText, red)
                thiRect.center = (400, 400)
                gameDisplay.blit(thiSurf, thiRect)
                button("Equip", 200, 450, 100, 50, black, dark_gray, self.traveling_screen)
                start_button("Drop", 300, 450, 100, 50, black, dark_gray, item,  self.removing_element)
                pygame.display.update()

            elif item.name == "Fajna Zbroja ":
                secSurf, secRect = text_objects(item.name, smallText, red)
                secRect.center = (400, 350)
                gameDisplay.blit(secSurf, secRect)
                thiSurf, thiRect = text_objects(item.info, smallText, red)
                thiRect.center = (400, 400)
                gameDisplay.blit(thiSurf, thiRect)
                button("Equip", 200, 450, 100, 50, black, dark_gray, self.traveling_screen)
                start_button("Drop", 300, 450, 100, 50, black, dark_gray, item,  self.removing_element)
                pygame.display.update()

            elif item.name == "Mikstura ":
                secSurf, secRect = text_objects(item.name, smallText, red)
                secRect.center = (400, 350)
                gameDisplay.blit(secSurf, secRect)
                thiSurf, thiRect = text_objects(item.info, smallText, red)
                thiRect.center = (400, 400)
                gameDisplay.blit(thiSurf, thiRect)
                button("Equip", 200, 450, 100, 50, black, dark_gray, self.traveling_screen)
                start_button("Drop", 300, 450, 100, 50, black, dark_gray, item, self.removing_element)
                pygame.display.update()

    def removing_inventory_screen(self):
        inv_loop = True
        while inv_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            if len(self.choosen_hero.item_list) < 6:
                button("Back", 680, 20, 100, 50, black, dark_gray, self.traveling_screen)
            space_down = 0

            print self.choosen_hero.item_list
            for item in self.choosen_hero.item_list:
                space_down += 70
                row = str(item.name + item.info)
                button(row, 40, (20 + space_down), 400, 50, black, dark_gray, self.traveling_screen)
                start_button("Drop", 400, (20+space_down), 100, 50, black, dark_gray, item, self.removing_element)
            pygame.display.update()

    def removing_element(self, item):
        self.choosen_hero.item_list.remove(item)
        self.traveling_screen()

    def items_action(self):
        item_loop = True
        while item_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
        button("Destroy", 550, 450, 100, 50, black, dark_gray, self.traveling_screen)
        button("Equip", 150, 450, 100, 50, black, dark_gray, self.traveling_screen)