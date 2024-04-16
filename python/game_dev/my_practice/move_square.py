import random
import sys

import pygame as pg


x: int = 0
name: str = "John Doe"

def main() -> int:
    screen_width = 600
    screen_hight = 600
    # Create screen
    screen = pg.display.set_mode((screen_width, screen_hight))
    clock = pg.time.Clock()
    FPS = 30
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    SPEED = 50

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
                    rect.x += SPEED
                if event.key == pg.K_LEFT:
                    rect.x -= SPEED
                if event.key == pg.K_UP:
                    rect.y -= SPEED
                if event.key == pg.K_DOWN:
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
