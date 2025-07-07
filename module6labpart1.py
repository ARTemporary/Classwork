def add_ingredient(ingredient):
    """Add an ingredient to the virtual burger"""
    print("Adding " + ingredient + " to your burger!")
    return

add_ingredient("cheese")
add_ingredient("bacon")
add_ingredient("pickles")

TAX_RATE = 0.085
BURGER_PRICE = 4.99
FRIES_PRICE = 2.49
DRINK_PRICE = 1.29

def calculate_combo_price(has_burger, has_fries, has_drink):
    """calculates the total combo price"""
    subtotal = 0
    if has_burger:
        subtotal += BURGER_PRICE
    if has_fries:
        subtotal += FRIES_PRICE
    if has_drink:
        subtotal += DRINK_PRICE

    tax = TAX_RATE * subtotal
    total_cost = subtotal + tax
    print("Total combo price: $" + str(total_cost))
    return total_cost

calculate_combo_price(True, True, False)

## how to round up?

def order_decision():
    """ask user if they want to supersize their combo"""
    supersize = input("Would you like to supersize your combo? (yes/no): ")

    if supersize.lower() == "yes":
        print("Great Choice!")
        return True
    else:
        print("Remember, life is short—go for the large fries!")
        return False
    
order_decision()

# recursion example

def order_food(menu):
    """order food off a menu, remove item if ordered"""

    if not menu:
        print("Your order is complete. Enjoy your meal!")
        return
    else:
        print("Would you like to order a " + menu.pop(0) + "?")
        input()
        order_food(menu)

menu_items = ["bruger", "fries", "soda"]

order_food(menu_items)