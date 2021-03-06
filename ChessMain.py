'''
This is oour main driver file. It will be responsible for handling user input and displaying the current GameState Object
'''

#Take care of black and white turn
#Make sure empty selects don't get tracked
#Figure out how to highlight

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512 #400 IS ANOTHER OPTION
DIMENSION = 8 #DIMESION OF CHESS BOARD IS 8X8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
INITIALIZE A GLOBAL DIC OF IMAGES. THIS IS CALLED EXACTLY ONCE IN THE MAIN
'''
def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bR", "bN", "bB", "bK", "bQ"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("chess images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

'''
The main driver for our code. This will handle user input and updating the graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    sqSelected = () #no square is selected, keep track of the last click of the user (tuple: (row, col))
    playerClicks = [] #keep track of player clicks (two tuples: [(6, 4), (4, 4)]

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONUP:
                BGCOLOR = (3, 115, 46)


            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE


                if sqSelected == (row, col): #the user clicked the same square twice
                    sqSelected, playerClicks = (), []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                    #Here is where list of moves need to be added

                if len(playerClicks) == 2: #after 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    gs.makeMove(move)
                    sqSelected, playerClicks = (), []


        drawGameState(screen, gs)

        if len(playerClicks) == 1:
            (row, col) = playerClicks[0]
            highlight(screen, col, row, gs.board)

        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen) #draw squares on the board
    drawPieces(screen, gs.board) #draw pieces on top of the sqaures

'''
Draw the squares on the board. The top left square is always light
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

''' 
Draw the pieces on the board using the current GameState.board
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

''' 
Highlight the pieces after being selected
--Need to add logic to unhighlight when user changes chooses another piece
'''
def highlight(screen, c, r, board):
    color = p.Color(207, 164, 235)
    p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    #Draw the piece ontop of highlighted item
    piece = board[r][c]
    if piece != "--": screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))



if __name__ == '__main__':
    main()



