import random
from os import path

import pygame as pg
import settings as st
from sprites import Platform, Player, Spritesheet


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((st.WIDTH, st.HEIGHT))
        pg.display.set_caption(st.TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(st.FONT_NAME)
        self.highscore = 0
        self.dir = path.dirname(__file__)
        self.img_dir = path.join(self.dir, "img")
        self.snd_dir = path.join(self.dir, "snd")
        self.load_data()

    def load_data(self):
        # highscore file
        with open(path.join(self.dir, st.HS_FILE), "r+") as f:
            try:
                self.highscore = int(f.read())
            except ValueError:
                self.highscore = 0
        # load spritesheet
        self.spritesheet = Spritesheet(path.join(self.img_dir, st.SPRITESHEET))

        # -- load sounds
        self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir, "Jump33.wav"))
        self.jump_sound.set_volume(0.5)

    def new(self):
        self.score = 0
        self.playing = True
        # start new game after `game over`
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in st.PLATFORM_LIST:
            p = Platform(self, *plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        pg.mixer.music.load(path.join(self.snd_dir, "Happy Tune.ogg"))
        self.run()

    def run(self):
        # play background music
        pg.mixer.music.play(loops=-1)
        # game loop
        while self.playing:
            self.clock.tick(st.FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(500)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()

    def update(self):
        self.all_sprites.update()
        # if player hits a platform - only falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.y < lowest.rect.centery:
                    self.player.pos.y = lowest.rect.top
                    self.player.vel.y = 0
                    self.player.jumping = False

        # player reaches 1/4 height of the screen.
        if self.player.rect.top <= st.HEIGHT / 4:
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.vel.y), 2)
                # delete platforms under screen
                if plat.rect.top > st.HEIGHT:
                    plat.kill()
                    self.score += 10

        # Die
        if self.player.rect.bottom > st.HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            self.playing = False

        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            x = random.randrange(0, st.WIDTH - width)
            y = random.randrange(-75, -30)
            p = Platform(self, x, y)
            self.platforms.add(p)
            self.all_sprites.add(p)

    def draw(self):
        self.screen.fill(st.BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        self.draw_text(str(self.score), 22, st.WHITE, st.WIDTH / 2, 15)
        pg.display.flip()

    def show_start_screen(self):
        pg.mixer.music.load(path.join(self.snd_dir, "Yippee.ogg"))
        pg.mixer.music.play(loops=-1)
        pg.mixer.music.set_volume(.5)
        self.screen.fill(st.BGCOLOR)
        self.draw_text(st.TITLE, 48, st.WHITE, st.WIDTH / 2, st.HEIGHT / 4)
        self.draw_text(
            "Arrows to move, Space to jump", 22, st.WHITE, st.WIDTH / 2, st.HEIGHT / 2
        )
        self.draw_text(
            "Press a key to play", 22, st.WHITE, st.WIDTH / 2, st.HEIGHT * 3 / 4
        )
        self.draw_text(f"High Score: {self.highscore}", 22, st.WHITE, st.WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def show_game_over_screen(self):
        if not self.running:
            return

        pg.mixer.music.load(path.join(self.snd_dir, "Yippee.ogg"))
        pg.mixer.music.play(loops=-1)
        pg.mixer.music.set_volume(.5)

        self.screen.fill(st.BGCOLOR)
        self.draw_text("Game Over", 48, st.WHITE, st.WIDTH / 2, st.HEIGHT / 4)
        self.draw_text(
            "score: " + str(self.score), 22, st.WHITE, st.WIDTH / 2, st.HEIGHT / 2
        )
        self.draw_text(
            "Press any key to play again", 22, st.WHITE, st.WIDTH / 2, st.HEIGHT * 3 / 4
        )
        self.draw_text(f"High Score: {self.highscore}", 22, st.WHITE, st.WIDTH / 2, 15)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text(
                "NEW HIGH SCORE: " + str(self.highscore),
                22,
                st.WHITE,
                st.WIDTH / 2,
                st.HEIGHT / 2 + 40,
            )

        # write highscore
        with open(path.join(self.dir, st.HS_FILE), "w") as f:
            f.write(str(self.highscore))

        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(st.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surf, text_rect)


game = Game()
game.show_start_screen()
while game.running:
    game.new()
    game.show_game_over_screen()

pg.quit()
