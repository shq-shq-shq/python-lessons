import pygame
import random
from pygame.locals import *

SCREEN_SIZE = (800, 600)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("A Game")

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    screen.fill((0, 0, 0), pygame.rect.Rect((0, 0), SCREEN_SIZE))
    # ...
    pygame.display.flip()
