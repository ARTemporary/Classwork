import pygame
import map_generator as mg
from pathlib import Path
import sys

def make_map(map: mg.Map, file_type='png', tile_set='default'):
    """create an image from map object use pygame surfaces"""
    file_type = file_type
    tile_set = tile_set
    tile_size = pygame.image.load(Path(sys.argv[0]).parent / Path(f'{tile_set}/empty.png')).get_width()
    width = map.width
    height = map.height

    map_surface = pygame.Surface((width * tile_size, height * tile_size))
    map.load_images(tile_set)

    for y in range(height):
            for x in range(width):
                map_surface.blit(map.cells[y][x].image, (tile_size * x, tile_size * y))

    pygame.image.save(map_surface, Path(sys.argv[0]).parent / Path(f'temp.{file_type}'))

