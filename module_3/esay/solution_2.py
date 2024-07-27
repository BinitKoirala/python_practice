# Write a function get_system_info() that returns the operating system name and version.

import platform

def get_system_info():
    """
    Returns the operating system name and version.

    This function uses the `platform` module to retrieve the
    system's operating system name and its version.

    Returns:
        str: A string containing the OS name and version.
    """
    os_name = platform.system()
    os_version = platform.version()
    system_info = f"Operating System: {os_name}, Version: {os_version}"
    
    return system_info

print (get_system_info())

