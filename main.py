import time

from base_class import *
from static_settings import *
from Interface import Interface


class Main:

    def minus_attr(self, instance, value):
        time.sleep(0.25)
        if instance.const_dict[value] == instance.attribute_dict[value]:
            allow_flag = False
        else:
            allow_flag = True

        if allow_flag and instance.attribute_points != 10:
            instance.attribute_dict[value] -= 1
            instance.attribute_points += 1

    def plus_attr(self, instance, value):
        time.sleep(0.25)
        if instance.attribute_points != 0:
            allow_flag = True
        else:
            allow_flag = False
        if allow_flag:
            instance.attribute_points -= 1
            instance.attribute_dict[value] += 1

    def start_game(self, hero_instance):
        hero_instance.const_dict = hero_instance.attribute_dict.copy()
        Interface(hero_instance).traveling_screen()

    def mage_hero(self):
        """
        First Playable Character class, all of them
        should be unified and generalize TODO in further
        development
        """
        mage = Mage()
        choose = True
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
            for field, value in mage.attribute_dict.items():
                space_counter += 70
                add_button("<", 7, (10 + space_counter), 25, 25, black, dark_gray, mage, field, self.minus_attr)
                add_button(">", 190, (10 + space_counter), 25, 25, black, dark_gray, mage, field, self.plus_attr)
                row = field, str(value)

                makelist = list(row)
                makestring = ': '.join(makelist)
                textSurf, textRect = text_objects(makestring, smallText, red)
                textRect.center = (80, (22 + space_counter))
                gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects('Hero Info', meciumText, red)
            textRect.center = (250, 40)
            gameDisplay.blit(textSurf, textRect)
            space_counter = 0
            for field, value in mage.info_dict.items():
                space_counter += 30
                row = field, str(value)
                makelist = list(row)
                makestring = ': '.join(makelist)
                textSurf, textRect = text_objects(makestring, smallText, red)
                textRect.center = (340, (60 + space_counter))
                gameDisplay.blit(textSurf, textRect)
            bio = wrapline(mage.bio,font,500)
            textSurf, textRect = text_objects('BIO:', smallText, red)
            textRect.center = (240, 150)
            gameDisplay.blit(textSurf, textRect)
            for i in bio:
                space_counter += 20
                textSurf, textRect = text_objects(i, smallText, red)
                textRect.center = (440, (70 + space_counter))
                gameDisplay.blit(textSurf, textRect)
            start_button("Play", display_width/2, 450, 100, 50, black, dark_gray, mage, self.start_game)
            button("Back", 680, 20, 100, 50, black, dark_gray, self.choose_hero)
            textSurf, textRect = text_objects(str(mage.attribute_points), smallText, red)
            textRect.center = (190, 550)
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects('Points: ', meciumText, red)
            textRect.center = (120, 550)
            gameDisplay.blit(textSurf, textRect)
            pygame.display.update()

    def hunter_hero(self):
        hunter = Hunter()
        choose = True
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
            for field, value in hunter.attribute_dict.items():
                space_counter += 70
                add_button("<", 7, (10 + space_counter), 25, 25, black, dark_gray, hunter, field, self.minus_attr)
                add_button(">", 190, (10 + space_counter), 25, 25, black, dark_gray, hunter, field, self.plus_attr)
                row = field, str(value)
                makelist = list(row)
                makestring = ': '.join(makelist)
                textSurf, textRect = text_objects(makestring, smallText, red)
                textRect.center = (110, (22 + space_counter))
                gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects('Hero Info', meciumText, red)
            textRect.center = (290, 40)
            gameDisplay.blit(textSurf, textRect)
            space_counter = 0
            for field, value in hunter.info_dict.items():
                space_counter += 30
                row = field, str(value)
                makelist = list(row)
                makestring = ': '.join(makelist)
                textSurf, textRect = text_objects(makestring, smallText, red)
                textRect.center = (370, (60 + space_counter))
                gameDisplay.blit(textSurf, textRect)
            bio = wrapline(hunter.bio, font, 500)
            textSurf, textRect = text_objects('BIO:', smallText, red)
            textRect.center = (270, 150)
            gameDisplay.blit(textSurf, textRect)
            for i in bio:
                space_counter += 25
                textSurf, textRect = text_objects(i, smallText, red)
                textRect.center = (510, (70 + space_counter))
                gameDisplay.blit(textSurf, textRect)
            start_button("Play", display_width/2, 450, 100, 50, black, dark_gray, hunter, self.start_game)
            button("Back", 680, 20, 100, 50, black, dark_gray, self.choose_hero)
            textSurf, textRect = text_objects(str(hunter.attribute_points), smallText, red)
            textRect.center = (190, 550)
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects('Points: ', meciumText, red)
            textRect.center = (120, 550)
            gameDisplay.blit(textSurf, textRect)
            pygame.display.update()

    def barb_hero(self):
        barb = Barbarian()
        choose = True
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
            for field, value in barb.attribute_dict.items():
                space_counter += 70
                add_button("<", 7, (10 + space_counter), 25, 25, black, dark_gray, barb, field, self.minus_attr)
                add_button(">", 190, (10 + space_counter), 25, 25, black, dark_gray, barb, field, self.plus_attr)
                row = field, str(value)
                makelist = list(row)
                makestring = ': '.join(makelist)
                textSurf, textRect = text_objects(makestring, smallText, red)
                textRect.center = (80, (22 + space_counter))
                gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects('Hero Info', meciumText, red)
            textRect.center = (320, 40)
            gameDisplay.blit(textSurf, textRect)
            space_counter = 0
            for field, value in barb.info_dict.items():
                space_counter += 30
                row = field, str(value)
                makelist = list(row)
                makestring = ': '.join(makelist)
                textSurf, textRect = text_objects(makestring, smallText, red)
                textRect.center = (365, (60 + space_counter))
                gameDisplay.blit(textSurf, textRect)
            bio = wrapline(barb.bio,font,500)
            textSurf, textRect = text_objects('BIO:', smallText, red)
            textRect.center = (250, 150)
            gameDisplay.blit(textSurf, textRect)
            for i in bio:
                space_counter += 20
                textSurf, textRect = text_objects(i, smallText, red)
                textRect.center = (420, (70 + space_counter))
                gameDisplay.blit(textSurf, textRect)
            start_button("Play", display_width/2, 450, 100, 50, black, dark_gray, barb, self.start_game)
            button("Back", 680, 20, 100, 50, black, dark_gray, self.choose_hero)
            textSurf, textRect = text_objects(str(barb.attribute_points), smallText, red)
            textRect.center = (190, 550)
            gameDisplay.blit(textSurf, textRect)
            textSurf, textRect = text_objects('Points: ', meciumText, red)
            textRect.center = (120, 550)
            gameDisplay.blit(textSurf, textRect)
            pygame.display.update()

    def choose_hero(self):
        """
        Screen where you can chose hero
        """
        choose = True
        while choose:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            smallText = pygame.font.Font('OldLondon.ttf', 60)
            TextSurf, TextRect = text_objects("Choose Hero", smallText, red)
            TextRect.center = (400, 50)
            gameDisplay.blit(TextSurf, TextRect)
            button("Barbarian", 350, 150, 100, 50, black, dark_gray, self.barb_hero)
            button("Hunter", 350, 250, 100, 50, black, dark_gray, self.hunter_hero)
            button("Mage", 350, 350, 100, 50, black, dark_gray, self.mage_hero)
            button("Back", 350, 450, 100, 50, black, dark_gray, self.game_intro)
            pygame.display.update()

    def quitgame(self):
        """
        Function allowing to quit game with button action
        """
        pygame.quit()
        quit()

    def game_intro(self):
        """
        First called function all while for if loops
        are very repetetive, must be refactored in
        further development
        """
        intor = True
        while intor:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(black)
            largeText = pygame.font.Font('OldLondon.ttf',115)
            TextSurf, TextRect = text_objects('Endless Story', largeText, red)
            TextRect.center = ((display_width/2),(70))
            gameDisplay.blit(titleImg, (175, 150))
            gameDisplay.blit(TextSurf, TextRect)
            button("Play", 150, 450, 100, 50, black, dark_gray, self.choose_hero)
            button("Quit", 550, 450, 100, 50, black, dark_gray, self.quitgame)
            pygame.display.update()

    def game_loop(self):

        """
        In further development this function will be
        main, calling all other function
        For now this function is not in use
        """

        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
            gameDisplay.fill(black)
            pygame.display.update()

