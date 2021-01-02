import operator

import Rook
import sys


class Pawn:

    def __init__(self, r, c, color):
        self.r, self.c, self.color = r, c, color
        self.piece = 'Pawn'

    def get_position(self):
        return (self.r, self.c)

    def get_moves(self, board):
        valid_moves = []
        r, c, my_color = self.r, self.c, self.color

        x = 0
        first_row = -1
        if my_color == 'W': x, first_row, last_row = -1, 6, 0
        if my_color == 'B': x, first_row, last_row = 1, 1, 7
        comp = operator.lt if my_color == 'W' else operator.gt

        #If at the end of the board
        if r == last_row: return valid_moves

        # At the start
        if r == first_row:
            #Move one space
            if board[r + x][c] is None: valid_moves.append((r + x, c))
            #Move two spaces
            if board[r + (2 * x)][c] is None: valid_moves.append((r + (2 * x), c))

        #Anywhere on the board
        if comp(r, first_row):
            #Move one space
            if board[r + x][c] is None: valid_moves.append((r + x, c))

        #Taking a piece
        if board[r + x][c-1] is not None and board[r + x][c-1].color != my_color:
            valid_moves.append((r + x, c-1))
        if board[r + x][c+1] is not None and board[r + x][c+1].color != my_color:
            valid_moves.append((r + x, c+1))

        return valid_moves

    def moving(self, new_r, new_c, board):
        item_ate = None
        old_r, old_c  = self.r, self.c

        if board[new_r][new_c] is not None: item_ate = board[new_r][new_c]

        board[new_r][new_c] = self
        board[old_r][old_c] = None

        self.r, self.c = new_r, new_c
        return (board, item_ate)

    def choosing(self, option):
        if self.color == 'W': last_row = 0
        if self.color == 'B': last_row = 7

        #Make sure I'm in last row to convert
        if self.r != last_row:
            return (None, None)

        module_lst = ["Queen", "Bishop", "Knights", Rook]
        string_lst = ["Queen", "Bishop", "Knights", "Rook"]
        return (module_lst[option], string_lst[option])

    def convert(self, module, new_type, board):
        r, c, color = self.r, self.c, self.color

        #module = getattr(sys.modules[__name__], new_type)
        new_class = getattr(module, new_type)
        new_piece = new_class(r, c, color)

        #new_class = getattr(Rook, new_type)
        #new_piece = new_class(r, c, color)

        board[r][c] = new_piece
        return board

    #def convert(self, new_type):
        #new_class = getattr(Rook, new_type)
        #new_obj = new_class(5, 5, 'W')
        #print(new_obj.name)

if __name__ == '__main__':
    board = [[None for i in range(8)] for j in range(8)]
    #board[r][c]

    w_pawn = Pawn(0, 1, 'W')
    b_pawn = Pawn(5, 0, 'B')
    board[w_pawn.r][w_pawn.c] = w_pawn
    board[b_pawn.r][b_pawn.c] = b_pawn


    for row in board:
        print(row)

    print

    (module, name) = w_pawn.choosing(3)
    w_pawn.convert(module, name, board)

    for row in board:
        print(row)
    ''' 
    for row in board:
        print(row)


    print(b_pawn.get_moves(board))
    (board, item_ate) = w_pawn.moving(5, 1, board)

    print()
    for row in board:
        print(row)

    if item_ate is not None:
        print(item_ate.piece + ' ' +  item_ate.color)


'''