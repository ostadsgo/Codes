import sys

import pygame as pg

x: int = 0

def draw_grid(screen):
    for x in range(0, 600, 50):
        for y in range(0, 600, 50):
            rect = pg.Rect(x, y, 50, 50)
            pg.draw.rect(screen, "#373737", rect, 1)


def main():
    screen_width = 600
    screen_hight = 600
    # Create screen
    screen = pg.display.set_mode((screen_width, screen_hight))
    clock = pg.time.Clock()
    rect = pg.Rect(300, 300, 50, 50)
    direction = "right"
    SPEED = 5
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    draw_grid(screen)

    # create game loop
    running = True
    while running:
        # check for user input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    direction = "right"
                if event.key == pg.K_LEFT:
                    direction = "left"
                if event.key == pg.K_UP:
                    direction = "up"
                if event.key == pg.K_DOWN:
                    direction = "down"

        # move based on direction
        if direction == "right":
            rect.x += SPEED
        if direction == "left":
            rect.x -= SPEED
        if direction == "up":
            rect.y -= SPEED
        if direction == "down":
            rect.y += SPEED

        screen.fill(BLACK)
        pg.draw.rect(screen, GREEN, rect)
        # update game
        pg.display.flip()
        clock.tick(30)

    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
