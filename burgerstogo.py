## Burgers to Go 
## 

BURGER_PRICE = 10.30
TOPPINGS = {'tomato': 0.50,
            'pickles': 0.50,
            'lettuce': 0.50,
            'onions': 0.50,
            'mushrooms': 1.00,
            'cheese': 1.00,
            'bacon': 1.00,
            'pickled onions': 1.00}

toppings_list = list(TOPPINGS.items())

def print_burger(burger):
    print(f"{burger['name']}:")
    if len(burger['toppings']) < 1:
        print("  No Toppings")
        return
    else:
        for topping in burger['toppings']:
            print(f"  {topping}")



def get_burger_cost(burger):
    """calculates total cost of burger"""
    cost = 0
    cost =  cost + BURGER_PRICE
    if len(burger['toppings']) > 1:
        for topping in burger['toppings']:
            cost += TOPPINGS[topping]
    return cost

def display_options(options):
    """prints out numbered list of options starting at 1 with price"""
    for i in range(0, len(options)):
        print(f"{i + 1}: {options[i][0]:<15} ${options[i][1]:.2f}")

def print_receipt(burgers):
    """ Prints out the receipt for the order of burgers"""
    total = 0
    print("RECEIPT")
    for burger in burgers:
        print()
        print(f"{burger["name"]:<15} ${BURGER_PRICE:.2f}")
        if len(burger["toppings"]) < 1:
            print(f"- {"no toppings":<13} ${0:.2f}")
        else:
            for topping in burger["toppings"]:
                print(f"- {topping:<13} ${TOPPINGS[topping]:.2f}")
        subtotal = get_burger_cost(burger)
        total += subtotal
        print(f"{"subtotal":<15} ${subtotal:.2f}")
    print("------------------------")
    print(f"{"TOTAL":<15} ${total:.2f}")

def yes_no_input(text):
    """takes user input y = true or n = false"""
    while True:
        user_input = input(text)
        if user_input.lower() == 'y':
            return True
        elif user_input.lower() == 'n':
            return False
        else:
            print("Invalid input. Please enter y or n")

def numbered_input(start, stop):
    """checks if input is a valid number for list of objects"""
    while True:
        user_input = input(f"Please enter your choice or 0 to exit.\n")
        if user_input.isdecimal() and int(user_input) in range(start, stop + 1):
            return int(user_input)
        else:
            print(f'Enter a number {start}-{stop}.')
            
def add_burger(burgers, burger):
    burgers.append(burger)
    return burgers

## Ordering Burgers

print("Welcome to Burgers to Go!")

burger_count = 1
burgers = []

# burger making loop
# order burger 
# ask if more burgers 
# if more burgers order another burger
# if false print receipt
while True:
    
    burger = {'name': f'Hamburger {burger_count}'}
    burger['toppings'] = []
    
    print(f'Ordering {burger['name']}')
    
    
    # Adding toppings loop
    while True:
        add_toppings = yes_no_input("Would you like to add toppings? y/n\n")
        if not add_toppings:
            break

        print("Toppings:")
        display_options(toppings_list)
        # more_toppings = yes_no_input("Would you like to add a topping? y/n\n")
        # if not more_toppings:
        #     break
        while True:
            topping_choice = numbered_input(0, len(toppings_list))
            
            if topping_choice == 0:
                break

            burger['toppings'].append(toppings_list[topping_choice - 1][0])
            print(f'Added {toppings_list[topping_choice - 1][0]} to your burger.\n')

        if topping_choice == 0:
            break

    
    print(f'Finished ordering {burger['name']}')
    # ! information about burger

    burger['toppings'].sort()

    print_burger(burger)

    burgers = add_burger(burgers, burger)

    # Adding another burger
    more_burgers = yes_no_input("Would you like to add a burger? y/n\n")
    if more_burgers:
        burger_count += 1
        continue
    if not more_burgers:
        break

print("Thank you for ordering from Burgers to Go!")
print("Here is your receipt:\n")
print_receipt(burgers)