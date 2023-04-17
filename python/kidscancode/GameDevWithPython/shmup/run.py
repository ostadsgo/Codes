import pygame as pg


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
        self.speedx = 5
        self.go_right = True
        self.go_left = False

    def update(self):
        if self.go_right:
            self.rect.x += self.speedx

        if self.rect.right >= WIDTH:
            self.go_right = False
            self.go_left = True

        if self.go_left:
            self.rect.x -= self.speedx

        if self.rect.left <= 0:
            self.go_left = False
            self.go_right = True


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
