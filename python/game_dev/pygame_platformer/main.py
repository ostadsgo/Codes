import random
import pygame as pg
import settings
from sprites import Platform, Player


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
        # start new game after `game over`
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in settings.PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
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
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def update(self):
        self.all_sprites.update()
        # if player hits a platform - only falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        # player reaches 1/4 height of the screen.
        if self.player.rect.top <= settings.HEIGHT / 4:
            self.player.pos.y += (self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                # delete platforms under screen
                if plat.rect.top > settings.HEIGHT:
                    plat.kill()

        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            x = random.randrange(0, settings.WIDTH - width)
            y = random.randrange(-75, -30)
            p = Platform(x, y, width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)


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
