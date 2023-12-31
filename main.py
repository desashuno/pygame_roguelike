import pygame as pg
import sys
import os
from map import Map
from player import Player
from settings import *
from bullet import *


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('PG test :)')
        self.screen = pg.display.set_mode(RES)

        self.clock = pg.time.Clock()
        self.deltatime = 1

        self.start_modules()

    def start_modules(self):
        self.map = Map(self)        
        self.player = Player(self)
        self.bullet_handler = BulletHandler(self)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def dev_info(self):
        if sys.platform == 'win32':
            os.system('cls')
        elif sys.platform == 'linux':
            os.system('clear')
        self.player.dev_info() 

    def update(self):
        pg.display.flip()
        self.deltatime = self.clock.tick(FPS)
        self.player.update()

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()

    def run(self):
        while True:
            self.events()
            self.update()
            self.draw()
            self.dev_info()


if __name__ == "__main__":
    game = Game()
    game.run()
