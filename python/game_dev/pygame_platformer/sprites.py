import pygame as pg
import settings

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((30, 40))
        self.image.fill(settings.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH // 2, settings.HEIGHT // 2)
        self.pos = vec(settings.WIDTH // 2, settings.HEIGHT // 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -settings.PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = settings.PLAYER_ACC

        self.acc += self.vel * settings.PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > settings.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = settings.WIDTH

        self.rect.center = (int(self.pos.x), int(self.pos.y))
