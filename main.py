import pygame

from game_functions.events import check_events
from game_functions.update import update_screen
from game_data.settings import ScreenSetings
from game_data.stats import Stats

from game_objects.board import GridBoard

screen = pygame.display.set_mode((ScreenSetings.screen_width, ScreenSetings.screen_height))
stats = Stats()

screen.fill(ScreenSetings.bg_color)

grid_board = GridBoard()

game_objects = {
    'grid_board' : grid_board
}

while True:
    check_events(stats)
    update_screen(screen, game_objects, stats)
    