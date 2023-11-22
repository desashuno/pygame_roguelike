import pygame as pg


class Map: 
    def __init__(self, main): 
        _ = 'floor'
        
        WN = 'wall_n'
        WS = 'wall_s'
        WE = 'wall_e'
        WW = 'wall_w'

        NW = 'corner_nw'
        NE = 'corner_ne'
        SW = 'corner_sw'
        SE = 'corner_se'
        
        self.room_map = []

        self.test_room = [[WN,WN,WN,WN,WN,WN,WN],
                          [WW, _, _, _, _, _,WE],
                          [WW, _, _, _, _, _,WE],
                          [WW, _, _, _, _, _,WE],
                          [WW, _, _, _, _, _,WE],
                          [WW, _, _, _, _, _,WE],
                          [SW,WS,WS,WS,WS,WS,WS]]

        self.get_map()
        print(self.room_map)

    def get_map(self):
        for j, row in enumerate(self.test_room):
            for i, value in enumerate(row):
               self.room_map.append(value)
