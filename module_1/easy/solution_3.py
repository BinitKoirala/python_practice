# Write a program that asks the user to enter their age and then prints how old they will be in 10 years.

age = input("Enter your current age: ")
if not age.isdigit():
    print("Please enter a valid number.")
else:
    age = int(age) + 10
    print("In 10 years your age will be", age, ".")
