# Write a program that asks the user to enter numbers until they enter a negative number, then prints the sum of all the numbers entered.

sum = 0
while True:
    number = int(input("Please enter positive number to add:"))
    if number < 0:
        break
    sum += number
print(sum)
