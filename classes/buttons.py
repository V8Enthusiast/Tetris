import random
from classes import tetris
from classes import settings
import pygame

import pygame
import colorsys

colors = [(0,173,238), (27,116,187), (246,146,30), (255,241,0), (139,197,63), (101,45,144),(236,27,36)]

class Button:
    def __init__(self, width, height, x, y, translucent, font, text, bgcolor, fgcolor, function, app):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.font_type = font
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.app = app
        self.text = text
        self.function = function
        self.outline_color = (255, 255, 255)  # Initial outline color
        self.hue = 0  # Starting hue
        self.hover_color = random.choice(colors)

        pygame.font.init()

    def render(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.Font(self.font_type, int(32 * self.app.scale))
        self.display_text = self.font.render(self.text, True, self.fgcolor)
        self.display_text_rect = self.display_text.get_rect()
        self.display_text_rect.center = self.rect.center

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            current_bg_color = self.hover_color
        else:
            current_bg_color = self.bgcolor

        # Update the outline color
        self.hue = (self.hue + 0.001) % 1  # Increment hue and wrap around at 1
        self.outline_color = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(self.hue, 1, 1))

        # Draw the button
        pygame.draw.rect(self.app.screen, current_bg_color, self.rect, border_radius=5)
        pygame.draw.rect(self.app.screen, self.outline_color, self.rect, 5, border_radius=5)
        self.app.screen.blit(self.display_text, self.display_text_rect)
    def click(self):
        if self.function == 'start':
            self.app.ui = tetris.TetrisGame(self.app, 20, 10) # Change the displayed ui to the simulation
        elif self.function == 'settings':
            self.app.ui = settings.Settings(self.app)
        elif self.function == 'save_score':
            print("Saved score")
        else:
            self.bgcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))