import pygame
import sys

left_click = 1
right_click = 3

def check_mouse_click(game_objects, stats, event):
    clear_button = game_objects['clear_button']
    randomize_button = game_objects['randomize_button']
    
    if clear_button.button.is_clicked():
        clear_button.clear_board(game_objects)
    elif randomize_button.button.is_clicked():
        randomize_button.randomize(game_objects)
    
    elif event.button == left_click:
        stats.holding_left_click = True
    elif event.button == right_click:
        stats.holding_right_click = True

def check_mouse_release(stats, event):
    if event.button == left_click:
        stats.holding_left_click = False
    elif event.button == right_click:
        stats.holding_right_click = False

def check_events(game_objects, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_click(game_objects, stats, event)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            check_mouse_release(stats, event)
                