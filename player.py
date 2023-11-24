import pygame as pg
from settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS

    def movement(self):
        dx, dy = 0, 0
        self.vel = (PLAYER_SPEED * self.game.deltatime) / 200
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.y -= self.vel
        if keys[pg.K_s]:
            self.y += self.vel 
        if keys[pg.K_a]:
            self.x -= self.vel
        if keys[pg.K_d]:
            self.x += self.vel
            
        #print('x: ', self.x, 'y: ', self.y)
        self.check_collider()

    def check_collider(self):
       pass 

    def update(self):
        self.movement()
        #self.check_collider()

    def draw(self):
        pg.draw.rect(self.game.screen, 'yellow', (self.x * 100, self.y * 100, PLAYER_SIZE_SCALE, PLAYER_SIZE_SCALE))

