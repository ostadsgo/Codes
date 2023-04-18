# Jumpy platform game.
import pygame as pg
from settings import *
from sprite import *


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        # sprite groups
        self.all_sprites = pg.sprite.Group()
        self.paltforms = pg.sprite.Group()

    # start new game if you lose.
    def new(self):
        # make a player
        self.player = Player()
        self.all_sprites.add(self.player)
        # make a platform
        p1 = Platform(0, HEIGHT - 40, WIDTH, 60)
        p2 = Platform(WIDTH / 2, 450, 100, 10)
        self.all_sprites.add(p1)
        self.all_sprites.add(p2)
        self.paltforms.add(p1)
        self.paltforms.add(p2)
        # run the game
        self.run()

    # Game loop
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.paltforms, False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


game = Game()
game.show_start_screen()
while game.running:
    game.new()
    game.show_start_screen()
pg.quit()
