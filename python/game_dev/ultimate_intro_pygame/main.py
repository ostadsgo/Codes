from pathlib import Path

import pygame as pg

TITLE = "My Game"
WIDTH = 800
HEIGHT = 450
SCREEN_SIZE = (WIDTH, HEIGHT)
FPS = 60
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "img"
SOUND_DIR = BASE_DIR / "snd"
FONT_DIR = BASE_DIR / "font"
GROUND = HEIGHT - 150

pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

# Text
font = pg.font.Font(FONT_DIR / "Pixeltype.ttf", 40)
score = font.render("Points : 0", False, (64, 64, 64))
score_rect = score.get_rect(center=(WIDTH // 2, 50))

# Graphics
sky = pg.image.load(IMAGE_DIR / "Sky.png")
ground = pg.image.load(IMAGE_DIR / "ground.png").convert_alpha()
snail = pg.image.load(IMAGE_DIR / "snail" / "snail1.png").convert_alpha()
snail_rect = snail.get_rect(midbottom=(WIDTH - 100, GROUND))
snail_x = 600

# Player
player = pg.image.load(IMAGE_DIR / "Player" / "player_walk_1.png")
player_rect = player.get_rect(midbottom=(100, GROUND))
player_gravity = 0

running = True
while running:
    # Event handling.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and player_rect.bottom == GROUND:
                    player_gravity = -20

    screen.fill((0, 0, 0))
    # ----- Showing graphics -----
    screen.blit(sky, (0, 0))
    pg.draw.rect(screen, "#c0e8ec", score_rect)
    screen.blit(score, score_rect)
    screen.blit(ground, (0, GROUND))
    # ----- snail -----
    screen.blit(snail, snail_rect)
    snail_rect.x -= 5
    if snail_rect.left < -50:
        snail_rect.left = WIDTH + 50
    # ------ player ------
    screen.blit(player, player_rect)
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom > GROUND:
        player_rect.bottom = GROUND

    # collision between player and snail

    # Draw the images by FPS
    clock.tick(FPS)
    pg.display.update()

pg.quit()
