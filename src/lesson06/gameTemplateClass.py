import pygame
import random
from pygame.locals import *

SCREEN_SIZE = (800, 600)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("A Game")

    def run(self):
        self.running = True

        while self.running:
            self.handleEvents()
            self.updateObjects()
            self.draw()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False

    def updateObjects(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0), pygame.rect.Rect((0, 0), SCREEN_SIZE))
        # ...
        pygame.display.flip()


def main():
    pygame.init()
    game = Game()
    game.run()

main()