from checkers.constants import *
from checkers.board import Board


class Game:

    def __init__(self, id):
        self.ready = False
        self.id = id
        self._init()

    def update(self):
        self.board.draw()
        self.board.draw_valid_moves(self.valid_moves)
        self.board.update()

    def _init(self):
        self.p1 = RED
        self.p2 = WHITE
        self.p1_turn = True
        self.p2_turn = False
        self.selected = None
        self.board = Board()
        self.turn = self.p1
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

    def winner(self):
        if self.board.winner() == self.p1:
            return "RED IS THE WINNER!"
        elif self.board.winner() == self.p2:
            return "WHITE IS THE WINNER!"
        else:
            return self.board.winner()

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            # self.change_turn()

        else:
            return False

        return True

    def change_turn(self, who):
        self.valid_moves = []
        if who == 0:
            self.p1_turn = False
            self.turn = WHITE
            self.p2_turn = True
        else:
            self.p2_turn = False
            self.turn = self.p1
            self.p1_turn = True

    def connected(self):
        return self.ready
