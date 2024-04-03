import pygame

class TetrisGame:
    def __init__(self, app, rows, colums):
        self.app = app
        self.ROWS = rows
        self.COLUMNS = colums
        self.buttons = []
        self.map = [[0 for _ in range(colums)] for i in range(rows)]
        self.tile_size = 50
        self.offset = (self.app.width - self.tile_size * self.COLUMNS) / 2

    def render(self):
        for r_idx, r in enumerate(self.map):
            for c_idx, c in enumerate(r):
                pygame.draw.rect(self.app.screen, (255, 255, 255), (self.offset + c_idx * self.tile_size, r_idx * self.tile_size, self.tile_size, self.tile_size))


    def events(self):
        pass