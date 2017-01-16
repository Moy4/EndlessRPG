import pygame
from itertools import chain

"""
Base Settings for my pygame App
"""


display_width = 800
display_height = 600
red = (183, 38, 38)
bright_red = (200, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
dark_gray = (32, 32, 32)
FPS = 30
clock = pygame.time.Clock()


pygame.init()

start_sound = pygame.mixer.Sound("questdone.wav")
button_sound = pygame.mixer.Sound("select.wav")

# pygame.mixer.music.stop()
# pygame.mixer.Sound.play(start_sound)
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SebaRPG')
font = pygame.font.Font('OldLondon.ttf', 36)
titleImg = pygame.image.load('newdevil.png')


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    """
    Almost general button class
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action:
            # pygame.mixer.music.stop()
            # pygame.mixer.Sound.play(button_sound)
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font('Deutsch.ttf',27)
    textSurf, textRect = text_objects(msg, smallText, red)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def start_button(msg, x, y, w, h, ic, ac, acion_arg, action=None):
    """
    Start Button used once to pass choosen instance
    to next stage of game
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action:
            # pygame.mixer.music.stop()
            # pygame.mixer.Sound.play(button_sound)
            action(acion_arg)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.Font('Deutsch.ttf',27)
    textSurf, textRect = text_objects(msg, smallText, red)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def add_button(msg, x, y, w, h, ic, ac, acion_arg, action_arg, action=None):
    """
    Start Button used once to pass choosen instance
    to next stage of game
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action:
            # pygame.mixer.music.stop()
            # pygame.mixer.Sound.play(button_sound)
            action(acion_arg, action_arg)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.Font('Deutsch.ttf',27)
    textSurf, textRect = text_objects(msg, smallText, red)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def truncline(text, font, maxwidth):
        real = len(text)
        stext = text
        l=font.size(text)[0]
        cut = 0
        a = 0
        done = 1
        old = None
        while l > maxwidth:
            a = a + 1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l = font.size(stext)[0]
            real = len(stext)
            done = 0
        return real, done, stext


def wrapline(text, font, maxwidth):
    done=0
    wrapped=[]

    while not done:
        nl, done, stext=truncline(text, font, maxwidth)
        wrapped.append(stext.strip())
        text=text[nl:]
    return wrapped


def wrap_multi_line(text, font, maxwidth):
    """
    Returns text taking new lines into account.
    """
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)