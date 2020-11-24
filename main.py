import pygame
from network import Network
from checkers.constants import *
from checkers.board import *
from checkers.game import Game

FPS = 60


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player+1)

    while run:
        clock.tick(FPS)
        try:
            game = n.send("get")
        except:
            run = False
            print("Game could not be created")
            break

        # change winning text
        if game.winner() is not None:
            print(game.winner())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                try:
                    game = n.send(str(row + "," + col))
                except:
                    print() # error message for not being able to choose a position

        game.update() # changes this so game = n.send("update")

    pygame.quit()


main()
