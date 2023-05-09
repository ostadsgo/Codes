from pathlib import Path
import pygame as pg

TITLE = "My Game"

WIDTH = 1000
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)
FPS = 60
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "img"
SOUND_DIR = BASE_DIR / "snd"
FONT_DIR = BASE_DIR / "font"


pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

# Text
font = pg.font.Font(FONT_DIR / "freecam.ttf")
text = font.render("Points : 0", False, "Black")

# Graphics
bg = pg.image.load(IMAGE_DIR / "bg.jpg")
bg = pg.transform.scale(bg, SCREEN_SIZE)
ground = pg.image.load(IMAGE_DIR / "ground.png")
snail = pg.image.load(IMAGE_DIR / "snail1.png")
snail_x = WIDTH - 100

running = True
while running:
    # Event handling.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Showing graphics
    screen.blit(bg, (0, 0))
    screen.blit(text, (10, 10))
    screen.blit(ground, (0, HEIGHT - 150))
    screen.blit(snail, (snail_x, HEIGHT - 150))
    if snail_x > -20:
        snail_x -= 5
    else:
        snail_x = WIDTH + 20

    # Draw the images by FPS
    clock.tick(FPS)
    pg.display.update()

pg.quit()
