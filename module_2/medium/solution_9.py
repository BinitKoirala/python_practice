# Write a program that asks the user to enter a distance in kilometers, converts it to miles, and prints the result.

distance = int(input("Enter a distance in kilometers: "))
conversion = round(distance / 1.609 )
print("The disatnce is " + str(conversion) + " miles.")