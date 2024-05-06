import time

import pygame
from classes import tetris_structure
colors = [(0,173,238), (27,116,187), (246,146,30), (255,241,0), (139,197,63), (101,45,144),(236,27,36)]

pygame.font.init()
font = pygame.font.Font(None, 24)
class TetrisGame:
    def __init__(self, app, rows, columns):
        self.app = app
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.tile_color = (100, 100, 100)
        self.tile_outline_color = (40, 40, 40)
        self.ROWS = rows
        self.COLUMNS = columns
        self.buttons = []
        self.blocks = {}
        self.map = [[0 for _ in range(columns)] for i in range(rows)]
        self.tile_size = self.app.height/self.ROWS
        self.border = 1
        self.x_offset = (self.app.width - self.tile_size * self.COLUMNS) / 2
        self.y_offset = (self.app.height - self.tile_size * self.ROWS) / 2
        self.block_spawner_x = self.COLUMNS // 2 - 2
        self.placed_structures = []
        self.current_structure = tetris_structure.generate_random_structure(self.block_spawner_x, 0, self)
        pygame.mouse.set_pos(self.x_offset + self.block_spawner_x * self.tile_size, self.y_offset + self.app.height/2)
        self.clock = time.time()
        self.direction_clock = time.time()
        self.move_down_faster = False
        self.move_left = False
        self.move_right = False
        self.moving_speed = 10
        self.accelerated_moving_speed = 20
        self.fps = 1
        self.game_over = False
        self.debug = False
    def reset_game(self):
        self.blocks = {}
        self.map = [[0 for _ in range(self.COLUMNS)] for i in range(self.ROWS)]
        self.placed_structures = []
        self.current_structure = tetris_structure.generate_random_structure(self.block_spawner_x, 0, self)
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
    def draw_tiles(self):
        for r_idx, r in enumerate(self.map):
            for c_idx, c in enumerate(r):
                rect = pygame.Rect(self.x_offset + c_idx * self.tile_size, self.y_offset + r_idx * self.tile_size, self.tile_size, self.tile_size)
                pygame.draw.rect(self.app.screen, self.tile_color, rect)
                pygame.draw.rect(self.app.screen, self.tile_outline_color, rect, self.border)

        for structure in self.placed_structures:
            structure.render()
        self.current_structure.render()
        score_font = pygame.font.SysFont('Impact', 24)
        level_surface = score_font.render(f"Level: {self.level}", True, (255, 255, 255))
        lines_surface = score_font.render(f"Lines Cleared: {self.lines_cleared}", True, (255, 255, 255))
        self.app.screen.blit(level_surface, (10, 10))
        self.app.screen.blit(lines_surface, (10, 40))

        if self.debug:
            for block in self.blocks.values():
                if block is not None:
                    block.render()
            for r_idx, r in enumerate(self.map):
                for c_idx, c in enumerate(r):
                    rect = pygame.Rect(self.x_offset + c_idx * self.tile_size, self.y_offset + r_idx * self.tile_size,
                                       self.tile_size, self.tile_size)
                    text_surface = font.render(str(c), True, (255, 255, 255))
                    text_rect = text_surface.get_rect(center=rect.center)
                    self.app.screen.blit(text_surface, text_rect)
    def check_for_completed_rows(self):
        rows_cleared = 0
        for row_id, row in enumerate(self.map):
            if 0 not in row and 1 not in row:
                rows_cleared += 1
                for i in range(self.COLUMNS):
                    self.map[row_id][i] = 0
                for r in range(row_id, -1, -1):
                    for c in range(self.COLUMNS):
                        if self.map[r][c] == 2 and self.map[r + 1][c] == 0:
                            self.map[r + 1][c] = 2
                            self.map[r][c] = 0
                            # self.blocks[(c, r)].y += 1
                            # self.blocks[(c, r)], self.blocks[(c, r + 1)] = None, self.blocks[(c, r)]
                            # if self.blocks[(c, r + 1)] is not None:
                            #     self.blocks[(c, r + 1)].destroyed = True
                            temp_block = self.blocks[(c, r)]
                            self.blocks[(c, r + 1)] = temp_block
                            self.blocks[(c, r)] = None
                            temp_block.y += 1
        self.lines_cleared += rows_cleared
        if self.lines_cleared >= self.level * 10:
            self.level += 1
        print(f"Level: {self.level}")
        print(f"Lines Cleared: {self.lines_cleared}")
    def render(self):
        if self.game_over:
            self.draw_tiles()
            game_over_font = pygame.font.SysFont('Impact', 148)
            game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
            text_rect = game_over_text.get_rect(center=(self.app.width // 2, self.app.height // 2))
            self.app.screen.blit(game_over_text, text_rect)
        else:
            self.check_for_completed_rows()
            self.draw_tiles()
            if time.time() > self.clock + 1/self.fps or (self.move_down_faster and time.time() > self.clock + 1/self.accelerated_moving_speed):
                self.current_structure.move(1, 0)
                self.clock = time.time()
            if self.move_right and time.time() > self.direction_clock + 1/self.moving_speed:
                self.current_structure.move(0, 1)
                self.direction_clock = time.time()
            if self.move_left and time.time() > self.direction_clock + 1/self.moving_speed:
                self.current_structure.move(0, -1)
                self.direction_clock = time.time()
            if self.current_structure.can_move is False:
                self.placed_structures.append(self.current_structure)
                self.current_structure.place()
                self.current_structure = tetris_structure.generate_random_structure(self.block_spawner_x, 0, self)



    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.run = False
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    self.reset_game()
                else:
                    if event.key == pygame.K_DOWN:
                        self.move_down_faster = True
                    if event.key == pygame.K_UP:
                        self.current_structure.rotate()
                    if event.key == pygame.K_SPACE:
                        self.current_structure = tetris_structure.generate_random_structure(self.block_spawner_x, 0, self)
                    if event.key == pygame.K_LEFT:
                        self.move_left = True
                    if event.key == pygame.K_RIGHT:
                        self.move_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.move_down_faster = False
                if event.key == pygame.K_LEFT:
                    self.move_left = False
                if event.key == pygame.K_RIGHT:
                    self.move_right = False

