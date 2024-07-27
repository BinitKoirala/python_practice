# Write a function celsius_to_fahrenheit(celsius) that converts Celsius to Fahrenheit and returns the result.


def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit and returns the result.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
 
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


celsius_temp = 42.0
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"Temperature in Celsius: {celsius_temp}°C")
print(f"Temperature in Fahrenheit: {fahrenheit_temp}°F")
