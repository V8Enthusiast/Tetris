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
        self.block_spawner_x = self.COLUMNS // 2 - 2
        self.placed_structures = []
        self.current_structure = tetris_structure.generate_random_structure(self.block_spawner_x, 0, self)
        pygame.mouse.set_pos(self.x_offset + self.block_spawner_x * self.tile_size, self.y_offset + self.app.height/2)
        self.clock = pygame.time.Clock()
        self.fps = 5

    def render(self):
        for r_idx, r in enumerate(self.map):
            for c_idx, c in enumerate(r):
                rect = pygame.Rect(self.x_offset + c_idx * self.tile_size, self.y_offset + r_idx * self.tile_size, self.tile_size, self.tile_size)
                pygame.draw.rect(self.app.screen, (100, 100, 100), rect)
                pygame.draw.rect(self.app.screen, (40, 40, 40), rect, self.border)
        for structure in self.placed_structures:
            structure.render()
        self.current_structure.render()
        self.current_structure.move(1, 0)
        if self.current_structure.can_move is False:
            self.placed_structures.append(self.current_structure)
            self.current_structure.place()
            self.current_structure = tetris_structure.generate_random_structure(self.block_spawner_x, 0, self)
        self.clock.tick(self.fps)



    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.current_structure.move(1, 0)
                if event.key == pygame.K_SPACE:
                    self.current_structure = tetris_structure.generate_random_structure(self.block_spawner_x, 0, self)

