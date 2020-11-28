import os
import pygame
import pygame_menu
#import main
from main import run
from credits import credits


pygame.display.set_caption('Checkers')
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
surface = pygame.display.set_mode((800, 600))


def set_difficulty(selected, value):
    """
    Set the difficulty of the game.
    """
    print('Set game mode to {} ({})'.format(selected[0], value))


def start_the_game():
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    print('Run main?')
    run()
#    execfile('main.py')


def show_credits():

    print("Display Credits")
    credits()
#    execfile('credits.py')


menu = pygame_menu.Menu(height=600,
                        width=800,
                        theme=pygame_menu.themes.THEME_DARK,
                        title='Welcome')

menu.add_text_input('Name: ', default='Enter Name Here')
menu.add_selector('Game Mode: ', [('Single Player', 1), ('Multiplayer', 2)], onchange=set_difficulty)
menu.add_button('Play', start_the_game)
menu.add_button('Credits', show_credits)
menu.add_button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)
