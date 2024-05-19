import pygame
from classes import buttons
import settings_values
class LevelSelect:
    def __init__(self, app):
        self.app = app
        self.main_text_rect_center = (self.app.width//2, 250 * self.app.scale)
        self.font = "fonts/main_font.ttf"
        self.arrow_font = "fonts/arrows.ttf" # character map: https://www.1001fonts.com/pizzadude-pointers-font.html
        self.font_color = (255, 255, 255)
        self.selected_level = settings_values.default_level
        self.buttons = [buttons.Button(100 * self.app.scale, 75 * self.app.scale, self.app.width/2 - 200 * self.app.scale, self.app.height/2 - 75 * self.app.scale/2, False, self.arrow_font, "Q", (0, 0, 0), self.font_color, 'minus', self.app),
                        buttons.Button(100 * self.app.scale, 75 * self.app.scale, self.app.width/2 + 100 * self.app.scale, self.app.height/2 - 75 * self.app.scale/2, False, self.arrow_font, "U", (0, 0, 0), self.font_color, 'plus', self.app),
                        buttons.Button(200 * self.app.scale, 75 * self.app.scale, self.app.width/2 - 100 * self.app.scale, self.app.height/2 + 150 * self.app.scale/2, False, self.font, "Start", (0, 0, 0), self.font_color, 'start_game', self.app),
                        buttons.Button(200 * self.app.scale, 75 * self.app.scale, self.app.width/2 - 100 * self.app.scale, self.app.height/2 + 350 * self.app.scale/2, False, self.font, "Back", (0, 0, 0), self.font_color, 'back_to_menu', self.app)]

    def render(self):
        self.app.screen.fill((0, 0, 0))
        for button in self.buttons:
            button.render()
        font = pygame.font.Font(self.font, int(72 * self.app.scale))
        font2 = pygame.font.Font(self.font, int(48 * self.app.scale))

        display_text = font.render("Select start level", True, self.font_color)
        display_text_rect = display_text.get_rect()
        display_text_rect.center = self.main_text_rect_center

        level_text = font2.render(f"Level {self.selected_level}", True, self.font_color)
        rect = pygame.Rect(self.app.width/2 - 50 * self.app.scale, self.app.height/2 - 75 * self.app.scale/2, 100 * self.app.scale, 75 * self.app.scale)
        level_text_rect = level_text.get_rect()
        level_text_rect.center = rect.center

        self.app.screen.blit(display_text, display_text_rect)
        self.app.screen.blit(level_text, level_text_rect)
    def add(self):
        if self.selected_level < 15:
            self.selected_level += 1
    def subtract(self):
        if self.selected_level > 1:
            self.selected_level -= 1
    def events(self):
        pass