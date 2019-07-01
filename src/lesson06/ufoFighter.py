import pygame
import random
from pygame.locals import *

SCREEN = None
NEW_ENEMY_EVT = pygame.USEREVENT + 1


def replaceColorKeepAlpha(surface, newColor):
    result = surface.copy()
    w, h = result.get_size()
    r, g, b, newA = newColor

    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            result.set_at((x, y), pygame.Color(r, g, b, a * newA // 256))

    return result


class Background:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('space_2500.jpg').convert(), SCREEN.get_size())
        self.offsetX = 0

    def update(self):
        self.offsetX -= 1
        if self.offsetX < -self.image.get_width():
            self.offsetX += self.image.get_width()

    def draw(self):
        SCREEN.blit(self.image, (self.offsetX, 0))
        SCREEN.blit(self.image, (self.offsetX + self.image.get_width(), 0))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.normalImage = pygame.image.load('jet_128.png').convert()
        self.normalImage.set_colorkey((0, 0, 0), RLEACCEL)
        self.normalImage = self.normalImage.convert_alpha()
        self.damagedImage = replaceColorKeepAlpha(self.normalImage, (255, 0, 0, 128))

        self.image = self.normalImage
        self.rect = self.image.get_rect().move((20, (SCREEN.get_height() - self.image.get_height()) / 2))

        self.damagedCountDown = 0
        self.enemiesEncountered = pygame.sprite.Group()
        self.score = 100

    def handleKeysPressed(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0, -5)
        if keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if self.rect.top < 0:
            self.rect.move_ip(0, -self.rect.top)
        elif self.rect.bottom > SCREEN.get_height():
            self.rect.move_ip(0, SCREEN.get_height() - self.rect.bottom)

    def fire(self):
        if self.damagedCountDown == 0:
            return Missile((self.rect.right - 58, self.rect.top + 36))
        else:
            return None

    def update(self):
        if self.damagedCountDown > 0:
            self.damagedCountDown -= 1
            if self.damagedCountDown == 0:
                self.image = self.normalImage

    def enemyCollision(self, enemy):
        if enemy not in self.enemiesEncountered:
            self.enemiesEncountered.add(enemy)
            self.damagedCountDown = 30
            self.image = self.damagedImage
            self.score -= 5

    def updateScoreHitEnemy(self):
        self.score += 1

    def updateScoreMissedEnemy(self):
        self.score -= 2


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()

        self.image = pygame.image.load('ufo_96.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = self.image.convert_alpha()

        self.dyingImage = replaceColorKeepAlpha(self.image, (255, 255, 255, 128))

        self.rect = self.image.get_rect(center=(SCREEN.get_width() + self.image.get_width(),
                                                self.image.get_height() * random.randint(0, SCREEN.get_height() // self.image.get_height())))
        self.speed = random.randint(2, 7)

        self.timeToLive = 0

    def update(self):
        self.rect.move_ip(-self.speed, 0)

        if self.rect.right < 0:
            self.kill()
        elif self.timeToLive > 0:
            self.timeToLive -= 1
            if self.timeToLive == 0:
                self.kill()

    def die(self):
        self.image = self.dyingImage
        self.timeToLive = 3


class Missile(pygame.sprite.Sprite):
    def __init__(self, coord):
        super(Missile, self).__init__()

        self.image = pygame.image.load('missile.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)

        self.rect = self.image.get_rect(center=coord)

        self.speed = 7

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left > SCREEN.get_width():
            self.kill()


class Controller:
    def __init__(self):
        self.background = Background()
        self.player = Player()

        self.enemies = pygame.sprite.Group()
        self.enemies.add([Enemy() for _ in range(5)])

        self.missiles = pygame.sprite.Group()

        self.allSprites = pygame.sprite.Group()
        self.allSprites.add(self.player)
        self.allSprites.add(self.enemies)

        self.missedEnemies = pygame.sprite.Group()

        pygame.time.set_timer(NEW_ENEMY_EVT, 250)

        self.font = pygame.font.Font(None, 30)
        self.clock = pygame.time.Clock()

        self.running = False

    def run(self):
        self.running = True

        while self.running:
            self.updateObjects()
            self.handleEvents()
            self.handlePressedKeys()
            self.handleCollisions()
            self.draw()
            self.clock.tick()

    def updateObjects(self):
        self.background.update()

        for sprite in self.allSprites:
            sprite.update()

        for enemy in self.enemies:
            if enemy.rect.left < 80 and enemy not in self.missedEnemies:
                self.missedEnemies.add(enemy)
                self.player.updateScoreMissedEnemy()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False

                if event.key == K_SPACE and self.player:
                    missile = self.player.fire()
                    if missile:
                        self.missiles.add(missile)
                        self.allSprites.add(missile)

            elif event.type == QUIT:
                self.running = False

            elif event.type == NEW_ENEMY_EVT:
                enemy = Enemy()
                self.enemies.add(enemy)
                self.allSprites.add(enemy)

    def handlePressedKeys(self):
        self.player.handleKeysPressed(pygame.key.get_pressed())

    def handleCollisions(self):
        for missile in self.missiles:
            for enemy in self.enemies:
                if missile.rect.colliderect(enemy.rect):
                    missile.kill()
                    enemy.die()
                    self.player.updateScoreHitEnemy()

        collidedWithEnemy = pygame.sprite.spritecollideany(self.player, self.enemies)
        if collidedWithEnemy:
            self.player.enemyCollision(collidedWithEnemy)

    def draw(self):
        self.background.draw()

        for entity in self.allSprites:
            SCREEN.blit(entity.image, entity.rect)

        fpsLabel = self.font.render("FPS: " + str(int(self.clock.get_fps())), True, (255, 255, 255))
        SCREEN.blit(fpsLabel, (10, 10))

        playerScoreLabel = self.font.render("Score: " + str(int(self.player.score)), True,
                                            (0, 255, 0) if self.player.score >= 0 else (255, 0, 0))
        SCREEN.blit(playerScoreLabel, (SCREEN.get_width() - 130, 10))

        pygame.display.flip()


def main():
    global SCREEN

    pygame.init()
    SCREEN = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("UFO Fighter")
    pygame.display.set_icon(pygame.image.load('ufo_96.png'))

    controller = Controller()

    controller.run()

main()