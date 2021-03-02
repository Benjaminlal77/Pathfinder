import pygame

from game_data.settings import ScreenSettings, ButtonSettings

from game_objects.text_box import Text

class Button:
    
    settings = ButtonSettings
    
    def __init__(self, button_num, text):
        self.image = pygame.image.load('images/button.png')
        self.image = pygame.transform.scale(self.image, ButtonSettings.size)
        
        self.rect = self.image.get_rect()
        
        # Define cords
        
        self.rect.x = self.settings.width * button_num + self.settings.marginx * button_num
        self.rect.x -= self.settings.width
        self.rect.centery = ScreenSettings.button_area_height/2
        self.rect.centery = abs(self.rect.centery - ScreenSettings.screen_height)
        
        # Define size 
        
        self.rect.w = self.settings.width
        self.rect.h = self.settings.height
        
        self.button_text = Text(text, 25, (0,0,0), (self.rect.center))
        
    def draw_button(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.button_text.text_image, self.button_text.text_rect)
        
    def is_clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_x, mouse_y)
        
class ClearButton:
    def __init__(self):
        self.button = Button(1, 'Clear Board')
        
    def clear_board(self, game_objects):
        grid_board = game_objects['grid_board']
        for box in grid_board.boxes:
            box.is_obstacle = False

class RandomizeButton:
    def __init__(self):
        self.button = Button(3, 'Randomize Points')
        
    def randomize(self, game_objects):
        grid_board = game_objects['grid_board']
        for box in grid_board.boxes:
            box.is_obstacle = False
            box.is_start_point = False
            box.is_end_point = False
        
        grid_board.randomize_points()
        