import pygame
from random import randint

from game_data.settings import GridBoardSettings

class GridBoard:
    class Outline:    
        def __init__(self):
            self.rect = pygame.Rect(0,0,0,0)
            self.rect.x, self.rect.y = 0, 0
            self.rect.w = GridBoard.settings.width
            self.rect.h = GridBoard.settings.height 

            self.color = (0,0,0)
        
        def draw_outline(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)
    
    class Box:
        settings = GridBoardSettings.BoxSettings
        def __init__(self, box_num):
            self.box_num = box_num
            self.is_obstacle = False
            self.is_start_point = False
            self.is_end_point = False
            
            self.column = self.get_columm()
            self.row = self.get_row()
            
            self.x, self.y = self.get_cords()
            
            self.make_border()
            self.make_box()
            
        def get_columm(self):
                column = self.box_num % GridBoard.boxes_per_column
                
                if column == 0:
                    return GridBoard.boxes_per_column

                return column
        
        def get_row(self):        
            for row_num in range(GridBoard.boxes_per_row + 1):
                if self.box_num <= GridBoard.boxes_per_row * row_num:
                    return row_num
            
        def get_cords(self):
            x = (self.settings.width * self.column) - self.settings.width
            y = (self.settings.height * self.row) - self.settings.height
            
            return x,y 
            
        def is_hovered_over(self):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            return self.rect.collidepoint(mouse_x, mouse_y)
            
        def make_border(self):
            self.border_rect = pygame.Rect(self.x,self.y,0,0)

            self.border_rect.w = self.settings.width
            self.border_rect.h = self.settings.height
            
            self.border_color = self.settings.border_color
            
        def make_box(self):
            self.rect = pygame.Rect(self.x,self.y,0,0)
            
            self.rect.x += self.settings.border_size
            self.rect.y += self.settings.border_size

            self.rect.w = self.settings.width - (2 * self.settings.border_size)
            self.rect.h = self.settings.height - (2 * self.settings.border_size)
            
            self.box_color = self.settings.color
            
        def update(self):
            if self.is_start_point:
                self.box_color = self.settings.start_point_color
            elif self.is_end_point:
                self.box_color = self.settings.end_point_color
            elif self.is_obstacle:
                self.box_color = self.settings.obstacle_color
            else:
                self.box_color = self.settings.color
            
        def draw_box(self, screen):
            pygame.draw.rect(screen, self.border_color, self.border_rect)
            pygame.draw.rect(screen, self.box_color, self.rect)
            
    settings = GridBoardSettings
            
    boxes_per_column = settings.columns
    boxes_per_row = settings.rows
    num_of_boxes = boxes_per_column * boxes_per_row    
    
    def __init__(self):
        self.outline = self.Outline()
        self.boxes = [self.Box(num) for num in range(1, GridBoard.num_of_boxes + 1)]
        
        self.randomize_points()
        
    def randomize_points(self):
        def randomize_start_point():
            while True:
                for box in self.boxes:
                    chance = randint(1, self.num_of_boxes) == 1
                    if chance:
                        box.is_start_point = True
                        return
        
        def randomize_end_point():
            while True:
                for box in self.boxes:
                    if box.is_start_point:
                        continue

                    chance = randint(1, self.num_of_boxes) == 1
                    if chance:
                        box.is_end_point = True
                        return
        
        randomize_start_point()
        randomize_end_point()
        
    def update(self, stats):    
        def check_to_edit_obstacle():
            for box in self.boxes:
                if box.is_start_point or box.is_end_point:
                    continue
                
                if box.is_hovered_over():
                    if stats.holding_left_click:
                        if not box.is_obstacle:
                            box.is_obstacle = True
                            
                    elif stats.holding_right_click:
                        if box.is_obstacle:
                            box.is_obstacle = False
                            
        check_to_edit_obstacle()
        for box in self.boxes:
            box.update()
        
    def draw_board(self, screen):
        for box in self.boxes:
            box.draw_box(screen)
        