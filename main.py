import pygame
from checkers.constants import *
from checkers.board import *
from checkers.game import Game
from network import Network

FPS = 60

pygame.font.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('checkers')


def end_screen(win, text):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 80)
    show = font.render(text, True, (255, 255, 255))
    win.blit(show, (WIDTH / 2 - show.get_width() / 2, 300))
    pygame.display.update()


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def run():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    n = Network()
    player = int(n.getP())
    connected = n.send("connected")

    while connected < 2:
        connected = n.send("connected")
    while run:
        clock.tick(FPS)
        # change winning text
        winner = game.winner()
        if winner is not None:
            if winner == RED:
                end_screen(WIN, "RED is the Winner!")
            else:
                end_screen(WIN, "WHITE is the Winner!")
            print(winner)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if player == 1 and n.send("turn") == RED or player == 2 and n.send("turn") == WHITE:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col, n)
                    for row in game.board.board:
                        for col in row:
                            if col != 0:
                                print(col.row, "-", col.col, " ", end="")
                        print("\n")
            game.change_turn_n(n.send("turn"))
            n.send(game.board)
        game.setBoard(n.send("giveMe"))
        game.update()
    pygame.quit()
