# Write a function count_vowels(string) that returns the number of vowels in the given string.

def count_vowels(string):
    """
    Returns the number of vowels in the given string.

    Args:
        string (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """

    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
            
    return count


print(count_vowels("binit"))


