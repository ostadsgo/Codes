import pygame as pg
import os

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

# Setup assets folder
game_folder = os.path.dirname(__file__)
img_foler = os.path.join(game_folder, "img")


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(os.path.join(img_foler, "jump.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.x = -50


# initial pg and create main window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

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
