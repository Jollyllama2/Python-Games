import pygame
import random 
from pathlib import Path
import time 

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 45
GRAVITY = 5
GAME_SPEED = 25 

GROUND_WIDTH = 2*SCREEN_HEIGHT
GROUND_HEIGHT = 120

dd = Path(__file__).parent

#class Dino()
    








BACKGROUD =  pygame.image.load(dd / 'images/dino_party_sheet.png')
BACKGROUND = pygame.transform.scale(BACKGROUD, (SCREEN_WIDTH, SCREEN_HEIGHT))
while True:    