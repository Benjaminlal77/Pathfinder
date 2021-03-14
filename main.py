import pygame

from game_functions.events import check_events
from game_functions.update import update_screen
from game_data.settings import ScreenSettings
from game_data.stats import Stats

from game_objects.board import GridBoard
from game_objects.buttons import ClearButton, FindPathButton, RandomizeButton

pygame.init()
screen = pygame.display.set_mode((ScreenSettings.screen_width, ScreenSettings.screen_height))

pygame.display.set_caption('Path Finder')
icon_image = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon_image)

stats = Stats()

grid_board = GridBoard()

# Creating game objects
clear_button = ClearButton()
find_path_button = FindPathButton()
randomize_button = RandomizeButton()

game_objects = {
    'grid_board' : grid_board,
    'clear_button' : clear_button,
    'find_path_button' : find_path_button,
    'randomize_button' : randomize_button
}

while True:
    check_events(screen, stats, game_objects)
    update_screen(screen, stats, game_objects)
    