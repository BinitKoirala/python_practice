# Write a program that asks the user to enter a number and prints "Even" if the number is divisible by 2, otherwise prints "Odd".

number = int(input("Please enter a number: "))
if number % 2 == 0:
    print("The number you entered is Even.")
else:
    print("The number is odd.")