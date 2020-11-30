import pygame
from checkers.constants import *
from checkers.board import Board


class Game:

    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        for row in range(8):
            for col in range(8):
                if self.board.board[row][col] != 0:
                    self.board.board[row][col].row = row
                    self.board.board[row][col].col = col
                    self.board.board[row][col].calc_pos()

                    if (row == ROWS - 1 and self.board.board[row][col].color == WHITE) or (
                            row == 0 and self.board.board[row][col].color == RED):
                        self.board.board[row][col].make_king()
                        if self.board.board[row][col].color == WHITE:
                            self.board.white_kings += 1
                        else:
                            self.board.red_kings += 1
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
        self._init()

    def setBoard(self, board):
        self.board = board

    def select(self, row, col, n):
        if self.selected:
            result = self._move(row, col, n)
            if not result:
                self.selected = None
                self.select(row, col, n)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

    def winner(self):
        return self.board.winner()

    def _move(self, row, col, n):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn(n)

        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def change_turn(self, n):
        self.valid_moves = []
        blank = n.send("changeTurn")
        print("changed")
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def change_turn_n(self, color):
        if color == RED:
            self.turn = RED
        elif color == WHITE:
            self.turn = WHITE
