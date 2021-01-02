import operator
class Rook:
    def __init__(self, r, c, color):
        self.r, self.c, self.color = r, c, color
        self.name = 'Rook'

    def get_position(self):
        return (self.r, self.c)

    def get_moves(self, board):
        valid_moves = []
        r, c, my_color = self.r, self.c, self.color

        #Left
        comp, comp_2 = operator.gt, operator.ge
        valid_moves = self.checking_direction('c', comp, comp_2, r, 0, c, -1, 0, valid_moves, board)

        #Up
        valid_moves = self.checking_direction('r', comp, comp_2, r, -1, c, 0, 0, valid_moves, board)

        #Right
        comp, comp_2 = operator.lt, operator.le
        valid_moves = self.checking_direction('c', comp, comp_2, r, 0, c, 1, 7, valid_moves, board)

        # Down
        valid_moves = self.checking_direction('r', comp, comp_2, r, 1, c, 0, 7, valid_moves, board)

        return valid_moves

    def checking_direction(self, r_c_type, comp, comp_2, r, x, c, y, last, valid_moves, board):
        '''
        :param r_c: type
        :param comp: compare type (eg. less than or greater than)
        :param x: adding/subtracting to r
        :param y: adding/subtracting to c
        :param last: last column or row on board
        :param valid_moves: list of possible moves
        '''

        r_c = r if r_c_type == 'r' else c
        i = x if r_c_type == 'r' else y

        while (comp(r_c, last) and board[r + x][c + y] is None):
            valid_moves.append((r + x, c + y))
            r += x
            c += y
            r_c += i

        (last_r, last_c) = valid_moves[-1]
        last_r_c = last_r + x if r_c_type == 'r' else last_c + y
        if(comp_2(last_r_c, last)):
            temp_item = board[last_r + x][last_c + y]
            if (temp_item.color != self.color):
                valid_moves.append((last_r + x, last_c + y))

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
    b_rook_1 = Rook(4, 1, 'B')
    b_rook_2 = Rook(4, 6, 'B')
    b_rook_3 = Rook(1, 4, 'B')
    w_rook_2 = Rook(6, 4, 'B')

    board[4][4] = w_rook
    board[4][1] = b_rook_1
    board[4][6] = b_rook_2
    board[1][4] = b_rook_3
    board[7][4] = w_rook_2
    #board[4][6] = b_rook


    for row in board:
        print(row)
    print

    lst = w_rook.get_moves(board)
    print(lst)

    #first: [(4, 3), (4, 2), (4, 1)]
    #second: [(4, 3), (4, 2), (4, 1), (4, 0)]
