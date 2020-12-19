class Rook:
    def __init__(self, r, c, color):
        self.r = r
        self.c = c
        self.color = color
        self.name = 'Rook'

    def get_position(self):
        return (self.r, self.c)

    def get_moves(self, board):
        valid_moves = []
        r, c, my_color = self.r, self.c, self.color

        #Check Left
        while(c > 0 and board[r][c-1] is None):
            valid_moves.append((r, c-1))
            c-= 1

        (last_r, last_c) = valid_moves[-1]
        if last_c - 1 >= 0:
            temp_item = board[last_r][last_c - 1]

            if (temp_item is not None and temp_item.color != my_color):
                valid_moves.append((last_r, last_c - 1))

        #Check right
        r, c, my_color = self.r, self.c, self.color
        while (c < 7 and board[r][c + 1] is None):
            valid_moves.append((r, c + 1))
            c += 1

        (last_r, last_c) = valid_moves[-1]
        if last_c + 1 <= 7:
            temp_item = board[last_r][last_c + 1]

            if (temp_item is not None and temp_item.color != my_color):
                valid_moves.append((last_r, last_c + 1))


        #Check Up
        r, c, my_color = self.r, self.c, self.color
        while (r > 0 and board[r - 1][c] is None):
            valid_moves.append((r - 1,c))
            r -= 1

        (last_r, last_c) = valid_moves[-1]
        if last_r - 1 >= 0:
            temp_item = board[last_r - 1][last_c]

            if (temp_item is not None and temp_item.color != my_color):
                valid_moves.append((last_r - 1, last_c))

        #Check Down
        r, c, my_color = self.r, self.c, self.color
        while (r < 7 and board[r + 1][c] is None):
            valid_moves.append((r + 1, c))
            r += 1

        (last_r, last_c) = valid_moves[-1]
        if last_r + 1 <= 7:
            temp_item = board[last_r + 1][last_c]

            if (temp_item is not None and temp_item.color != my_color):
                valid_moves.append((last_r + 1, last_c))


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
    # board[r][c]

    w_rook = Rook(4, 4, 'W')
    b_rook_1 = Rook(4, 0, 'B')
    b_rook_2 = Rook(4, 6, 'B')
    b_rook_3 = Rook(1, 4, 'B')
    w_rook_2 = Rook(6, 4, 'W')

    board[4][4] = w_rook
    board[4][0] = b_rook_1
    board[4][6] = b_rook_2
    board[1][4] = b_rook_3
    board[6][4] = w_rook_2
    #board[4][6] = b_rook


    for row in board:
        print(row)
    print

    lst = w_rook.get_moves(board)
    print(lst)