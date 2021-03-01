import pygame

from game_data.settings import ScreenSetings

def update_screen(screen, game_objects):
    grid_board = game_objects['grid_board']

    screen.fill(ScreenSetings.bg_color)
    
    grid_board.draw_board(screen)
    
    pygame.display.flip()
    pygame.time.Clock().tick(ScreenSetings.FPS)

