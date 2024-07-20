# Write a program that asks the user to enter a temperature in Celsius and prints "Hot" if it's 30 degrees or more, otherwise prints "Cool".

temperature = int(input("Please enter a temperature: "))
if temperature >= 30:
    print("Be careful its hot outside.")
else:
    print("Omg, its cold outside.")
