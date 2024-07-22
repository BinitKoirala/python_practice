# Write a program that asks the user to enter their height in centimeters, converts it to inches, and prints the result.

height = int(input("Enter your height in centimeters: "))
conversion = round(height / 2.54)
print("Your height is " + str(conversion) + " Inches.")
