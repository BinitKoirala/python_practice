# rite a program that asks the user to enter a traffic light color (red, yellow, green) and prints "Stop" for red, "Slow down" for yellow, and "Go" for green.

traffic_light = input("Enter a traffic light color: ").capitalize()
match traffic_light:
    case "Red":
        print("Stop!")
    case "Yellow":
        print("Slow Down!")
    case "Red":
        print("GO!")
