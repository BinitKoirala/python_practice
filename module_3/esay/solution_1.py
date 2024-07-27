# Write a function display_list(list) that takes a list and prints each element on a new line.

def display_list(element_list: list) -> None:
    """
    This function takes a list of number as an argument and prints each element on a new line.
    
    Parameters:
    element_list (list): The list to be printed.
    """
    for item in element_list:
        print(item)

display_list([1,2,3])