import pygame as pg

# constatnts
WIDTH = 1000
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Runner")
clock = pg.time.Clock()

# Srufaces(Every part of the game; anything on the screen)
bg = pg.image.load("./img/bg.jpg")
bg = pg.transform.scale(bg, SCREEN_SIZE)
ground = pg.image.load("./img/ground2.png")
# font
# font type, font size
test_font = pg.font.Font("./font/freecam.ttf", 50)
# text inft, anti alises, color
text_surface = test_font.render("My Game", False, "Black")
# Snail
snail_surface = pg.image.load("./img/snail1.png")
snail_x_pos = 900

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    # add pictures to the screen.
    # screen.blit(bg, (0, 0))
    # screen.blit(ground, (0, 420))
    # screen.blit(text_surface, (350, 50))
    screen.blit(snail_surface, (snail_x_pos, 420))
    snail_x_pos -= 3
    if snail_x_pos <= 0:
        snail_x_pos = 900

    pg.display.update()
    clock.tick(60)
