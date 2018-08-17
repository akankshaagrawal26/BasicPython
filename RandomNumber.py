import random
from random import randrange

num = random.randrange(1,101,2)    #Generating random numbers
guess = int(input("Please guess a number between 1-100 : "))
print("Random number is :",num)
if guess < num:
    print("Number guessed is too low")
elif guess > num:
    print("Number guessed is too high")
else:
    print("You guessed the right number")