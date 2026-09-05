import os
import random
from typing import List

import pygame 
pygame.init()
"""
if not pg.image.get_extended():
    raise SystemExit("Sorry, extended image module required")
"""
SCREEN_WIDTH= 800
SCREEN_LENGTH = 600
BACKGROUND_COLOR = (0,0,255)

MAX_SHOTS = 3

running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

screen = pygame.screen 
screen.fill(BACKGROUND_COLOR)