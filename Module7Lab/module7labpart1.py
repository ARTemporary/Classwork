## Dictionaries

food_stands = {"Pronto Pups": "Corn Dogs", "Big Fat Bacon": "Bacon-on-a-Stick"}

# print("Food stands at the fair:")
# for stand, food in food_stands.items():
#     print(stand + ": " + food)

food_stands["Pronto Pups"] = "Footlong Corn Dogs"

# print("Food stands at the fair:")
# for stand, food in food_stands.items():
#     print(stand + ": " + food)


del food_stands["Big Fat Bacon"]

print("Food stands at the fair:")
for stand, food in food_stands.items():
    print(stand + ": " + food)

## Tuples

attractions = [("Giant Slide", "East of the Grandstand"), ("Skyride", "Near Dan Patch Avenue")]

new_attraction = ("Haunted House", "Near the Midway")
attractions.append(new_attraction)

print("\nFair attractions:")
for attraction in attractions:
    print(attraction[0] + " is located " + attraction[1])

## Sets

activities = {"Riding the Giant Slide", "Watching the Parade"}

print("\nInitial set of activities:")
print(activities)

activities.add("Watching the Parade")
print("\nAfter trying ti add a duplicate activity:")
print(activities)

activities.remove("Riding the Giant Slide")
print("\nAfter removing an activity:")
print(activities)
