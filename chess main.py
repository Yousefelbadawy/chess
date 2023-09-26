import pygame as p
import chessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def load_images():
    pieces = {"wP", "wR", "wN", "wB", "wK",
              "wQ", "wP", "wR", "wN", "wB", "wK", "wQ", "bP", "bR", "bN", "bB", "bK",
              "bQ"}
    for piece in pieces:
        IMAGES[piece] = p.image.load("images/" + piece + ".png")


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("green"))
    gs = chessEngine.GameState()
    load_images()
    running = True
    sqSelected = []
    plyerClicks = []

    while running:

        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                x,y = p.mouse.get_pos()
                col = x,y[0]/SQ_SIZE
                row = x,y[1]/SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                    plyerClicks = []
                else:
                    plyerClicks.append(sqSelected)
                    sqSelected = (row, col)
                if len(plyerClicks) == 2:

                    Move = chessEngine.Move(
                        plyerClicks[0], plyerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = ()
                    plyerClicks = []

        clock.tick(MAX_FPS)
        p.display.flip()
        drawGameState(screen, gs)


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [p.Color("black"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(
                c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(
                    c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
