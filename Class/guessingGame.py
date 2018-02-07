import random
from random import randint
print("Welcome to the number guessing game!")
seed = input("Enter random seed:")
random.seed(seed)
while True:
    answer = randint(1,100)
    guess = 0
    guesses = 0
    while answer != guess:
        print()
        guess=input("please enter a guess:")
        guesses+=1
        if int(guess) < answer:
            print("Higher")
        elif int(guess) > answer:
            print("Lower")
        elif int(guess) == answer:
            print("Congradulations. You guessed it!")
            print("It took you",guesses,"guesses.")
            break
    print()
    again = input("Would you like to play again (yes/no)?")
    if again == 'no':
        break
    elif again == 'yes':
        continue
    
