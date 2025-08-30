"""
Example of loading a background image that is not as wide as the screen, and
tiling it to fill the screen.

"""
import pygame
import random

# Initialize Pygame
pygame.init()

from pathlib import Path
assets = Path(__file__).parent / 'images'

# Set up display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Free Robux')

def make_tiled_bg(screen, bg_file):
    # Scale background to match the screen height
    
    bg_tile = pygame.image.load(bg_file).convert()
    
    background_height = screen.get_height()
    bg_tile = pygame.transform.scale(bg_tile, (bg_tile.get_width(), screen.get_height()))

    # Get the dimensions of the background after scaling
    background_width = bg_tile.get_width()
    print(background_width)

    # Make an image the is the same size as the screen
    image = pygame.Surface((screen.get_width(), screen.get_height()))

    # Tile the background image in the x-direction
    for x in range(0, screen.get_width(), background_width):
        image.blit(bg_tile, (x, 0))
        
    return image

import pygame

def draw__bg(screen):
    """
    Creates and tiles a background on the screen from a list of surfaces.
    
    Args:
        screen (pygame.Surface): The main display surface to draw on.
        bg_tiles (list): A list of pygame.Surface objects to be tiled.
    """
    # Create one large surface from the individual tiles
    screen_width, screen_height = screen.get_size()
    tile_width = 126
    combined_surface = pygame.Surface((screen_width, screen_height))
    
    # Blit each tile onto the combined surface
    tile = pygame.Surface([tile_width, screen_height])
    # Tile the combined surface to fill the entire screen
    
    for x in range(0, screen_width, tile_width):
        tile.fill((0,0,random.randint(0,255)))
        combined_surface.blit(tile, (x, 0))

    return combined_surface


background = draw__bg(screen)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
