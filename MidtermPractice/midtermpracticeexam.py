def display_options(options):
    """display the menu with numbers next to the options"""
    for i in range(0,len(options)):
        print(f"{i+1}: {options[i]}")

def get_choice(options):
    """takes user input and outputs correct menu item"""
    while True:
        choice = input("Please enter menu item number: ")

        if int(choice) in range(0,(len(options) + 2)):
            break
        else:
            print("Please enter a valid option.")
    if choice == "0":
        return
    menu_item = options[int(choice) - 1]
    return menu_item

# setting up variables
tortilla_types = ["Corn", "Flour", "Whole Wheat"]
filling_types = ["Beans", "Chicken", "Fish", "Beef"]
toppings = ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"]


print("Welcome to Catrin's Build Your Own Taco!")
taco = []

# select tortilla type
print("Let's start by choosing your tortilla:")
display_options(tortilla_types)
user_tortilla = get_choice(tortilla_types)

print(f"You selected a {user_tortilla.lower()} tortilla")

# selct filling type
print("Next let's select your filling:")
display_options(filling_types)
user_filling = get_choice(filling_types)

print(f"You selected {user_filling.lower()} for your filling.")

# select toppings
print("Please select your toppings! Enter 0 when you are finished")
display_options(toppings)
user_toppings = []

while True:
    topping = get_choice(toppings)

    if topping == None:
        break
    else:
        user_toppings.append(topping)
        print(f"Added {topping.lower()}.")

if user_toppings == []:
    print("You selected no toppings.")
else:
    for i in range(0,len(user_toppings)):
        user_toppings.append(user_toppings.pop(0).lower())
    print("Your toppings are " + ", ".join(user_toppings) + ".")

# output taco

print("Your order is:")

if user_toppings == []:
    print("A " + user_tortilla + " tortilla with " + user_filling + ".")
else:
    print("A " + user_tortilla.lower() + " tortilla with " + user_filling.lower() + " and " + ", ".join(user_toppings) + ".")

if "salsa" in user_toppings:
    print("One spicy salsa taco coming up!")

print("Thank you for ordering from Catrina's Mexican Grill!")
