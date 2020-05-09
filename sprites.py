import pygame as pg
from settings import *
import pokebase as pb
import random

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):

    def __init__(self, game):

        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load('R1.png')
        self.rect = self.image.get_rect()
        self.pos = vec(75, 3*WIDTH/4)
        self.rect.centerx = (self.pos.x)
        self.rect.centery = (self.pos.y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):

        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()

        self.rect.y += 1
        dhit = pg.sprite.spritecollide(self, self.game.landtiles, False)
        self.rect.y -= 1

        if(dhit):
            
            self.rect.x += -20
            rhit = pg.sprite.spritecollide(self, self.game.platforms, False)
            self.rect.x -= 40
            lhit = pg.sprite.spritecollide(self, self.game.platforms, False)
            self.rect.x += -20

            # print(rhit)
            # print(lhit)
            # print('\n')

            if(rhit and lhit):
                pass
            elif(rhit):
                if(keys[pg.K_LEFT]):
                    self.pos.x -= 5
            elif(lhit):
                if(keys[pg.K_RIGHT]):
                    self.pos.x += 5
            else:
                if(keys[pg.K_LEFT]):
                    self.pos.x -= 5
                if(keys[pg.K_RIGHT]):
                    self.pos.x += 5


            if(keys[pg.K_UP]):
                self.acc.y -= 20
                self.vel.y += self.acc.y
                self.pos.y += self.vel.y
                self.rect.centery = self.pos.y
                
            
            print(self.vel.y)
            self.rect.centerx = self.pos.x


            

        else:

            self.rect.x += -20
            rhit = pg.sprite.spritecollide(self, self.game.platforms, False)
            self.rect.x -= 40
            lhit = pg.sprite.spritecollide(self, self.game.platforms, False)
            self.rect.x += -20


            if(rhit and lhit):
                print('')
            elif(rhit):
                if(keys[pg.K_LEFT]):
                    self.pos.x -= 5
            elif(lhit):
                if(keys[pg.K_RIGHT]):
                    self.pos.x += 5
            else:
                if(keys[pg.K_LEFT]):
                    self.pos.x -= 5
                if(keys[pg.K_RIGHT]):
                    self.pos.x += 5

            self.acc.y = 0.5
            self.vel += self.acc
            self.pos += self.vel
            self.rect.center = self.pos

            


        # if hits:
        #     self.rect.y -= 1   
        #     self.vel.x += self.acc.x
        #     self.pos.x += self.vel.x
        #     self.rect.center = self.pos
        # else:

        #     self.rect.y -= 1
        #     self.vel += self.acc
        #     self.pos += self.vel
        #     self.rect.center = self.pos

        


class Land(pg.sprite.Sprite):

    def __init__(self, x):

        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('grass.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, HEIGHT-20)
        # self.pos = vec(HEIGHT, self.x)

    def update(self):
        pass


class Platforms(pg.sprite.Sprite):

    def __init__(self):

        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('grass.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(200, WIDTH), random.randint(200, HEIGHT - 100))


class Pokeballs(pg.sprite.Sprite):

    def __init__(self):

        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('grass.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(200, WIDTH), random.randint(200, HEIGHT - 100))


class Pokemons(pg.sprite.Sprite):

    def __init__(self):

        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('grass.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(200, WIDTH), random.randint(200, HEIGHT - 100))


