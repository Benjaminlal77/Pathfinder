import pygame
import sys

left_click = 1
right_click = 3

def check_events(screen, stats, game_objects):
    def check_mouse_click():
        clear_button = game_objects['clear_button']
        randomize_button = game_objects['randomize_button']
        find_path_button = game_objects['find_path_button']
        
        # Check button clicks
        if clear_button.button.is_clicked():
            clear_button.clear_board(game_objects, stats)
        elif find_path_button.button.is_clicked():
            find_path_button.find_path(game_objects, stats, screen)
        elif randomize_button.button.is_clicked():
            randomize_button.randomize(game_objects, stats)
        
        elif event.button == left_click:
            stats.holding_left_click = True
        elif event.button == right_click:
            stats.holding_right_click = True
    
    def check_mouse_release():
        if event.button == left_click:
            stats.holding_left_click = False
        elif event.button == right_click:
            stats.holding_right_click = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_click()
        elif event.type == pygame.MOUSEBUTTONUP:
            check_mouse_release()
                
def check_events_while_finding_path(stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stats.fast_solve = True 
    