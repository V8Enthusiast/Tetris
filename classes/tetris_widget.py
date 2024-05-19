import pygame


class NextStructuresWidget:
    def __init__(self, game, app, bg_color):
        self.game = game
        self.app = app
        self.width = self.app.width / 5
        self.height = self.app.height * 3 / 4
        self.x = self.app.width * 3/ 4
        self.y = self.app.width / 10
        self.bg_color = bg_color
        self.font = pygame.font.SysFont('Impact', 48)
        self.title_text = self.font.render(f"NEXT", True, (255, 255, 255))
        self.next_structures = self.game.next_structures
        self.offset = self.height / 7

    def render(self):
        self.next_structures = self.game.next_structures
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.app.screen, self.bg_color, rect)
        self.app.screen.blit(self.title_text, (self.x + self.width/3.4, self.y + self.height / 35))
        for i, structure in enumerate(self.next_structures):
            structure.preview(self.x - self.width /2.76, self.y + i * self.height/3.5 + self.offset)
            if i >= 2:
                break

class HoldWidget:
    def __init__(self, game, app, bg_color):
        self.game = game
        self.app = app
        self.width = self.app.width / 5
        self.height = self.app.height / 3.5
        self.x = self.app.width / 20
        self.y = self.app.width / 10
        self.bg_color = bg_color
        self.font = pygame.font.SysFont('Impact', 48)
        self.title_text = self.font.render(f"HOLD", True, (255, 255, 255))
        self.held_structure = self.game.held_structure
        self.offset = self.height / 7

    def render(self):
        self.held_structure = self.game.held_structure
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.app.screen, self.bg_color, rect)
        self.app.screen.blit(self.title_text, (self.x + self.width/3.4, self.y + self.height / 35))
        if self.held_structure is not None:
            self.held_structure.preview(self.x - self.width /2.76, self.y + self.height/3.5 + self.offset)