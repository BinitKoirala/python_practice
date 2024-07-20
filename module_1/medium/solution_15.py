# Write a program that asks the user to enter a month and prints the number of days in that month.

month = input("Enter a month: ").capitalize()
match month:
    case "January" | "March" | "May" | "July" | "August" | "October" | "December":
        print("31 days")
    case "April" | "June" | "September" | "November":
        print("30 days")
    case "February":
        print("28 or 29 day")
