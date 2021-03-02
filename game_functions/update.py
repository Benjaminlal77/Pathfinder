import pygame

from game_data.settings import ScreenSettings

def update_screen(screen, game_objects, stats):
    def draw_game_objects():
        grid_board.draw_board(screen)
        clear_button.button.draw_button(screen)
        
    grid_board = game_objects['grid_board']
    clear_button = game_objects['clear_button']
        
    grid_board.update(stats)
    
    screen.fill(ScreenSettings.bg_color)
        
    draw_game_objects()    
    
    pygame.display.flip()
    pygame.time.Clock().tick(ScreenSettings.FPS)

