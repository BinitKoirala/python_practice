# Write a function display_calendar_month(month, year) that prints the calendar for a given month and year. Use Python's built-in calendar module.

import calendar

def display_calendar_month(month, year):
    """
    This function prints the calendar for a given month and year.
    
    Parameters:
    month (int): The month for which to print the calendar (1-12).
    year (int): The year for which to print the calendar.
    """
    cal = calendar.month()