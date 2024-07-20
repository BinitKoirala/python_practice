# Write a program that asks the user to enter their age and prints "Child" if they are less than 13, "Teen" if they are between 13 and 19, and "Adult" if they are 20 or older.

age = int(input("Please enter your age: "))
if age < 13:
    print("You are a Child.")
else:
    if age <= 19:
        print("You are a Teen.")
    else:
        print("You are an Adult.")
