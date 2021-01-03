
class Pieces:
    def __init__(self, r, c, color):
        self.r, self.c, self.color = r, c, color

    def get_position(self):
        return (self.r, self.c)

    def moving(self, new_r, new_c, board):
        item_ate = None
        old_r, old_c  = self.r, self.c

        if board[new_r][new_c] is not None: item_ate = board[new_r][new_c]

        board[new_r][new_c] = self
        board[old_r][old_c] = None

        self.r, self.c = new_r, new_c
        return (board, item_ate)

if __name__ == '__main__':
    pass
