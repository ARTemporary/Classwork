# Author: Alice Radtke
# Date: June 28 2025
# Random Integer Guessing Game

## version one  ---  
## would like to add more complicated hints for how far from correct number
## 1/2 distance? within ten numbers?


import random

print("Welcome to the Magical Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("But beware, the number could change if you take too long!")

secret_number = random.randint(1, 100)
# secret_number = 6  #for testing

while True:
    
    ## main gameplay loop
    for guess_count in range(1, 6):   # 5 guesses before the number changes
        got_it = False
        guess_input = input("Enter your guess: ")
        

        if int(guess_input) == secret_number:   #correct
            print("Congradulations! Your guess was correct.")
            print("The secret number was", secret_number)
            got_it =True
            break

        elif int(guess_input) > secret_number:  #above
            print("Your guess was too large.")

        elif int(guess_input) < secret_number:  #below
            print("Your guess was too small")
    

    
    user_continue = input("Would you like to continue? y/n \n")
    
    ## add in a way to check user input  
    # user_continue.lower did not work when inputting n -- Why?

    if user_continue == "n":    #quit
        break

    
    if user_continue == "y":    #change number and start over
        secret_number = random.randint(1, 100)
        # secret_number = 7   # for testing

## Game done

if got_it != True:      #Only print if the last guessing game failed
    print("The secret number was:")
    print(secret_number)


print("Thanks for playing!")
