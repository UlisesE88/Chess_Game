import operator
from Pieces import Pieces
import pygame as p
class Bishop(Pieces):
    def __init__(self, r, c, color):
        super(Bishop, self).__init__(r, c, color)
        self.piece = 'Biship'

        piece = "wB" if color == 'white' else "bB"
        SQ_SIZE = 512 // 8
        self.image = p.transform.scale(p.image.load("chess images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    def get_position(self):
        return (super(Bishop, self).get_position())

    def moving(self, new_r, new_c, board):
        return super(Bishop, self).moving()