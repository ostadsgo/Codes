import random
import sys

import pygame as pg


def main():
    screen_width = 600
    screen_hight = 600
    # Create screen
    screen = pg.display.set_mode((screen_width, screen_hight))
    clock = pg.time.Clock()
    FPS = 30
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    SPEED = 5
    direction = "right"

    # draw square 50 x 50
    rect = pg.Rect(300, 300, 50, 50)

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
            # print("pressing RIGHT key", rect.x)
        # Fill the screen, (simulate clear screen)
        screen.fill(BLACK)
        # draw
        pg.draw.rect(screen, GREEN, rect)

        # update game
        pg.display.flip()

        # frame rate / aka wait to see the screen change
        clock.tick(FPS)

    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
