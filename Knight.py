import operator
from Pieces import Pieces
import pygame as p
class Knight(Pieces):
    def __init__(self, r, c, color):
        super(Knight, self).__init__(r, c, color)
        self.piece = 'Knight'

        piece = "wN" if color == 'white' else "bN"
        SQ_SIZE = 512 // 8
        self.image = p.transform.scale(p.image.load("chess images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    def get_position(self):
        return (super(Knight, self).get_position())

    def moving(self, new_r, new_c, board):
        return super(Knight, self).moving()