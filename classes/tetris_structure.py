import random
from classes import block

import pygame

def generate_random_structure(x, y, game):
    blocks = []
    remaining_blocks = 3
    blocks.append(block.Block(x, y))
    while remaining_blocks > 0:
        pass


class Structure:
    def __init__(self, game, blocks, color):
        self.game = game
        self.blocks = blocks
        self.color = color

