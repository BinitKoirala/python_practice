# Write a program that asks the user to enter a day of the week and prints whether it is a weekday or weekend using a match-case statement.

day = input("Enter a day of the week: ").capitalize()
match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")
