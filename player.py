import pygame as pg
from settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        self.dx, self.dy = 0, 0
        self.speed = (PLAYER_SPEED * self.game.deltatime) / 200
        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.dy += -self.speed
        if keys[pg.K_s]:
            self.dy += self.speed
        if keys[pg.K_a]:
            self.dx += -self.speed
        if keys[pg.K_d]:
            self.dx += self.speed

        #
        #    dx = 1/math.sqrt(2)
        #    dy = 1/math.sqrt(2)
            
        #print('x: ', self.x, 'y: ', self.y)
        self.check_collider()

    def check_wall_col(self, x, y):
        return (x, y) not in self.game.map.room_map_walls

    def check_collider(self):
        scale = PLAYER_SIZE_SCALE / self.game.deltatime
        if self.check_wall_col(int(self.x + self.dx * scale), int(self.y)):            
            self.x += self.dx
        if self.check_wall_col(int(self.x), int(self.y + self.dy * scale)):            
            self.y += self.dy

    def dev_info(self):
        print('Player Info')
        print('-----------')
        print('dx: ', self.dx, ' dy: ', self.dy)
        print('x: ', self.x, ' dy: ', self.y)

    def update(self):
        self.movement()
        #self.check_collider()

    def draw(self):
        pg.draw.circle(self.game.screen, 'yellow', (self.x * 100, self.y * 100), 32)

