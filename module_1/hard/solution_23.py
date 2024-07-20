# Write a program that asks the user to enter three numbers and prints the largest number.

number1 = int(input("Enter the number: "))
number2 = int(input("Enter the number: "))
number3 = int(input("Enter the number: "))

if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3
print("The largest number is:", largest)
