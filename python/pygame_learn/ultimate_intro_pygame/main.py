from pathlib import Path
import pygame as pg

TITLE = "My Game"

WIDTH = 1100
HEIGHT = 650
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
bg = pg.transform.scale(bg, SCREEN_SIZE).convert()
ground = pg.image.load(IMAGE_DIR / "ground.png").convert_alpha()
ground = pg.transform.scale(ground, (WIDTH, 200)).convert_alpha()
snail = pg.image.load(IMAGE_DIR / "snail1.png").convert_alpha()
snail_x = WIDTH - 100

# Player
player = pg.image.load(IMAGE_DIR / "freeknight/png/Walk (1).png")
player = pg.transform.scale(player, (110, 120)).convert_alpha()
player_rect = player.get_rect()

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
    snail_x -= 5
    if snail_x < -20:
        snail_x = WIDTH + 20
    screen.blit(player, (100, HEIGHT-200))
    

    # Draw the images by FPS
    clock.tick(FPS)
    pg.display.update()

pg.quit()
