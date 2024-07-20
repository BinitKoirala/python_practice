# Write a program that asks the user to guess a number between 1 and 10, and keeps asking until they guess correctly.

import random

random_number = random.randint(1, 11)

while True:
    guess = int(input("Guess a number between 1 to 10: "))
    if guess == random_number:
        print("You got it!")
        break
    else:
        print("Better luck next time.")
        continue
