## make the underlying structure
## an array of cells 

import random
import pygame
from pathlib import Path
import sys

class Tile:
    """each area on the map: room or hall, doors, location, closed or not"""

    def __init__(self, type: str, doors: set, location: tuple):
        self.type = type    # 'room' or 'hall' 
        self.doors = doors    # set containing doors as 'n' 'e' 's' 'w'
        self.location = location    # tuple of coordinates of the tile in the map array
        self.closed = False    # this variable checks whether new exits can be added

    def add_door(self, door: str):    # should i make this a non mutable function? # is this too simple a function?
        """adds door to doors, if door already in doors does nothing"""
        self.doors.add(door)

    def get_adjacent_tile(self, door: str):
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
        self.image_key = f'{self.type[0]},{''.join(temp_doors)}'

    def load_image(self):
        """loads image from """
        layout, name = self.image_key.split(',')
        self.image = pygame.image.load(Path(sys.argv[0]).parent / Path(f'tiles/{layout}/{name}.png')).convert_alpha()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.__dict__ == self.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        doors = list(self.doors)
        doors.sort()
        return f'{self.type[0]},{"".join(doors)}'
    
class EmptyTile:
    def __init__(self):
        self.image = pygame.image.load(Path(sys.argv[0]).parent / Path(f'tiles/empty.png')).convert_alpha()

class Map:
    """height, width, array of cells"""
    # how to make optional parameters?

    def __init__(self, height: int, width: int, frequency=6, type="center"):
        self._height = height    # map height , number of rows
        self._width = width    # map width , number of columns , length of rows
        self._frequency = frequency    # how many dice to roll when generating map
        self._type = type    # possible feature - different starting points to generate from - currently only starting from center
        # create array
        self.cells = []    # the array containing the tiles
        for i in range(0, height):    # generate 2 dimensional array of correct height and width
            self.cells.append(list(None for l in range(0, width)))
        self._generate()    # build the map

    def _generate(self):
        """generate the map"""
        queue = self._generate_first_queue_center()    # initialize queue
        while queue:    # run queue
            x, y = queue.pop(0)
            queue.extend(self._generate_new_tiles(self.cells[y][x]))    # generate new tiles and add their coordinates to the queue

    def _generate_new_tiles(self, tile: Tile):    # clean this up?
        """generate new tiles or adds new connection to available tiles, returns list of coordinates of new tiles"""
        OPPOSITES = {'n':'s', 'e':'w', 's':'n', 'w':'e'}    # dict for reference
        temp_doors = set_difference(get_doors(self._frequency), tile.doors)    # set of new potential tiles - does not include tiles that already exist
        new_tiles = []
        for door in temp_doors:
            tx, ty = tile.get_adjacent_tile(door)    # coordinates of the next tile in the direction of the door

            if not self._in_bounds((tx, ty)):
                continue
            else:
                temp_tile = self.cells[ty][tx]

                if temp_tile == None:    # no tile exists -> make new tile with correct door
                    self.cells[ty][tx] = Tile(get_type(), {OPPOSITES[door]}, (tx, ty))
                    tile.add_door(door)
                    new_tiles.append((tx, ty))    # add new tile to queue
                elif temp_tile.closed == False:    # tile exists and is not closed -> add correct door
                    self.cells[ty][tx].add_door(OPPOSITES[door])
                    tile.add_door(door)
                else:    # closed tile at coordinates
                    continue
        tile.close_tile()
        return new_tiles

    def _generate_first_queue_center(self):
        """build the center tile, generates adjacent tiles, and creates a queue of the adjacent tiles"""
        OPPOSITES = {'n':'s', 'e':'w', 's':'n', 'w':'e'}    # dict for reference
        x, y = (self._width // 2, self._height // 2)    # get the center coordinates - potential for customizing starting location
        self.cells[y][x] = Tile('room', {'n', 's', 'e', 'w'}, (x, y))    # build the same center tile each time - potential for future costumizing
        first_queue = [(x, y)]
        for door in ['n','s','e','w']:
            tx, ty = self.cells[y][x].get_adjacent_tile(door)
            first_queue.append((tx, ty))     
            self.cells[ty][tx] = Tile(get_type(), {OPPOSITES[door]}, (tx, ty))     
        return first_queue

    def _in_bounds(self, coords: tuple):
        """check if coordinates are within array"""
        x, y = coords
        if x in range(0, self._width) and y in range(0, self._height):
            return True
        else:
            return False

    def key_array(self):
        return list(list(str(self.cells[i][j]) for j in range(self._width)) for i in range(self._height))

    def map_print(self):
        return f"{"\n".join(" ".join(f"{str(self.cells[i][j]):<8}" for j in range(self._width)) for i in range(self._height))}"
    
    def __str__(self):
        return f"{self._width}x{self._height},{self._frequency}\n{self.map_print()}"
    
    def load_images(self):
        """load all the tiles in the map array"""
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.cells[i][j] == None:
                    self.cells[i][j] = EmptyTile()
                else:
                    self.cells[i][j].load_image()

def get_doors(n: int):
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

def get_type():
    """returns random 'room' or 'hall'."""
    type = random.choice(['room', 'hall'])
    return type

def set_difference(main, other):
    """removes elements from list main that already exist in other, return main w/o elements"""
    temp = []
    for element in main:
        if element not in other:
            temp.append(element)
        else:
            continue
    return temp