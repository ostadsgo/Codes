import random
import sys
import time

import pygame as pg


def get_random_color():
    """Creae random color in RGB format."""
    return [random.randrange(0, 255) for _ in range(3)]


def main():
    screen_width = 600
    screen_hight = 600
    # Create screen
    screen = pg.display.set_mode((screen_width, screen_hight))
    clock = pg.time.Clock()

    i = 1
    # create game loop
    running = True
    while running:
        
        # check for user input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # proccess / do some actions based on input

        # update game
        color = get_random_color()
        screen.fill(color)
        pg.display.flip()

        print("berfore tick", i)
        # frame rate / aka wait to see the screen change
        clock.tick(2)
        print("after tick", i)
        
        i += 1

    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
