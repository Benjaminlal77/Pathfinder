import pygame

from game_data.settings import ScreenSettings, ButtonSettings

from game_objects.text_box import Text

class Button:
    settings = ButtonSettings
    
    def __init__(self, button_num, text):
        self.image = pygame.image.load('images/button.png')
        self.image = pygame.transform.scale(self.image, ButtonSettings.size)
        
        self.rect = self.image.get_rect()
        
        # Defining cords
        self.rect.x = self.settings.width * button_num + self.settings.marginx * button_num
        self.rect.x -= self.settings.width
        self.rect.centery = ScreenSettings.button_area_height/2
        self.rect.centery = abs(self.rect.centery - ScreenSettings.screen_height)
        
        # Defining size 
        self.rect.w = self.settings.width
        self.rect.h = self.settings.height
        
        self.button_text = Text(text, 25, (0,0,0), (self.rect.center))
        
    def is_clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_x, mouse_y)
        
    def draw_button(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.button_text.text_image, self.button_text.text_rect)
        
class ClearButton:
    def __init__(self):
        self.button = Button(1, 'Clear Board')
        
    def clear_board(self, game_objects, stats):
        grid_board = game_objects['grid_board']
        
        # Reseting/Setting up nodes
        for node in grid_board.nodes:
            node.is_obstacle = False
            
            node.is_open = False
            node.is_closed = False
            node.is_part_of_path = False
            
        # Reseting/Setting up Stats
        stats.no_path = False

class FindPathButton:
    def __init__(self):
        self.button = Button(2, 'Find Path')
        
    def find_path(self, game_objects, stats, screen):
        grid_board = game_objects['grid_board']
        
        # Reseting/Setting up nodes
        for node in grid_board.nodes:
            node.reset_costs()
            node.parent = None 
            
            node.is_open = False
            node.is_closed = False
            node.is_part_of_path = False
            
            node.check_to_change_color()

        # Reseting/Setting up Stats
        stats.fast_solve = False
        stats.no_path = False
        
        grid_board.find_path(stats, screen)

class RandomizeButton:
    def __init__(self):
        self.button = Button(3, 'Randomize Points')
        
    def randomize(self, game_objects, stats):
        grid_board = game_objects['grid_board']
        
        # Reseting/Setting up nodes
        for node in grid_board.nodes:
            node.reset()
        
        # Reseting/Setting up Stats
        stats.no_path = False
        
        grid_board.randomize_node_points()
        