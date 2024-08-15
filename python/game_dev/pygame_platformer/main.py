import pygame as pg
import settings
from sprites import Player, Platform


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pg.display.set_caption(settings.TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = True

    def new(self):
        #start new game after `game over`
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        p1 = Platform(0, settings.HEIGHT - 40, settings.WIDTH, 40)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        p2 = Platform(settings.WIDTH / 2 - 50, settings.HEIGHT * 3 / 4, 100, 20)
        self.all_sprites.add(p2)
        self.platforms.add(p2)
        self.run()

    def run(self):
        # game loop
        while self.playing:
            self.clock.tick(settings.FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0

    def draw(self):
        self.screen.fill(settings.BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_game_over_screen(self):
        pass


game = Game()
game.show_start_screen()
while game.running:
    game.new()
    game.show_game_over_screen()
    break

pg.quit()
