# Write a function check_internet_connectivity() that checks if the machine is connected to the internet and returns True or False.

import urllib.request

def check_internet_connectivity():
    """
    Checks if the machine is connected to the internet.
    
    Returns:
    bool: True if the machine is connected to the internet, False otherwise.
    """
    try:
        # Attempt to connect to a reliable website
        urllib.request.urlopen('http://www.google.com', timeout=5)
        return True
    except urllib.request.URLError:
        return False

if check_internet_connectivity():
    print("Connected to the internet.")
else:
    print("Not connected to the internet.")
