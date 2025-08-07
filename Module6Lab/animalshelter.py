## Animal Shelter Management System

animal_shelter = []
CAPACITY = 20
CAPACITY = 3    # for testing

def get_animal_count():
    """Return the total number of animals in the shelter"""
    animal_count = len(animal_shelter)
    # print("There are " + str(animal_count) + " animals in the shelter.")    # for testing
    return animal_count

def add_animal(name):
    """Add and animal if the shelter is not at capacity"""
    if get_animal_count() >= CAPACITY:
        print("There is no room at the animal shelter for " + name + ".")
    else:
        animal_shelter.append(name)
        print(name + " is taken in by the animal shelter.")
        print("The animals at the shelter are: " + ", ".join(animal_shelter))

def adopt_animal(name):
    """Remove an animal from the shelter when adopted"""
    if name not in animal_shelter:
        print(name + " is not at the animal shelter.")
    else:
        animal_shelter.remove(name)
        print(name + " was adopted.")

add_animal("Bob the Cat")
add_animal("Burger the Rat")
add_animal("Fries the Rat")
add_animal("Daisy the Cat")

print(str(get_animal_count()))

adopt_animal("Bob the Cat")

print(str(get_animal_count()))

adopt_animal("Daisy the Cat")

print(str(get_animal_count()))


