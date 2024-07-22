# Write a program that asks the user to enter a temperature in Celsius, converts it to Fahrenheit, and prints the result.

temperature = int(input("Enter a Tempearture in degree Celsius: "))
conversion = temperature * 9 / 5 + 32
print("The temperature is " + str(conversion) + " degree Fahrenheit.")
