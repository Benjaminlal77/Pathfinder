import pygame
from random import randint
from math import sqrt

from game_functions.events import check_events_while_finding_path
from game_functions.update import update_screen_while_finding_path

from game_data.settings import GridBoardSettings

class GridBoard:
    class Outline:    
        def __init__(self):
            # Defining outline properties
            self.rect = pygame.Rect(0,0,0,0)
            self.rect.x, self.rect.y = 0, 0
            self.rect.w = GridBoard.settings.width
            self.rect.h = GridBoard.settings.height 

            self.color = (0,0,0)
        
        def draw_outline(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)
    
    class Node:
        settings = GridBoardSettings.NodeSettings
        def __init__(self, node_num):
            self.node_num = node_num
            
            # Defining what the node can be
            self.is_start_point = False
            self.is_end_point = False
            self.is_obstacle = False
            self.is_open = False
            self.is_closed = False
            self.is_part_of_path = False

            # Defining the node costs
            self.g_cost = 0
            self.h_cost = 0
            self.f_cost = self.g_cost + self.h_cost
            
            # Defining the node properties
            self.column = self.get_columm()
            self.row = self.get_row()
            self.x, self.y = self.get_cords()
            self.parent = None
            
            self.make_border()
            self.make_node()
            
        def get_columm(self):
                column = self.node_num % GridBoard.nodes_per_column
                if column == 0:
                    return GridBoard.nodes_per_column
                return column
        
        def get_row(self):        
            for row_num in range(GridBoard.nodes_per_row + 1):
                if self.node_num <= GridBoard.nodes_per_row * row_num:
                    return row_num
            
        def get_cords(self):
            x = (self.settings.width * self.column) - self.settings.width
            y = (self.settings.height * self.row) - self.settings.height
            return x,y 
            
        def is_hovered_over(self):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            return self.rect.collidepoint(mouse_x, mouse_y)
            
        def set_neighbors(self, nodes):
            def found_max_neighbors():
                return len(self.neighbors) == 8
            
            def is_relative_to():
                # Checking around node
                def is_to_left_or_right():
                    if self.row == node.row:
                        if self.column + 1 == node.column or self.column - 1 == node.column:
                            return True
                def is_above_or_below():
                    if self.column == node.column:
                        if self.row + 1 == node.row or self.row - 1 == node.row:
                            return True
                def is_diagonal_from():
                    if self.column + 1 == node.column or self.column - 1 == node.column:
                        if self.row + 1 == node.row or self.row - 1 == node.row:
                            return True                    
                        
                if is_to_left_or_right() or is_above_or_below() or is_diagonal_from():
                    return True
            
            self.neighbors = []
            for node in nodes:        
                if self is node:
                    continue
                elif found_max_neighbors():
                    break
                    
                elif is_relative_to():
                    self.neighbors.append(node)      
                      
        def get_path(self):
            path = []
            parent = self
            while True: 
                parent = parent.parent
                if not parent:
                    return path
                path.append(parent)
            
        def make_border(self):
            self.border_rect = pygame.Rect(self.x,self.y,0,0)

            # Defining border properties
            self.border_rect.w = self.settings.width
            self.border_rect.h = self.settings.height
            self.border_color = self.settings.border_color
            
        def make_node(self):
            self.rect = pygame.Rect(self.x,self.y,0,0)
            
            # Defining node properties
            self.rect.x += self.settings.border_size
            self.rect.y += self.settings.border_size
            self.rect.w = self.settings.width - (2 * self.settings.border_size)
            self.rect.h = self.settings.height - (2 * self.settings.border_size)
            self.node_color = self.settings.color
            
        def reset(self):
            # Reseting what the node is
            self.is_start_point = False
            self.is_end_point = False
            self.is_obstacle = False
            self.is_open = False
            self.is_closed = False
            self.is_part_of_path = False

            # Reseting the node's costs
            self.reset_costs()
            
            self.parent = False
            
        def reset_costs(self):
            self.g_cost = 0
            self.h_cost = 0
            self.f_cost = self.g_cost + self.h_cost
            
        def check_to_change_color(self):
            if self.is_start_point:
                self.node_color = self.settings.start_point_color
            elif self.is_end_point:
                self.node_color = self.settings.end_point_color
            
            elif self.is_obstacle:
                self.node_color = self.settings.obstacle_color
            elif self.is_part_of_path:
                self.node_color = self.settings.path_color
                
            elif self.is_open:
                self.node_color = self.settings.open_color
            elif self.is_closed:
                self.node_color = self.settings.closed_color
            else:
                self.node_color = self.settings.color
            
        def draw_node(self, screen):
            pygame.draw.rect(screen, self.border_color, self.border_rect)
            pygame.draw.rect(screen, self.node_color, self.rect)
            
    settings = GridBoardSettings
            
    nodes_per_column = settings.columns
    nodes_per_row = settings.rows
    num_of_nodes = nodes_per_column * nodes_per_row    
    
    def __init__(self):
        # Creating the grid board
        self.outline = self.Outline()
        self.nodes = [self.Node(num) for num in range(1, GridBoard.num_of_nodes + 1)]
        
        for node in self.nodes:
            node.set_neighbors(self.nodes)
        self.randomize_node_points()
        
    def randomize_node_points(self):
        def randomize_start_node():
            while True:
                for node in self.nodes:
                    chance = randint(1, self.num_of_nodes) == 1
                    if chance:
                        node.is_start_point = True
                        return
        
        def randomize_end_node():
            while True:
                for node in self.nodes:
                    if node.is_start_point:
                        continue

                    chance = randint(1, self.num_of_nodes) == 1
                    if chance:
                        node.is_end_point = True
                        return
        
        randomize_start_node()
        randomize_end_node()
              
    def get_start_node(self):
        for node in self.nodes:
            if node.is_start_point:
                return node
        
    def get_end_node(self):
        for node in self.nodes:
            if node.is_end_point:
                return node
            
    def get_distance_between(self, node_a, node_b):
        x_distance = (node_a.rect.centerx - node_b.rect.centerx) ** 2
        y_distance = (node_a.rect.centery - node_b.rect.centery) ** 2
        distance = sqrt(x_distance + y_distance)
        return distance
               
    def find_path(self, stats, screen):            
        def get_closet_node():
            closet_node = None
            for node in open_nodes:
                if not closet_node:
                    closet_node = node
                elif node.f_cost < closet_node.f_cost:
                    closet_node = node
                elif node.f_cost == closet_node.f_cost and node.h_cost < closet_node.h_cost:
                    closet_node = node
            
            return closet_node
            
        def path_is_shorter():
            new_path_to_node = closet_node.g_cost + self.get_distance_between(neighbor, closet_node)
            return new_path_to_node < neighbor.g_cost
            
        open_nodes = []
        closed_nodes = []
        
        start_node = self.get_start_node()
        end_node = self.get_end_node()
        open_nodes.append(start_node)
        
        while True:
            closet_node = get_closet_node()
            
            if not closet_node:
                stats.no_path = True
                break
            
            open_nodes.remove(closet_node)
            closet_node.is_open = False
            closed_nodes.append(closet_node)
            closet_node.is_closed = True
                
            closet_node.check_to_change_color()
                
            if closet_node is end_node:
                for node in closet_node.get_path():
                    node.is_part_of_path = True
                break
            
            for neighbor in closet_node.neighbors:
                if neighbor.is_obstacle or neighbor.is_closed:
                    continue   
        
                if path_is_shorter() or not neighbor in open_nodes:
                    # Updating costs
                    neighbor.g_cost = closet_node.g_cost + self.get_distance_between(closet_node, neighbor) 
                    neighbor.h_cost = self.get_distance_between(neighbor, end_node)
                    neighbor.f_cost = neighbor.g_cost + neighbor.h_cost
                    
                    neighbor.parent = closet_node
                    if not neighbor.is_open in open_nodes:
                        neighbor.is_open = True
                        open_nodes.append(neighbor) 
                        
                        # Updating board
                        neighbor.check_to_change_color()
                        check_events_while_finding_path(stats)
                        if not stats.fast_solve:
                            update_screen_while_finding_path(screen, self)            

    def update(self, stats):    
        def check_to_edit_obstacle():
            for node in self.nodes:
                if node.is_start_point or node.is_end_point:
                    continue
                
                if node.is_hovered_over():
                    if stats.holding_left_click:
                        if not node.is_obstacle:
                            node.is_obstacle = True
                            
                    elif stats.holding_right_click:
                        if node.is_obstacle:
                            node.is_obstacle = False
                            
        check_to_edit_obstacle()
        for node in self.nodes:
            node.check_to_change_color()

    def draw_board(self, screen):
        for node in self.nodes:
            node.draw_node(screen)
        