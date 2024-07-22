# Write a program that asks the user to enter a mode of transportation (car, bus, bike, walk) and prints the average speed using a match-case statement.

transportation_mode = input("Enter a mode of transportation (car, bus, bike, walk): ").lower()
match transportation_mode:
    case "car":
        print("The average speed of a car is 60 mph.")
    case "bus":
        print("The average speed of a bus is 40 mph.")
    case "bike":
        print("The average speed of a bike is 15 mph.")
    case "walk":
        print("The average speed of walking is 3 mph.")
    case _:
        print("Invalid mode of transportation entered. Please enter a valid mode (car, bus, bike, walk).")
