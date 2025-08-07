## make the underlying structure
## an array of cells 

import random
import pygame
from pathlib import Path
import sys

class Tile:
    """each area on the map: room or hall, doors, location, closed or not"""

    def __init__(self, layout: str, doors: set, location: tuple):
        self.layout = layout    # 'room' or 'hall' 
        self.doors = doors    # set containing doors as 'n' 'e' 's' 'w'
        self.location = location    # tuple of coordinates of the tile in the map array
        self.closed = False    # this variable checks whether new exits can be added

    def add_door(self, door: str):    # should i make this a non mutable function? # is this too simple a function?
        """adds door to doors, if door already in doors does nothing"""
        self.doors.add(door)

    def adjacent_tile(self, door: str):
        """returns adjacent coordinates to the tile in the direction of the door"""
        MODIFIERS = {'n': (0, -1), 'e': (1, 0), 's': (0, 1), 'w': (-1, 0)}
        x, y = self.location
        mod_x, mod_y = MODIFIERS[door]
        return (x + mod_x, y + mod_y)

    def close_tile(self):    # is this also too simple?
        """set the closed attribute to true"""
        self.closed = True
        temp_doors = list(self.doors)
        temp_doors.sort()
        self.image_key = f'{self.layout[0]},{''.join(temp_doors)}'

    def load_image(self, tile_set='default'):
        """loads image from """
        layout, name = self.image_key.split(',')
        self.image = pygame.image.load(Path(sys.argv[0]).parent / Path(f'{tile_set}/{layout}/{name}.png'))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.__dict__ == self.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.image_key
    
class EmptyTile:
    def __init__(self, tile_set='default'):
        self.tile_set = tile_set
        self.image = pygame.image.load(Path(sys.argv[0]).parent / Path(f'{tile_set}/empty.png'))

    def __str__(self):
        return f'|      |'

class Map:
    """height, width, array of cells"""
    # how to make optional parameters?

    def __init__(self, height: int, width: int, frequency=6, start="center"):
        self.height = height    # map height , number of rows
        self.width = width    # map width , number of columns , length of rows
        self.frequency = frequency    # how many dice to roll when generating map
        self.start = start    # possible feature - different starting points to generate from - currently only starting from center
        # create array
        self.cells = []    # the array containing the tiles
        for i in range(0, height):    # generate 2 dimensional array of correct height and width
            self.cells.append(list(None for l in range(0, width)))
        self.gernerate()    # build the map

    def gernerate(self):
        """generate the map"""
        queue = self.generate_center_start()    # initialize queue
        while queue:    # run queue
            x, y = queue.pop(0)
            queue.extend(self.gernerate_new_tiles(self.cells[y][x]))    # generate new tiles and add their coordinates to the queue

    def gernerate_new_tiles(self, tile: Tile):    # clean this up?
        """generate new tiles or adds new connection to available tiles, returns list of coordinates of new tiles"""
        OPPOSITES = {'n':'s', 'e':'w', 's':'n', 'w':'e'}    # dict for reference
        temp_doors = new_doors(self.frequency)
        new_tiles = []
        for door in temp_doors:
            if door in tile.doors:    # if the door already exists, skip
                continue

            tx, ty = tile.adjacent_tile(door)    # coordinates of the next tile in the direction of the door

            if not self.is_in_bounds((tx, ty)):    # if out of bounds, skip
                continue
            else:
                temp_tile = self.cells[ty][tx]

                if temp_tile == None:    # no tile exists -> make new tile with correct door
                    self.cells[ty][tx] = Tile(rand_layout(), {OPPOSITES[door]}, (tx, ty))
                    tile.add_door(door)
                    new_tiles.append((tx, ty))    # add new tile to queue
                elif temp_tile.closed == False:    # tile exists and is not closed -> add correct door
                    self.cells[ty][tx].add_door(OPPOSITES[door])
                    tile.add_door(door)
                else:    # closed tile at coordinates
                    continue
        tile.close_tile()
        return new_tiles

    def generate_center_start(self):
        """build the center tile, generates adjacent tiles, and creates a queue of the first 5 tiles"""
        OPPOSITES = {'n':'s', 'e':'w', 's':'n', 'w':'e'}    # dict for reference
        x, y = (self.width // 2, self.height // 2)    # get the center coordinates - potential for customizing starting location
        self.cells[y][x] = Tile('room', {'n', 's', 'e', 'w'}, (x, y))    # build the same center tile each time - potential for future costumizing
        first_queue = [(x, y)]
        for door in ['n','s','e','w']:
            tx, ty = self.cells[y][x].adjacent_tile(door)
            first_queue.append((tx, ty))     
            self.cells[ty][tx] = Tile(rand_layout(), {OPPOSITES[door]}, (tx, ty))     
        return first_queue

    def is_in_bounds(self, coords: tuple):
        """check if coordinates are within array"""
        x, y = coords
        if x in range(0, self.width) and y in range(0, self.height):
            return True
        else:
            return False

    def map_print(self):
        return f"{"\n".join(" ".join(f"{str(self.cells[i][j]):<8}" for j in range(self.width)) for i in range(self.height))}"
    
    def __str__(self):
        return f"{self.width}x{self.height},{self.frequency}\n{self.map_print()}"
    
    def load_images(self, tile_set='default'):
        """load all the tile images in the map array"""
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.cells[i][j] == None:
                    self.cells[i][j] = EmptyTile()
                else:
                    self.cells[i][j].load_image(tile_set)

def new_doors(n: int):
    """roll n d6, return list of doors"""
    rolls = list(random.randint(1,6) for i in range(0, n))
    doors = set()
    DOORS = {1:'n', 2:'e', 3:'s', 4:'w'}
    for roll in rolls:
        if roll not in DOORS.keys():    # skip if can't translate to a door
            continue
        else:
            doors.add(DOORS[roll])    # add the door corresponding to the roll value to the set
    return list(doors)

def rand_layout():
    """returns random 'room' or 'hall'."""
    layout = random.choice(['room', 'hall'])
    return layout