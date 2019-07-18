import pygame
from pygame.locals import *
import random

FIGURES = [
    ["O"],

    ["O",
     "O",
     "O",
     "O"],

    ["OOO",
     ".O."],

    ["OOO",
     ".O.",
     ".O."],

    [".O.",
     "OOO",
     ".O."],

    ["O.",
     "O.",
     "OO"],

    ["OO",
     "OO"]
]

CELL_W = 30
CELL_H = 30
FIELD_W = 10
FIELD_H = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FIGURE_SPEED_FAST = 1
FIGURE_SPEED_SLOW = 20

pygame.init()

SCREEN = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Tetris")

fieldPos = (50, SCREEN.get_height() - CELL_H * FIELD_H - 50)
fieldRect = pygame.rect.Rect(fieldPos, (FIELD_W * CELL_W, FIELD_H * CELL_H))

class Tetris:
    def createEmptyField(self):
        self.field = [
             [WHITE] + [BLACK for x in range(FIELD_W - 2)] + [WHITE] for y in range(FIELD_H - 1)
         ] + [[WHITE for i in range(FIELD_W)]]

    @staticmethod
    def rotateFigure(figure):
        return [[figure[y][-1 - x] for y in range(len(figure))] for x in range(len(figure[0]))]

    def createNewFigure(self):
        self.figure = random.choice(FIGURES)
        for i in range(random.randint(0, 3)):
            self.figure = self.rotateFigure(self.figure)

        self.figurePos = (random.randint(1, FIELD_W - len(self.figure[0]) - 2), -len(self.figure) + 1)
        self.figureColor = (random.randint(32, 255), random.randint(32, 255), random.randint(32, 255))

    def canMoveFigureTo(self, figure, figurePos):
        for y in range(len(figure)):
            for x in range(len(figure[y])):
                if 0 <= figurePos[1] + y and 0 <= figurePos[0] + x < FIELD_W \
                        and figure[y][x] == 'O' \
                        and self.field[figurePos[1] + y][figurePos[0] + x] != BLACK:
                    return False
        return True

    def transferFigureToField(self, figurePos):
        for y in range(len(self.figure)):
            for x in range(len(self.figure[y])):
                if y + figurePos[1] >= 0 and self.figure[y][x] == 'O':
                    self.field[figurePos[1] + y][figurePos[0] + x] = self.figureColor

    def isRowFull(self, y):
        for c in self.field[y]:
            if c == BLACK:
                return False

        return True

    def removeFullRows(self):
        destRow = len(self.field) - 2
        srcRow = destRow

        while srcRow >= 0:
            if self.isRowFull(srcRow):
                srcRow -= 1
            else:
                if srcRow != destRow:
                    self.field[destRow] = self.field[srcRow]
                destRow -= 1
                srcRow -= 1

        while destRow >= 0:
            self.field[destRow] = [WHITE] + [BLACK for i in range(FIELD_W - 2)] + [WHITE]
            destRow -= 1

    def draw(self):
        for y in range(FIELD_H):
            for x in range(FIELD_W):
                SCREEN.fill(self.field[y][x], pygame.rect.Rect((fieldPos[0] + CELL_W * x, fieldPos[1] + CELL_H * y), (CELL_W, CELL_H)))

        for y in range(len(self.figure)):
            if y + self.figurePos[1] >= 0:
                for x in range(len(self.figure[y])):
                    if self.figure[y][x] == 'O':
                        SCREEN.fill(self.figureColor,
                            pygame.rect.Rect((fieldPos[0] + CELL_W * (x + self.figurePos[0]),
                                              fieldPos[1] + CELL_H * (y + self.figurePos[1])),
                                             (CELL_W, CELL_H)))

        pygame.display.flip()

    def restart(self):
        self.createEmptyField()
        self.createNewFigure()

    def run(self):
        self.restart()

        figureSpeed = FIGURE_SPEED_SLOW
        figureSpeedCounter = 1

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

                    elif event.key == K_r:
                        self.restart()
                        figureSpeedCounter = 1
                        figureSpeed = FIGURE_SPEED_SLOW

                    elif event.key in (K_DOWN, K_SPACE):
                        figureSpeedCounter = 1
                        figureSpeed = FIGURE_SPEED_FAST

                    elif event.key == K_LEFT:
                        newPos = (self.figurePos[0] - 1, self.figurePos[1])
                        if self.canMoveFigureTo(self.figure, newPos):
                            self.figurePos = newPos

                    elif event.key == K_RIGHT:
                        newPos = (self.figurePos[0] + 1, self.figurePos[1])
                        if self.canMoveFigureTo(self.figure, newPos):
                            self.figurePos = newPos

                    elif event.key == K_UP:
                        rotatedFigure = self.rotateFigure(self.figure)
                        if self.canMoveFigureTo(rotatedFigure, self.figurePos):
                            self.figure = rotatedFigure

            figureSpeedCounter -= 1

            if figureSpeedCounter <= 0:
                newPos = (self.figurePos[0], self.figurePos[1] + 1)

                if not self.canMoveFigureTo(self.figure, newPos):
                    self.transferFigureToField(self.figurePos)
                    self.removeFullRows()
                    self.createNewFigure()
                    if not self.canMoveFigureTo(self.figure, self.figurePos):
                        self.restart()

                    figureSpeed = FIGURE_SPEED_SLOW

                else:
                    self.figurePos = newPos

                figureSpeedCounter = figureSpeed

            self.draw()

tetris = Tetris()
tetris.run()
