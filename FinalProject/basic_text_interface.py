import map_generator as mg
from map_maker import make_map

def get_positive_number_input(text: str):
    """get user input between as a positive number"""
    while True:
        user_input = input(text)
        if user_input.isdecimal() and int(user_input) > 0:
            return int(user_input)
        else:
            print(f'Invalid input. Enter a number greater than zero.')
        

while True:
    height = get_positive_number_input('Height: ')
    width = get_positive_number_input('Width: ')
    frequency = get_positive_number_input('Frequency: ')    # how many dice to roll for possible exits

    if height < 3 or width < 3:
        print("Width and height must be greater than 2.")
        continue

    map = mg.Map(height, width, frequency)
    make_map(map)

    print()
    print(map)
    print()
    print(f'Map made at temp.png.\n')    