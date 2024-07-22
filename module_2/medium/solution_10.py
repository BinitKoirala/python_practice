# Write a program that asks the user to enter a number of seconds, converts it to hours, minutes, and seconds, and prints the result.

seconds = int(input("Enter a number of seconds: "))
to_hour = (seconds / 3600)
additional_seconds = seconds % 3600
minute = additional_seconds / 60
print (to_hour)
print (minute)