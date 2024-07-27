# Write a function get_python_version() that returns the current Python version being used.

import sys

def get_python_version():
    """
    Returns the current Python version being used.
    
    Returns:
    version (str): The current Python version.
    """
    version = sys.version
    return version
print (get_python_version())