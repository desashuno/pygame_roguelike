import pygame as pg
from settings import *
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        dx, dy = 0, 0
        self.speed = (PLAYER_SPEED * self.game.deltatime) / 200
        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dy += -self.speed
        if keys[pg.K_s]:
            dy += self.speed
        if keys[pg.K_a]:
            dx += -self.speed
        if keys[pg.K_d]:
            dx += self.speed
            
        #print('x: ', self.x, 'y: ', self.y)
        self.check_collider(dx, dy)

    def check_wall_col(self, x, y):
        return (x, y) not in self.game.map.room_map_walls

    def check_collider(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.deltatime
        if self.check_wall_col(int(self.x + dx * scale), int(self.y)):            
            self.x += dx
        if self.check_wall_col(int(self.x), int(self.y + dy * scale)):            
            self.y += dy

    def update(self):
        self.movement()
        #self.check_collider()

    def draw(self):
        pg.draw.circle(self.game.screen, 'yellow', (self.x * 100, self.y * 100), 32)

