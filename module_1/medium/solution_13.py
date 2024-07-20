# Write a program that asks the user to enter a day of the week and prints "Weekend" if it's Saturday or Sunday, otherwise prints "Weekday".

day = input("Enter a day of the week: ").capitalize()
match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")
