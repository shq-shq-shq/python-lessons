import pygame
from pygame.locals import *
import random

pygame.init()

SCREEN_SIZE = (800, 600)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Linux Admin")

COMP_SIZE = (150, 150)
COMP_SCREEN_RECT = pygame.rect.Rect((23,33), (105,64))
COMP_IMAGE = pygame.image.load("img/computer.jpg").convert()

APPLE_LOGO = pygame.image.load("img/apple.png").convert()
APPLE_ADMIN_IMAGE = pygame.image.load("img/steveJobs.jpg").convert()

WINDOWS_LOGO = pygame.image.load("img/windows.png").convert()
WINDOWS_ADMIN_IMAGE = pygame.image.load("img/billGates.jpg").convert()

LINUX_LOGO = pygame.image.load("img/linux.png").convert()

INSTALLATION_CYCLES = 60

COMPUTER_GRID_SIZE = (4, 3)
COMPUTER_GRID_COORD = (50, 50)
COMPUTERS_CELL_WH = (180, 180)

NEW_OS_EVENT = pygame.USEREVENT + 1

pygame.time.set_timer(NEW_OS_EVENT, 1000)

computerStates = [[['L', 0] for x in range(COMPUTER_GRID_SIZE[0])] for y in range(COMPUTER_GRID_SIZE[1])]

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == MOUSEBUTTONDOWN:
            x, y = event.pos

            cellX = (x - COMPUTER_GRID_COORD[0]) // COMPUTERS_CELL_WH[0]
            cellY = (y - COMPUTER_GRID_COORD[1]) // COMPUTERS_CELL_WH[1]

            if 0 <= cellX < COMPUTER_GRID_SIZE[0] and 0 <= cellY < COMPUTER_GRID_SIZE[1]:
                cellOffsetX = x - COMPUTER_GRID_COORD[0] - cellX * COMPUTERS_CELL_WH[0]
                cellOffsetY = y - COMPUTER_GRID_COORD[1] - cellY * COMPUTERS_CELL_WH[1]

                if COMP_SCREEN_RECT.collidepoint((cellOffsetX, cellOffsetY)):
                    computerStates[cellY][cellX] = ['L', 0]

        elif event.type == NEW_OS_EVENT:
            newInstallationCoord = (
            random.randint(0, COMPUTER_GRID_SIZE[0] - 1), random.randint(0, COMPUTER_GRID_SIZE[1] - 1))
            newInstallationOS = random.choice(['W', 'M'])

            compState = computerStates[newInstallationCoord[1]][newInstallationCoord[0]]

            if compState[0] != newInstallationOS and compState[1] == 0:
                computerStates[newInstallationCoord[1]][newInstallationCoord[0]] = [newInstallationOS,
                                                                                    INSTALLATION_CYCLES]

    for y in range(COMPUTER_GRID_SIZE[1]):
        for x in range(COMPUTER_GRID_SIZE[0]):
            if computerStates[y][x][1] > 0:
                computerStates[y][x][1] -= 1

    screen.fill((255, 255, 255), pygame.rect.Rect((0, 0), SCREEN_SIZE))

    for y in range(COMPUTER_GRID_SIZE[1]):
        for x in range(COMPUTER_GRID_SIZE[0]):
            coord = (COMPUTER_GRID_COORD[0] + x * COMPUTERS_CELL_WH[0],
                     COMPUTER_GRID_COORD[1] + y * COMPUTERS_CELL_WH[1])

            screen.blit(COMP_IMAGE, coord)

            computerState, count = computerStates[y][x]

            screenImg = None
            if computerState == 'L':
                screenImg = LINUX_LOGO
            elif computerState == 'W':
                if count > 0:
                    screenImg = WINDOWS_ADMIN_IMAGE
                else:
                    screenImg = WINDOWS_LOGO
            elif computerState == 'M':
                if count > 0:
                    screenImg = APPLE_ADMIN_IMAGE
                else:
                    screenImg = APPLE_LOGO

            screen.blit(screenImg, (coord[0] + COMP_SCREEN_RECT[0], coord[1] + COMP_SCREEN_RECT[1]))

    pygame.display.flip()
