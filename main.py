import pygame as pg
import sys
from map import Map
from settings import *


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('THE BINDING OF XAVI')
        self.screen = pg.display.set_mode(RES)

        self.clock = pg.time.Clock()
        self.deltatime = 1

        self.start_modules()

    def start_modules(self):
        self.map = Map(self)        

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def update(self):
        pg.display.flip()
        self.deltatime = self.clock.tick(FPS)

    def draw(self):
        self.screen.fill('black')

    def run(self):
        while True:
            self.events()
            self.update()
            self.draw()



if __name__ == "__main__":
    game = Game()
    game.run()
