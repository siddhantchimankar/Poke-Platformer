import pygame as pg
import random
from settings import *
from sprites import *

class Game:

    def __init__(self):

        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("firstgame")
        self.clock = pg.time.Clock()
        self.running = True

    def newGame(self):

        self.allsprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.pokeballs = pg.sprite.Group()
        self.pokemons = pg.sprite.Group()
        self.landtiles = pg.sprite.Group()

        self.player1 = Player(self)
        self.land = Land(20)
        self.landtiles.add(self.land)
        self.allsprites.add(self.player1)
        self.allsprites.add(self.land)
        
        for i in range(25):
            self.land = Land(20*i)
            self.allsprites.add(self.land)
            self.landtiles.add(self.land)

        for i in range(random.randint(3, 6)):
            self.plat = Platforms()
            self.allsprites.add(self.plat)
            self.platforms.add(self.plat)



        self.run()


    def run(self):

        self.playing = True
        while(self.playing):
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        self.player1.update()


    def events(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
            self.running = False

        

    def draw(self):

        self.screen.fill(BLACK)
        self.allsprites.draw(self.screen)

        pg.display.flip()



g = Game()

while g.running:
    g.newGame()

pg.quit()

        
