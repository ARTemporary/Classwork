## Name: Alice Radtke
## Date: 2025-07-06
## Description: Dad Joke App

import random   # for later

# List of the jokes

dad_jokes = ["What kind of shoes do frogs wear?\nOpen-toad sandals.", "Why do crabs never volunteer?\nBecause they're shell-fish.", "What's brown and sticky?\nA stick.", "Why do melons have wedding?\nThey cantelope.", "Why can't dinosaurs clap their hands?\nBecause they're extinct.", "Where do surfers go for an education?\nBoarding school.", "Why are libraries so tall?\nBecause they have many stories.", "How do fish pay for groceries?\nWith sand dollars.", "How do bees get to school?\nOn the school buzz.", "Where do fingers grow?\nOn palm trees."]

# Welcome message and number of dad jokes

print("Welcome! We have " + str(len(dad_jokes)) + " dad jokes in our collection.")

# Loop of hearing jokes
while True:
    want_jokes = input("Would you like to hear some dad jokes?\n")

    if want_jokes[0].lower() != 'y':    # quit the program
        break
    

    # print four random jokes
    for i in range(0,4):
        # joke = random.choice(dad_jokes) 
        # print(joke + "\n")
        # not using above code because of duplicate jokes
        # below code removes jokes from list

        b = 9 - i   # largest index value

        rand_num = random.randint(0, b) # random index value
        
        joke = dad_jokes.pop(rand_num)

        print(joke + "\n")
        
    b = 5   # the largest index of jokes left 

    # loop for more jokes
    while True:
        more_jokes = input("Would you like to hear another joke?\n")

        if more_jokes[0].lower() != 'y':    # quit the program
            break

        if len(dad_jokes) == 0: # list is empty
            print("Sorry, there are no more jokes to hear.\n")
            break

       
        rand_num = random.randint(0,b)

        joke = dad_jokes.pop(rand_num)

        print(joke + "\n")

        b = b - 1   # lower to largest index value



    

    break



print("Goodbye!") # exit message