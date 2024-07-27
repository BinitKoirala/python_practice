# Write a function is_palindrome(string) that checks if a given string s is a palindrome and returns True or False.

def is_palindrome(s):
    """
    Checks if a given string is a palindrome.
    
    Parameters:
    s (str): The string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    
    s = s.replace(" ", "").lower() 
  
    return s == s[::-1]

print(is_palindrome("s os sos"))  
print(is_palindrome("hello"))  
