# Write a program that asks the user to enter their name and then prints a greeting message with their name.

name = input("Enter you full name: ").capitalize()
if not name.isalpha():
    print("Please enter a valid name.")
else:
    print("Hi!" + " " + name + "," + " " + "Nice to meet you!")
