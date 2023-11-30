import pygame as pg
from settings import *

class BulletHandler:
    def __init__(self, main):
        self.bullet_list = []
        for i in range(BULLET_CACHE):
            bullet_stats= {}
            bullet_stats['count'] = i
            bullet_stats['throw_position'] = (0, 0)
            bullet_stats['throw_direction'] = 0
            bullet_stats['speed'] = 0

            bullet_instance = Bullet(bullet_stats)

            self.bullet_list.append(bullet_instance)
            print(self.bullet_list)

class Bullet:
    def __init__(self, bullet_dict):
        pass
            
    def __str__(self):
        pass

    def shot(self, x, y, speed, direction):
        print('coordenates: ', x, ' ', y, ' speed: ', speed, ' direction: ', direction)

    def check_collider(self):
        pass

    def movement(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


