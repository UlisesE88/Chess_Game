import operator

class Pawn:

    def __init__(self, r, c, color):
        self.r = r
        self.c = c
        self.color = color
        self.piece = 'Pawn'

    def get_position(self):
        return (self.r, self.c)

    def get_moves(self, board):
        valid_moves = []
        r = self.r
        c = self.c
        my_color = self.color

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

if __name__ == '__main__':
    board = [[None for i in range(8)] for j in range(8)]
    #board[r][c]

    w_pawn = Pawn(6, 1, 'W')
    b_pawn = Pawn(5, 0, 'B')
    board[w_pawn.r][w_pawn.c] = w_pawn
    board[b_pawn.r][b_pawn.c] = b_pawn


    for row in board:
        print(row)


    print(b_pawn.get_moves(board))
    (board, item_ate) = w_pawn.moving(5, 1, board)

    print()
    for row in board:
        print(row)

    if item_ate is not None:
        print(item_ate.piece + ' ' +  item_ate.color)


