# Write a program that asks the user to enter a number of seconds, converts it to hours, minutes, and seconds, and prints the result.

seconds = int(input("Enter a number of seconds: "))
to_hour = (seconds // 3600)
to_minute = (seconds % 3600) // 60
to_seconds = seconds % 60

print (str(to_hour), "hr", str(to_minute), "min", str(to_seconds), "sec")