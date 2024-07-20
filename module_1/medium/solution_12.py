# Write a program that asks the user to enter a score and prints "A" for 90 and above, "B" for 80 to 89, "C" for 70 to 79, "D" for 60 to 69, and "F" for below 60.

score = int(input("Please Enter your score: "))
if score >= 90:
    print("Congratulations!, You have secured Grade A.")
elif score >= 80:
    print("Congratulations!, You have secured Grade B.")
elif score >= 70:
    print("Congratulations!, You have secured Grade C.")
elif score >= 60:
    print("Congratulations!, You have secured Grade D.")
else:
    print("Sorry, you have Failed.")
