class Biship:
    def __init__(self, r, c, color):
        self.r = r
        self.c = c
        self.color = color
        self.name = 'Biship'

    def get_position(self):
        return (self.r, self.c)

    def get_moves(self, board):
        valid_moves = []
        r, c, my_color = self.r, self.c, self.color