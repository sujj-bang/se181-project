import pygame
from network import Network
from checkers.constants import *
from checkers.board import *
# from checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def run():
    run = True
    clock = pygame.time.Clock()
    # game = Game()
    n = Network()
    player = int(n.getP())
    print("You are player ", player+1)

    while run:
        clock.tick(FPS)

        try:
            game = n.send("get")
        except:
            run = False
            print("Game could not be fetched")
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
                # game.select(row, col)
                if game.connected():
                    try:
                        n.send(str.encode(row + "," + col))
                    except:
                        print("could not send selected position")

        try:
            n.send("update")
        except:
            print("could not update window")


    pygame.quit()


#main()
