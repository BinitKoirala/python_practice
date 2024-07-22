# Write a program that asks the user to enter a month and prints the season (spring, summer, fall, winter) using a match-case statement.

month = input("Enter a month: ").capitalize()
match month:
    case "December" | "January" | "February":
        print("Winter")
    case "March" | "April" | "May":
        print("Spring")
    case "June" | "July" | "August":
        print("Summer")
    case "September" | "October" | "November":
        print("Fall")
    case _:
        print("Invalid month entered. Please enter a valid month.")
