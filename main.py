import pygame

from events import check_events
from update import update_screen
from settings import ScreenSetings

screen = pygame.display.set_mode((ScreenSetings.screen_width, ScreenSetings.screen_height))

screen.fill(ScreenSetings.bg_color)

while True:
    check_events()
    update_screen(screen)
    