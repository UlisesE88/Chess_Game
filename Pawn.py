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

        if self.color == 'W':
            #At the start
            if r == 6:
                if board[r - 1][c] is None:
                    valid_moves.append((r - 1, c))
                if board[r - 2][c] is None:
                    valid_moves.append((r - 2, c))
            #Anywhere on the board
            if r < 6:
                if board[r - 1][c] is None:
                    valid_moves.append((r - 1, c))
            #Taking a piece
            if board[r - 1][c-1] is not None and board[r - 1][c-1].color == 'B':
                valid_moves.append((r - 1, c-1))

            if board[r - 1][c+1] is not None and board[r - 1][c+1].color == 'B':
                valid_moves.append((r - 1, c+1))

        if self.color == 'B':
            #At the start
            if r == 1:
                if board[r + 1][c] is None:
                    valid_moves.append((r + 1, c))
                if board[r + 2][c] is None:
                    valid_moves.append((r + 2, c))
            #Anywhere on the board
            if r > 1:
                if board[r + 1][c] is None:
                    valid_moves.append((r + 1, c))
            #Taking a piece
            if board[r + 1][c-1] is not None and board[r+1][c-1].color == 'W':
                valid_moves.append((r+1, c-1))

            if board[r+1][c+1] is not None and board[r+1][c+1].color == 'W':
                valid_moves.append((r+1, c+1))

        return valid_moves

    def moving(self, r, c, board):
        item_ate = None

        old_r = self.r
        old_c = self.c

        if board[r][c] is not None:
            item_ate = board[r][c]

        board[r][c] = self
        board[old_r][old_c] = None

        self.r = r
        self.c = c

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


    print(w_pawn.get_moves(board))
    (board, item_ate) = w_pawn.moving(5, 0, board)

    for row in board:
        print(row)

    print(item_ate.piece + ' ' +  item_ate.color)
