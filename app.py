import pygame, json
from classes import mainmenu, playernick
import settings_values
resolutions = ["1000x800", "1200x900", "1920x1080", "2560x1440"]
class App:
    def __init__(self, width, height, fullscreen, vsync):
        with open('settings.json', 'r') as file:
            data = json.load(file)
            settings = data['settings']
        settings_values.mode = settings['Gamemode']
        settings_values.default_level = settings['Default level']
        settings_values.block_colors = settings['Block colors']
        settings_values.max_fall_speed = settings['Max fall speed']
        # Save the data passed into the function to variables
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.width = int(resolutions[settings['Resolution']].split('x')[0])
        self.height = int(resolutions[settings['Resolution']].split('x')[1])
        self.is_FS_enabled = fullscreen
        self.is_vsync_enabled = vsync
        self.scale = 1
        self.last_player = ''
        self.ui = mainmenu.MainMenu(self)
        self.onLevel = False
        # Initialize pygame
        pygame.init()

        # Window setup
        if fullscreen:
            self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN, vsync=int(vsync))
        else:
            self.screen = pygame.display.set_mode((self.width, self.height), vsync=int(vsync))

        self.run = True # Variable to determine if the app is running

        img = pygame.image.load("img/icon.png")

        pygame.display.set_caption("Tetris")
        pygame.display.set_icon(img)

    def LogPlayer(self):
        if self.ui.textBox.text == 'Your nick':
            self.ui.textBox.text = "Player 1"
        playernick.Playernick.SetNickname(self.ui.textBox.text)
        #print(playernick.Playernick.GetNickname())
        return True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_pos = pygame.mouse.get_pos()
                for button in self.ui.buttons:
                    if button.rect.collidepoint(click_pos[0], click_pos[1]):
                        button.click()
                if type(self.ui) == mainmenu.MainMenu and self.onLevel is False:
                    self.ui.textBox.handle_event(event)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pass
                #print(pygame.mouse.get_pos())
            if not self.onLevel and event.type == pygame.KEYDOWN:
               self.ui.textBox.handle_event(event)


    def background(self):
        self.screen.fill((0, 0, 0))

    def update(self):
        pygame.display.update()
    def mainloop(self):
        self.clock.tick(self.fps)
        if self.run is False:
            pygame.quit()
        self.background()
        self.ui.render()
        self.update()
        self.ui.events()
        self.events()
