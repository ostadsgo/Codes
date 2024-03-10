import pygame as pg


pg.init()

screen = pg.display.set_mode((400, 300))
pg.display.set_caption("Hello, World")

# game loop
running = True
while running:
    # input handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # Update screen.
    pg.display.update()

pg.quit()
