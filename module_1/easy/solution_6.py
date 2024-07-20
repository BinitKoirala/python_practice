# Write a program that asks the user to enter a letter and then prints "Vowel" if the letter is a, e, i, o, or u.

letter = input("Please enter a letter: ").lower()
if letter in ["a", "e", "i", "o", "u"]:
    print("It's a vowel.")
else:
    print("It's a consonant.")
