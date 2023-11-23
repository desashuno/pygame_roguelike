import pygame as pg


class Map: 
    def __init__(self, game): 
        self.game = game

        _ = 'floor'
        
        WN = 'wall_n'
        WS = 'wall_s'
        WE = 'wall_e'
        WW = 'wall_w'

        NW = 'corner_nw'
        NE = 'corner_ne'
        SW = 'corner_sw'
        SE = 'corner_se'
        
        self.room_map = {}

        self.test_room = [[NW,WN,WN,WN,WN,WN,WN,WN,WN,WN,NE],
                          [WW, _, _, _, _, _, _, _, _, _,WE],
                          [WW, _, _, _, _, _, _, _, _, _,WE],
                          [WW, _, _, _, _, _, _, _, _, _,WE],
                          [WW, _, _, _, _, _, _, _, _, _,WE],
                          [WW, _, _, _, _, _, _, _, _, _,WE],
                          [SW,WS,WS,WS,WS,WS,WS,WS,WS,WS,SE]]

        self.get_map()
        print(self.room_map)

    def get_map(self):
        for j, row in enumerate(self.test_room):
            for i, value in enumerate(row):
                if value == 'floor':
                    self.test_room[j][i] = False

        for j, row in enumerate(self.test_room):
            for i, value in enumerate(row):
                if value == 'wall_n':
                    self.room_map[(i, j)] = 110
                elif value == 'wall_s':
                    self.room_map[(i, j)] = 120
                elif value == 'wall_e':
                    self.room_map[(i, j)] = 130
                elif value == 'wall_w':
                    self.room_map[(i, j)] = 140
                elif value == 'corner_nw':
                    self.room_map[(i, j)] = 210
                elif value == 'corner_ne':
                    self.room_map[(i, j)] = 220
                elif value == 'corner_sw':
                    self.room_map[(i, j)] = 230
                elif value == 'corner_se':
                    self.room_map[(i, j)] = 240

    def draw(self):
        self.draw_background()
        self.draw_walls()

    def draw_background(self):
        self.game.screen.fill('darkgreen')

    def draw_walls(self):
        for pos in self.room_map:
            pg.draw.rect(self.game.screen, 'darkgray', (pos[0] *100, pos[1] * 100, 100, 100), 2)
