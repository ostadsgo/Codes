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


# initial pg and create main window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()


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
