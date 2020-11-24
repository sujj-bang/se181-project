import os
import pygame
import pygame_menu
#import main

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
surface = pygame.display.set_mode((600, 400))


def set_difficulty(selected, value):
    """
    Set the difficulty of the game.
    """
    print('Set difficulty to {} ({})'.format(selected[0], value))


def start_the_game():
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    print('Run main?')
 #   execfile('main.py')


menu = pygame_menu.Menu(height=300,
                        width=400,
                        theme=pygame_menu.themes.THEME_DARK,
                        title='Welcome')

menu.add_text_input('Name: ', default='John Doe')
menu.add_selector('Difficulty: ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)
