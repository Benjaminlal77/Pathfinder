import pygame

from settings import ScreenSetings

def update_screen(screen):

    screen.fill(ScreenSetings.bg_color)
    
    pygame.display.flip()
    pygame.time.Clock().tick(ScreenSetings.FPS)

