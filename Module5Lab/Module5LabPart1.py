# Date: 2025/07/06
# Description: Goldfish Playdate Planner

import random   # will need this later


goldfish = ["Bubbles", "Finley", "Goldie", "Splash", "Nemo"]

print("Welcome to the Goldfish Playdate Planner!")
print("Our goldfish friends are: " + ", ".join(goldfish))

while True:     # add a new fish to the list
    add_fish = input("Would you like to add a fish? y/n ")

    if add_fish == 'n': #done adding fish
        print('Your goldfish are: ' + ', '.join(goldfish))
        break

    if add_fish == 'y': # add a new fish
        new_fish = input('Enter the name of the new goldfish: ')
        goldfish.append(new_fish)
        print('Updated goldfish list: ' + ', '.join(goldfish))

while True:     # removing fish
    remove_fish = input('Would you like to remove a fish? y/n ')

    # quit removing
    if remove_fish == 'n':
        print('Your goldfish are: ' + ', '.join(goldfish))
        break

    # remove a fish
    if remove_fish == 'y':
        fish_to_remove = input('Enter the name of the goldfish to remove: ')
        
    # fish in the list 
    if fish_to_remove in goldfish:
        goldfish.remove(fish_to_remove)
        print(fish_to_remove + ' has been removed from the list.')
    else:   # or not
        print('Sorry, ' + fish_to_remove + ' is  not in the list.')

# creating playdate pairs 
print("\nLet's create some playdate pairs!")



random.shuffle(goldfish)    # shuffle the list

for i in range(0, len(goldfish), 2):
    if i + 1 < len(goldfish):
        print(goldfish[i] + " will have a playdate with " + goldfish[i + 1] + ".")
    else:
        print(goldfish[i] + " will have a solo play session.")

