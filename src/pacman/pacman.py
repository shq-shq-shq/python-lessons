import pygame as pg
import pygame.locals as pl
import math
from gameutil import *

pg.init()

CELL_W = 25
CELL_H = 25
CELL_WH = (CELL_W, CELL_H)

CELL_W2 = CELL_W // 2
CELL_H2 = CELL_H // 2
CELL_WH2 = (CELL_W2, CELL_H2)

FOOD_RADIUS = CELL_W / 5
LINE_THICKNESS = 4
PACMAN_RADIUS = CELL_W // 2

FIELD_TEMPLATE = [
    '/------------`',
    '|............|',
    '|./--`./---`.|',
    '|.|  |.|   |.|',
    '|.L--J.L---J.L',
    '|..........*..',
    '|./--`./`./---',
    '|.L--J.||.L--`',
    '|......||....|',
    'L----`.|L--`.|',
    '     |.|/--J.L',
    '     |.||.....',
    '     |.||./--=',
    '-----J.LJ.|   ',
    '..........|   '
]

# 0: 00     /
# 1: 01     `
# 2: 10     L
# 3: 11     J
MIRROR_CODES = '/`LJ'
WALL_CODES = '/`LJ|-='

PORTAL_CELL_1 = Vector(-1, 14)
PORTAL_CELL_2 = Vector(28, 14)

PLAYER_START_CELL = Vector(15, 5)

PLAYER_SPEED = 5

# player direction:
D_RIGHT = 0
D_UP = 1
D_LEFT = 2
D_DOWN = 3

DIRECTION_VECTOR = {
    D_RIGHT: Vector(1, 0),
    D_UP: Vector(0, -1),
    D_LEFT: Vector(-1, 0),
    D_DOWN: Vector(0, 1)
}


class Field:
    def __init__(self, fieldTemplate):
        templateRows = len(fieldTemplate)
        fieldRows = templateRows * 2 - (templateRows % 2)
        templateCols = len(fieldTemplate[0])
        fieldCols = templateCols * 2 - (templateCols % 2)

        def mirror(code, flipX, flipY):
            codePos = MIRROR_CODES.find(code)
            if codePos >= 0:
                return MIRROR_CODES[codePos ^ ((2 if flipY else 0) + (1 if flipX else 0))]
            else:
                return code

        def cell(x, y):
            if x < templateCols:
                if y < templateRows:
                    return fieldTemplate[y][x]
                else:
                    return mirror(fieldTemplate[fieldRows - y - 1][x], False, True)
            else:
                if y < templateRows:
                    return mirror(fieldTemplate[y][fieldCols - x - 1], True, False)
                else:
                    return mirror(fieldTemplate[fieldRows - y - 1][fieldCols - x - 1], True, True)

        self.field = [[cell(x, y) for x in range(fieldCols)] for y in range(fieldRows)]

    def cellToCoord(self, cell):
        return cell * CELL_WH

    def coordToCell(self, coord):
        return coord // CELL_WH

    def heightInCells(self):
        return len(self.field)

    def widthInCells(self):
        return len(self.field[0])

    def isFreeSpaceAt(self, cell):
        if cell in (PORTAL_CELL_1, PORTAL_CELL_2):
            return True

        if not 0 <= cell.x < self.widthInCells() or not 0 <= cell.y < self.heightInCells():
            return False

        return not self.field[cell.y][cell.x] in WALL_CODES

    def maybeMoveThroughPortal(self, cell, direction):
        if cell == PORTAL_CELL_1 and direction == D_LEFT:
            return PORTAL_CELL_2

        if cell == PORTAL_CELL_2 and direction == D_RIGHT:
            return PORTAL_CELL_1

        return None

    def drawCell(self, cell, code):
        x, y = self.cellToCoord(cell)

        if code == '/':
            pg.draw.line(SCREEN, (0, 0, 255), (x + CELL_W2, y + CELL_H), (x + CELL_W2, y + CELL_H2), LINE_THICKNESS)
            pg.draw.line(SCREEN, (0, 0, 255), (x + CELL_W2, y + CELL_H2), (x + CELL_W, y + CELL_H2), LINE_THICKNESS)
        elif code == '`':
            pg.draw.line(SCREEN, (0, 0, 255), (x, y + CELL_H2), (x + CELL_W2, y + CELL_H2), LINE_THICKNESS)
            pg.draw.line(SCREEN, (0, 0, 255), (x + CELL_W2, y + CELL_H2), (x + CELL_W2, y + CELL_H), LINE_THICKNESS)
        elif code == 'L':
            pg.draw.line(SCREEN, (0, 0, 255), (x + CELL_W2, y), (x + CELL_W2, y + CELL_H2), LINE_THICKNESS)
            pg.draw.line(SCREEN, (0, 0, 255), (x + CELL_W2, y + CELL_H2), (x + CELL_W, y + CELL_H2), LINE_THICKNESS)
        elif code == 'J':
            pg.draw.line(SCREEN, (0, 0, 255), (x, y + CELL_H2), (x + CELL_W2, y + CELL_H2), LINE_THICKNESS)
            pg.draw.line(SCREEN, (0, 0, 255), (x + CELL_W2, y + CELL_H2), (x + CELL_W2, y), LINE_THICKNESS)
        elif code == '|':
            pg.draw.line(SCREEN, (0, 0, 255), (x + CELL_W2, y), (x + CELL_W2, y + CELL_H), LINE_THICKNESS)
        elif code == '-':
            pg.draw.line(SCREEN, (0, 0, 255), (x, y + CELL_H2), (x + CELL_W, y + CELL_H2), LINE_THICKNESS)
        elif code == '=':
            pg.draw.line(SCREEN, (255, 0, 0), (x, y + CELL_H2), (x + CELL_W, y + CELL_H2), LINE_THICKNESS)
        elif code == '*':
            pg.draw.circle(SCREEN, (255, 224, 0), (x + CELL_W2, y + CELL_H2), int(FOOD_RADIUS))

    def draw(self):
        for y in range(len(self.field)):
            for x in range(len(self.field[y])):
                self.drawCell(Vector(x, y), self.field[y][x])


class Player:
    def __init__(self, field, coord):
        self.field = field
        self.coord = coord
        self.moveDirection = None
        self.desiredDirection = None
        self.facePhase = 0
        self.faceDirection = 0

    def draw(self):
        center = self.coord + CELL_WH2
        pg.draw.circle(SCREEN, (255, 255, 0), center, PACMAN_RADIUS)
        pg.draw.arc(SCREEN, (0, 0, 0), pg.rect.Rect(self.coord, (CELL_W, CELL_H)),
                    math.radians(self.faceDirection * 90 - 30),
                    math.radians(self.faceDirection * 90 + 30),
                    0)

    def setDesiredDirection(self, direction):
        self.desiredDirection = direction

    def move(self):
        if self.coord % CELL_WH == (0, 0):
            newCell = self.field.maybeMoveThroughPortal(self.field.coordToCell(self.coord), self.moveDirection)
            if newCell:
                self.coord = self.field.cellToCoord(newCell)

        if self.desiredDirection is not None:
            desiredCoord = self.coord + DIRECTION_VECTOR[self.desiredDirection] * PLAYER_SPEED

            if self.canMoveTo(desiredCoord, self.desiredDirection):
                self.coord = desiredCoord
                self.moveDirection = self.desiredDirection
                self.desiredDirection = None
                return

        if self.moveDirection is not None:
            newCoord = self.coord + DIRECTION_VECTOR[self.moveDirection] * PLAYER_SPEED

            if self.canMoveTo(newCoord, self.moveDirection):
                self.coord = newCoord
            else:
                self.moveDirection = None

    def canMoveTo(self, coord, direction):
        if direction in {D_RIGHT, D_LEFT} and coord.y % CELL_H != 0:
            return False

        if direction in {D_UP, D_DOWN} and coord.x % CELL_H != 0:
            return False

        if direction == D_RIGHT:
            coordToCheck = coord + (CELL_W - 1, 0)
        elif direction == D_DOWN:
            coordToCheck = coord + (0, CELL_H - 1)
        else:
            coordToCheck = coord

        return self.field.isFreeSpaceAt(self.field.coordToCell(coordToCheck))

class Game:
    def __init__(self):
        self.field = Field(FIELD_TEMPLATE)

        screenSize = Vector(self.field.widthInCells() * CELL_W, self.field.heightInCells() * CELL_H)

        global SCREEN
        SCREEN = pg.display.set_mode(screenSize)

        self.player = Player(self.field, self.field.cellToCoord(PLAYER_START_CELL))

        self.enemies = []

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pl.QUIT:
                return False

            if event.type == pl.KEYDOWN:
                if event.key == pl.K_ESCAPE:
                    return False

                elif event.key == pl.K_LEFT:
                    self.player.setDesiredDirection(D_LEFT)
                elif event.key == pl.K_RIGHT:
                    self.player.setDesiredDirection(D_RIGHT)
                elif event.key == pl.K_UP:
                    self.player.setDesiredDirection(D_UP)
                elif event.key == pl.K_DOWN:
                    self.player.setDesiredDirection(D_DOWN)

        return True

    def updateObjects(self):
        self.player.move()

        for enemy in self.enemies:
            enemy.move()

    def draw(self):
        SCREEN.fill((0, 0, 0), SCREEN.get_bounding_rect())

        self.field.draw()

        self.player.draw()

        pg.display.flip()

    def run(self):
        while True:
            if not self.handleEvents():
                break
            self.updateObjects()
            self.draw()


game = Game()
game.run()
