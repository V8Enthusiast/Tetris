import random
from classes import block
import pygame

colors = [(0,173,238), (27,116,187), (246,146,30), (255,241,0), (139,197,63), (101,45,144),(236,27,36)]
border_colors = [(105,206,244), (178,206,230), (248,187,117), (251,249,200), (213,234,188), (155,119,183), (242,109,114)]

templates = [
    [
        [0, 1, 0],
        [1, 1, 1]
    ],
    [
        [1, 0, 0],
        [1, 1, 1]
    ],
    [
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [1, 1],
        [1, 1]
    ],
    [
        [1, 1, 0],
        [0, 1, 1]
    ],
    [
        [0, 1, 1],
        [1, 1, 0]
    ],
    [
        [1, 1, 1, 1]
    ]
]

def generate_random_structure(x, y, game):
    blocks = []
    color_idx = random.randrange(len(colors))

    template = random.choice(templates)
    for r, row in enumerate(template):
        for c, value in enumerate(row):
            if value == 1:
                blocks.append(block.Block(x + c, y + r, game, colors[color_idx], border_colors[color_idx]))
    return Structure(game, blocks, color_idx)


class Structure:
    def __init__(self, game, blocks, color_idx):
        self.game = game
        self.blocks = blocks
        self.color_idx = color_idx
        self.can_move = True

    def render(self):
        for block in self.blocks:
            block.render()

    def move(self, p, q):
        if self.can_move:
            for block in self.blocks:
                self.game.map[block.y][block.x] = 0
                if block.x + q >= 0 and block.x + q < self.game.COLUMNS and self.game.map[block.y][block.x + q] != 2:
                    block.x += q
                if block.y + p >= 0 and block.y + p < self.game.ROWS - 1 and self.game.map[block.y + p + 1][block.x] != 2:
                    block.y += p
                else:
                    block.y += p
                    self.can_move = False
                self.game.map[block.y][block.x] = 1
    def place(self):
        for block in self.blocks:
            self.game.map[block.y][block.x] = 2