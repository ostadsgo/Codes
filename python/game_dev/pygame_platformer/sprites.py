import pygame as pg
import settings

vec = pg.math.Vector2

class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width // 2, height // 2))
        return image


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = self.game.spritesheet.get_image(614, 1063, 120, 191)
        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH // 2, settings.HEIGHT // 2)
        self.pos = vec(settings.WIDTH // 2, settings.HEIGHT // 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, settings.PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -settings.PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = settings.PLAYER_ACC

        self.acc.x += self.vel.x * settings.PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > settings.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = settings.WIDTH

        self.rect.midbottom = (int(self.pos.x), int(self.pos.y))

    def jump(self):
        # jump only if standing on platform
        self.rect.x += 1  # move player one pixel below to see if he is on a platform.
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = settings.PLAYER_JUMP


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pg.Surface((w, h))
        self.image.fill(settings.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
