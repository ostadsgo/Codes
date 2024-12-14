import pygame as pg


pg.init()

# screen
width = 600
height = 400
screen_size = (width, height)
title = "Snake game"

screen = pg.display.set_mode(screen_size)
pg.display.set_caption(title)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT():
            running = False

    screen.fill((255, 255, 255))
    pg.display.flip()

pg.quit()
