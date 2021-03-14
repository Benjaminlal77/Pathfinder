import pygame

from game_data.settings import ScreenSettings
from game_objects.text_box import FastSolveTextBox, NoPathTextBox

def update_screen(screen, stats, game_objects):
    def draw_game_objects():
        grid_board.draw_board(screen)

        clear_button = game_objects['clear_button']
        find_path_button = game_objects['find_path_button']
        randomize_button = game_objects['randomize_button']

        # Draw buttons
        clear_button.button.draw_button(screen)
        find_path_button.button.draw_button(screen)
        randomize_button.button.draw_button(screen)
        
        if stats.no_path:
            NoPathTextBox().write_text(screen)
        
    grid_board = game_objects['grid_board']
        
    grid_board.update(stats)
    
    screen.fill(ScreenSettings.bg_color)
        
    draw_game_objects()    
    
    pygame.display.flip()
    pygame.time.Clock().tick(ScreenSettings.FPS)

def update_screen_while_finding_path(screen, grid_board):
    screen.fill(ScreenSettings.bg_color)

    grid_board.draw_board(screen)
    FastSolveTextBox().write_text(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(ScreenSettings.FPS)
