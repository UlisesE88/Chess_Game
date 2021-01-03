'''
This class is responsible for storing all the info about the current state of a chess game.
It will also be responsible for determining the valid
moves at the current state. It will also keep a move log
'''

from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from Queen import Queen
from King import King


class GameState:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []

    def createpieces(self):
        board = [[None for i in range(8)] for j in range(8)]
        DIMENSION = 8
        for r in range(DIMENSION):
            for c in range(DIMENSION):
                if r == 1:
                    board[r][c] = Pawn(r, c, "black")
                if r == 6:
                    board[r][c] = Pawn(r, c, "white")

        #Place rooks on board
        board[0][0], board[0][7] = Rook(r, c, "black"), Rook(r, c, "black")
        board[7][0], board[7][7] = Rook(r, c, "white"), Rook(r, c, "white")

        # Place Knight on board
        board[0][1], board[0][6] = Knight(r, c, "black"), Knight(r, c, "black")
        board[7][1], board[7][6] = Knight(r, c, "white"), Knight(r, c, "white")

        # Place Bishop on board
        board[0][2], board[0][5] = Bishop(r, c, "black"), Bishop(r, c, "black")
        board[7][2], board[7][5] = Bishop(r, c, "white"), Bishop(r, c, "white")

        # Place Queen on board
        board[0][3] = Queen(r, c, "black")
        board[7][3] = Queen(r, c, "white")

        # Place King on board
        board[0][4] = King(r, c, "black")
        board[7][4] = King(r, c, "white")

        return board

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove



#Move class that tracks moves that were made
class Move:
    '''
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRank = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}
    '''
    rowsToRanks = {7: "1", 6: "2", 5: "3", 4: "4",
                   3: "5", 2: "6", 1: "7", 0: "8"}
    colsToFiles = {0: "a", 1: "b", 2: "c", 3: "d",
                   4: "e", 5: "f", 6: "g", 7: "h"}
    def __init__(self, startSq, endSq, board):
        (self.startRow, self.startCol) = startSq
        (self.endRow, self.endCol) = endSq
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + " -> " + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return Move.colsToFiles[c] + Move.rowsToRanks[r]

if __name__ == '__main__':
    board = [
        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
    move = Move((0, 0), (1,1), board)
    print(move.getChessNotation())

    for r in range(len(board)):
        for c in range(len(board)):
            print(board[r][c], r , c)

    gs = GameState()
    for row in gs.createpieces():
        print(row)

    pass

