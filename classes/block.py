import pygame

class Block:
    def __init__(self, x ,y, color):
        self.x = x
        self.y = y
        self.color = color
        self.moving = True