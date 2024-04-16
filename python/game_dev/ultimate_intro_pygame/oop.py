from sys import exit

import pygame as pg


class Player:
    def __init__(self):
        pass


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((400, 500))
        self.clock = pg.time.Clock()
        self.fps = 60
        self.square = pg.Surface((50, 50))
        self.square.fill("Green")

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            # other event

    def run(self):
        running = True
        while running:
            # check event
            self.check_event()

            self.screen.fill((0, 0, 0))

            # display other surfaces
            self.screen.blit(self.square, (200, 200))

            # update main screen
            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.run()
