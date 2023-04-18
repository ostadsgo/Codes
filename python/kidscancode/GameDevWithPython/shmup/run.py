import pygame as pg
import random


WIDTH = 360
HEIGHT = 480
SCREEN_SIZE = (WIDTH, HEIGHT)
FPS = 30
TITLE = "My Game"

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.go_right = True
        self.go_left = False

    def update(self):
        self.speedx = 0
        keystate = pg.key.get_pressed()

        if keystate[pg.K_LEFT]:
            self.speedx = -5
        if keystate[pg.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        # check wall
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Mob(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        # position of the mob
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, 40)
        self.speedy = random.randrange = (1, 8)

    def update(self):
        self.rect.y += self.speedy


# initial pg and create main window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Player()
mob = Mob()
all_sprites.add(player)
all_sprites.add(mob)


running = True
while running:
    # keep running at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pg.event.get():
        # Check for closing window
        if event.type == pg.QUIT:
            running = False

    # update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything flip the display
    pg.display.flip()

pg.quit()
