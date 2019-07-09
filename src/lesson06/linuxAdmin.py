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
STEVE_JOBS_FACE = pygame.image.load("img/steveJobs.jpg").convert()

WINDOWS_LOGO = pygame.image.load("img/windows.png").convert()
BILL_GATES_FACE = pygame.image.load("img/billGates.jpg").convert()

LINUX_LOGO = pygame.image.load("img/linux.png").convert()
LINUS_TORVALDS_FACE = pygame.image.load("img/linusTorvalds.jpg").convert()

INSTALLATION_CYCLES = 60

COMP_GRID_SIZE = (4, 3)
COMP_GRID_COORD = (50, 50)
COMP_WH = (180, 180)

NEW_OS_EVENT = pygame.USEREVENT + 1

pygame.time.set_timer(NEW_OS_EVENT, 1000)

computerStates = [[['L', 0] for x in range(COMP_GRID_SIZE[0])] for y in range(COMP_GRID_SIZE[1])]

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

            cellX = (x - COMP_GRID_COORD[0]) // COMP_WH[0]
            cellY = (y - COMP_GRID_COORD[1]) // COMP_WH[1]

            if 0 <= cellX < COMP_GRID_SIZE[0] and 0 <= cellY < COMP_GRID_SIZE[1]:
                cellOffsetX = x - COMP_GRID_COORD[0] - cellX * COMP_WH[0]
                cellOffsetY = y - COMP_GRID_COORD[1] - cellY * COMP_WH[1]

                if COMP_SCREEN_RECT.collidepoint((cellOffsetX, cellOffsetY)):
                    computerStates[cellY][cellX] = ['L', INSTALLATION_CYCLES]

        elif event.type == NEW_OS_EVENT:
            instCoord = (random.randint(0, COMP_GRID_SIZE[0] - 1), random.randint(0, COMP_GRID_SIZE[1] - 1))
            instOS = random.choice(['W', 'M'])

            os, timer = computerStates[instCoord[1]][instCoord[0]]

            if os != instOS and timer == 0:
                computerStates[instCoord[1]][instCoord[0]] = [instOS, INSTALLATION_CYCLES]

    for y in range(COMP_GRID_SIZE[1]):
        for x in range(COMP_GRID_SIZE[0]):
            if computerStates[y][x][1] > 0:
                computerStates[y][x][1] -= 1

    screen.fill((255, 255, 255), pygame.rect.Rect((0, 0), SCREEN_SIZE))

    for y in range(COMP_GRID_SIZE[1]):
        for x in range(COMP_GRID_SIZE[0]):
            coordX = COMP_GRID_COORD[0] + x * COMP_WH[0]
            coordY = COMP_GRID_COORD[1] + y * COMP_WH[1]

            screen.blit(COMP_IMAGE, (coordX, coordY))

            currentOS, timer = computerStates[y][x]

            screenImg = None

            if currentOS == 'L':
                if timer > 0:
                    screenImg = LINUS_TORVALDS_FACE
                else:
                    screenImg = LINUX_LOGO

            elif currentOS == 'W':
                if timer > 0:
                    screenImg = BILL_GATES_FACE
                else:
                    screenImg = WINDOWS_LOGO

            elif  currentOS == 'M':
                if timer > 0:
                    screenImg = STEVE_JOBS_FACE
                else:
                    screenImg = APPLE_LOGO

            screen.blit(screenImg, (coordX + COMP_SCREEN_RECT[0], coordY + COMP_SCREEN_RECT[1]))

            if timer > 0:
                progressBarX = COMP_SCREEN_RECT.width * ((INSTALLATION_CYCLES - timer) / INSTALLATION_CYCLES)

                screen.fill((240, 240, 255), pygame.rect.Rect((coordX + COMP_SCREEN_RECT.left, coordY + COMP_SCREEN_RECT.bottom - 5),
                                                              (progressBarX, 5)))
                screen.fill((128, 128, 255), pygame.rect.Rect((coordX + COMP_SCREEN_RECT.left + progressBarX, coordY + COMP_SCREEN_RECT.bottom - 5),
                                                              (COMP_SCREEN_RECT.width - progressBarX, 5)))

    pygame.display.flip()
