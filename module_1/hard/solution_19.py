# Write a program that prints the numbers from 1 to 100, but stops if a number is divisible by 17.

number = 1
while number <= 100:
    if number % 17 == 0:
        break
    number += 1
    print(number)
