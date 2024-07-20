# Write a program that asks the user to enter their age and prints "Adult" if they are 18 or older, otherwise prints "Minor".

age = int(input("Please enter your age: "))
if age >= 18:
    print("You are an Adult.")
else:
    print("You are a Minor.")
