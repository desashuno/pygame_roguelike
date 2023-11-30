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
        self.room_map_walls = []

        self.test_room = [[NW,WN,WN,WN,WN,WN,WN,WN,WN,WN,NE],
                          [WW, _, _, _, _, _, _, _, _, _,WE],
                          [WW, _, _, _, _, _, _, _, _, _,WE],
                          [WW, _, _, _, _, _, _, _, _, _,WE],
                          [WW, _, _, _, _, _, _, _, _, _,WE],
                          [WW, _, _, _, _, _, _, _, _, _,WE],
                          [SW,WS,WS,WS,WS,WS,WS,WS,WS,WS,SE]]

        self.actual_room = self.test_room
        self.get_map()
        
    def get_map(self):
        for j, row in enumerate(self.actual_room):
            for i, value in enumerate(row):
                if value == 'floor':
                    self.actual_room[j][i] = False

        for j, row in enumerate(self.actual_room):
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
                if value != False:
                    self.room_map_walls.append((i, j))

    def draw(self):
        self.draw_background()
        self.draw_walls()

    def draw_background(self):
        self.game.screen.fill('green')

    def draw_walls(self):
        for pos in self.room_map:
            if self.room_map[pos] == 110:
                pg.draw.rect(self.game.screen, 'darkgray', (pos[0] *100, pos[1] * 100, 100, 100))
            elif self.room_map[pos] == 120:
                pg.draw.rect(self.game.screen, 'darkblue', (pos[0] *100, pos[1] * 100, 100, 100))
            elif self.room_map[pos] == 130:
                pg.draw.rect(self.game.screen, 'cyan', (pos[0] * 100, pos[1] *100, 100, 100))
            elif self.room_map[pos] == 140:
                pg.draw.rect(self.game.screen, 'darkgreen', (pos[0] * 100, pos[1] *100, 100, 100))
            elif self.room_map[pos] == 210:
                pg.draw.rect(self.game.screen, 'yellow', (pos[0] * 100, pos[1] *100, 100, 100))
            elif self.room_map[pos] == 220:
                pg.draw.rect(self.game.screen, 'black', (pos[0] * 100, pos[1] *100, 100, 100))
            elif self.room_map[pos] == 230:
                pg.draw.rect(self.game.screen, 'white', (pos[0] * 100, pos[1] *100, 100, 100))
            elif self.room_map[pos] == 240:
                pg.draw.rect(self.game.screen, 'blue', (pos[0] * 100, pos[1] *100, 100, 100))

