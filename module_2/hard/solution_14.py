# Write a program that asks the user to enter a traffic light color (red, yellow, green) and prints the corresponding action (stop, slow down, go) using a match-case statement.

color = input("Enter a traffic light color (red, yellow, green): ").lower()
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Slow down")
    case "green":
        print("Go")
    case _:
        print("Invalid color entered. Please enter a valid traffic light color (red, yellow, green).")
