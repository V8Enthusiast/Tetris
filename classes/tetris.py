import pygame
from classes import tetris_structure
class TetrisGame:
    def __init__(self, app, rows, colums):
        self.app = app
        self.ROWS = rows
        self.COLUMNS = colums
        self.buttons = []
        self.map = [[0 for _ in range(colums)] for i in range(rows)]
        self.tile_size = self.app.height/self.ROWS
        self.border = 1
        self.x_offset = (self.app.width - self.tile_size * self.COLUMNS) / 2
        self.y_offset = (self.app.height - self.tile_size * self.ROWS) / 2

    def render(self):
        for r_idx, r in enumerate(self.map):
            for c_idx, c in enumerate(r):
                rect = pygame.Rect(self.x_offset + c_idx * self.tile_size, self.y_offset + r_idx * self.tile_size, self.tile_size, self.tile_size)
                pygame.draw.rect(self.app.screen, (100, 100, 100), rect)
                pygame.draw.rect(self.app.screen, (40, 40, 40), rect, self.border)


    def events(self):
        pass