import os
import pygame
import pygame_menu
from checkers.constants import WIDTH, HEIGHT
from main import run
from credits import credits

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers Menu")


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
    print('Running main')
    run()


#    execfile('main.py')


def show_credits():
    print("Display Credits")
    credits()


#    execfile('credits.py')


menu = pygame_menu.Menu(height=HEIGHT,
                        width=WIDTH,
                        theme=pygame_menu.themes.THEME_DARK,
                        title='Welcome to Checkers')

menu.add_text_input('Name: ', default='Enter Name Here')
menu.add_button('Play', start_the_game)
menu.add_button('Credits', show_credits)
menu.add_button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)
