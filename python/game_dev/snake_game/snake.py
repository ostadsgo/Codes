import random

import pygame as pg


class Snake:
    def __init__(self):
        self.body = [(1, 1), (2, 1), (3, 1)]
        self.head = self.body[-1]

    def draw(self, screen):
        for x, y in self.body:
            pg.draw.rect(screen, "#00ff00", (x * 50, y * 50, 49, 49))

    def move_right(self):
        pass

    def move_left(self):
        pass


class Food:
    def __init__(self):
        self.eaten = True
        pg.draw.rect(screen, "#ff0000", (300, 350, 50, 50))

    def draw(self, screen, x=300, y=400):
        pg.draw.rect(screen, "#ff0000", (x, y, 50, 50))


def draw_grid(screen, width, height, block_size):
    for x in range(0, width, block_size):
        for y in range(0, height, block_size):
            rect = pg.Rect(x, y, 50, 50)
            pg.draw.rect(screen, "#373737", rect, 1)


pg.init()

TITLE = "My Game"
WIDTH = 600
HEIGHT = 450
BLOCK_SIZE = 50
SCREEN_SIZE = (WIDTH, HEIGHT)
FPS = 60
BLACK = "#000000"
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption(TITLE)
clock = pg.time.Clock()
snake = Snake()
food = Food()

running = True
while running:
    # --- events ---
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                pass
            if event.key == pg.K_LEFT:
                pass
            if event.key == pg.K_UP:
                pass
            if event.key == pg.K_DOWN:
                pass

    # --- draw ---
    screen.fill(BLACK)
    draw_grid(screen, WIDTH, HEIGHT, BLOCK_SIZE)
    snake.draw(screen)
    food.draw(screen)

    # -- collision ---

    # --- update ---
    clock.tick(FPS)
    pg.display.update()

pg.quit()
exit()
