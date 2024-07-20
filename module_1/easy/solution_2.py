# Write a program that asks the user to enter a number and then prints the square of that number.

number = input("Enter a number: ")
if not number.isdigit():
    print("Please enter a number next time!")
else:
    number = int(number)
    print("The square is", number**2)
