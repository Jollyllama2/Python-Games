import pygame
import random 
from pathlib import Path
import time 

SCREEN_WIDTH = 590
SCREEN_HEIGHT = 690
SPEED = 45
GRAVITY = 5
GAME_SPEED = 25 

GROUND_WIDTH = SCREEN_HEIGHT
GROUND_HEIGHT = 120

dd = Path(__file__).parent


#class Dino()
    


clock= pygame.time.Clock()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dino Run')


BACKGROUND_1 =  pygame.image.load(dd / 'images/dino_party_sheet.png')
BACKGROUND = pygame.transform.scale(BACKGROUND_1, (SCREEN_WIDTH, SCREEN_HEIGHT))
while True: 
    
    
    clock.tick(15)

    screen.blit(BACKGROUND, (0,0))

    pygame.display.update()