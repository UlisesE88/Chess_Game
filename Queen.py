import operator
from Pieces import Pieces
import pygame as p
class Queen(Pieces):
    def __init__(self, r, c, color):
        super(Queen, self).__init__(r, c, color)
        self.piece = 'Biship'

        piece = "wQ" if color == 'white' else "bQ"
        SQ_SIZE = 512 // 8
        self.image = p.transform.scale(p.image.load("chess images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    def get_position(self):
        return (super(Queen, self).get_position())

    def moving(self, new_r, new_c, board):
        return super(Queen, self).moving()