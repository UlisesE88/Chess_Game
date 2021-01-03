import operator
from Pieces import Pieces
import pygame as p
class King(Pieces):
    def __init__(self, r, c, color):
        super(King, self).__init__(r, c, color)
        self.piece = 'King'

        piece = "wK" if color == 'white' else "bK"
        SQ_SIZE = 512 // 8
        self.image = p.transform.scale(p.image.load("chess images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    def get_position(self):
        return (super(King, self).get_position())

    def moving(self, new_r, new_c, board):
        return super(King, self).moving()