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

centers = [
    (1, 1),
    (1, 1),
    (1, 1),
    None,
    (1, 1),
    (1, 1),
    (1, 0)

]

def generate_random_structure(x, y, game):
    blocks = []
    color_idx = random.randrange(len(colors))

    template_idx = random.randrange(len(templates))
    template = templates[template_idx]
    center = centers[template_idx]
    for r, row in enumerate(template):
        for c, value in enumerate(row):
            if value == 1:
                blocks.append(block.Block(x + c, y + r, game, colors[color_idx], border_colors[color_idx]))
    if center is not None:
        return Structure(game, blocks, color_idx, (x + center[0], y + center[1]))
    else:
        return Structure(game, blocks, color_idx, None)

class Structure:
    def __init__(self, game, blocks, color_idx, center):
        self.game = game
        self.blocks = blocks
        self.color_idx = color_idx
        self.can_move = True
        self.can_move_left = True
        self.can_move_right = True
        self.center = center

    def render(self):
        for block in self.blocks:
            block.render()

    def move(self, p, q):
        if self.can_move and self.check_if_move_possible(p, q):
            for block in self.blocks:
                self.game.map[block.y][block.x] = 0
                block.x += q
                block.y += p
                self.game.map[block.y][block.x] = 1
                # self.game.map[block.y][block.x] = 0
                # if block.x + q in range(self.game.COLUMNS) and self.game.map[block.y][block.x + q] != 2:
                #     block.x += q
                # if block.y + p >= 0 and block.y + p < self.game.ROWS - 1 and self.game.map[block.y + p + 1][block.x] != 2:
                #     block.y += p
                # else:
                #     block.y += p
                #     self.can_move = False
                # self.game.map[block.y][block.x] = 1
            if self.center is not None:
                self.center = (self.center[0] + q, self.center[1] + p)

    def check_if_move_possible(self, p, q):
        possible = True
        for block in self.blocks:
            if block.x + q in range(self.game.COLUMNS) and self.game.map[block.y][block.x + q] == 2:
                possible = False
            elif block.x + q not in range(self.game.COLUMNS):
                possible = False

            if block.y + p in range(self.game.ROWS) and self.game.map[block.y + p][block.x] == 2:
                possible = False
                self.can_move = False
            elif block.y + p not in range(self.game.ROWS):
                possible = False
                self.can_move = False
        return possible

    def rotate(self):
        if self.center is not None and self.check_if_rotation_possible():
            for block in self.blocks:
                point = (block.x, block.y)
                rotated_x = self.center[0] + (point[1] - self.center[1])
                rotated_y = self.center[1] - (point[0] - self.center[0])

                self.game.map[block.y][block.x] = 0
                self.game.map[rotated_y][rotated_x] = 1
                block.x = rotated_x
                block.y = rotated_y
    def check_if_rotation_possible(self):
        possible = True
        for block in self.blocks:
            point = (block.x, block.y)
            rotated_x = self.center[0] + (point[1] - self.center[1])
            rotated_y = self.center[1] - (point[0] - self.center[0])
            try: # checks if the rotated coordinates aren't outside the map or a placed block
                if self.game.map[rotated_y][rotated_x] == 2:
                    possible = False
            except:
                possible = False
                break
        return possible

    def place(self):
        for block in self.blocks:
            self.game.map[block.y][block.x] = 2