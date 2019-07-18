import pygame

pygame.init()

SCREEN_SIZE = 500
STEP = 20

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))


running = 1

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    screen.fill((0, 0, 0))
    for y in range(SCREEN_SIZE // STEP):
        pygame.draw.line(screen, (0, 0, 255), (0, y * STEP), (SCREEN_SIZE - y * STEP, 0))
        pygame.draw.line(screen, (255, 0, 0), (SCREEN_SIZE, SCREEN_SIZE - y * STEP), (y * STEP, SCREEN_SIZE))
        pygame.draw.line(screen, (0, 255, 0), (0, SCREEN_SIZE - y * STEP), (SCREEN_SIZE - y * STEP, SCREEN_SIZE))
        pygame.draw.line(screen, (255, 255, 255), (SCREEN_SIZE, y * STEP), (y * STEP, 0))

    pygame.display.flip()
