# Write a function find_maximum(number_list) that returns the maximum element in a list.

def find_maximum(number_list):
    """
    Returns the maximum element in a list of numbers.
    
    Parameters:
    number_list (list): A list of numbers.
    
    Returns:
    max_element (number): The maximum element in the list.
    """
    if not number_list:
        return None  
    
    max_element = number_list[0]
    for number in number_list:
        if number > max_element:
            max_element = number
            
    return max_element
