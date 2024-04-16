from sys import exit

import pygame as pg


class Score:
    def __init__(self):
        self.font = pg.font.Font("./font/Pixeltype.ttf", 40)
        self.text = self.font.render("Score: 0", False, "Black")

    # update score
    def update(self, value):
        pass


class Snail:
    def __init__(self):
        self.surf = pg.image.load("./graphics/snail/snail1.png").convert_alpha()
        self.x = 600

    def update(self):
        self.x -= 5
        if self.x < -50:
            self.x = 900


class Game:
    def __init__(self):
        pg.init()
        self.width = 800
        self.height = 400
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.fps = 60
        # surfaces
        self.sky = pg.image.load("./graphics/Sky.png")
        self.ground = pg.image.load("./graphics/ground.png")
        self.score = Score()
        self.snail = Snail()

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
            self.screen.blit(self.sky, (0, 0))
            self.screen.blit(self.ground, (0, self.height // 2 + 50))
            self.screen.blit(self.score.text, (self.width // 2 - 50, 10))
            # snail
            self.screen.blit(self.snail.surf, (self.snail.x, self.height - 180))
            self.snail.update()

            # update main screen
            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.run()
