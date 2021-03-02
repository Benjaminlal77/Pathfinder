import pygame
import sys

left_click = 1
right_click = 3

def check_mouse_click(stats, event):
    if event.button == left_click:
        stats.holding_left_click = True
    elif event.button == right_click:
        stats.holding_right_click = True

def check_mouse_release(stats, event):
    if event.button == left_click:
        stats.holding_left_click = False
    elif event.button == right_click:
        stats.holding_right_click = False

def check_events(stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_click(stats, event)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            check_mouse_release(stats, event)
                