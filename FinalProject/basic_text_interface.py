import map_generator as mg

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

    map = mg.Map(height, width, frequency)

    print()
    print(map)
    print()
    
