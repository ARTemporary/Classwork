import pygame
import map_generator as mg

import map_maker as mm


print()

height = 80
width = 80



map = mg.Map(height, width, 2)

# print(map)

# print(map.map_print())

# print(map.key_array())

# test_string = 'r,ens'
# layout, doors = test_string.split(',')
# print(layout)

mm.make_map(map)