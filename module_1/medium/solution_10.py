# Write a program that asks the user to enter a number and prints "Positive Even" if the number is positive and even, "Positive Odd" if the number is positive and odd, and "Negative" if the number is negative.

number = int(input("Please enter a number:"))
if number > 0:
    if number % 2 == 0:
        print("The number you entered is Positive even.")
    else:
        print("The number you entered is Positive odd.")
else:
    print("The number you entered is Negative.")
