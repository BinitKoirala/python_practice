def calculate_price(price, tax_rate=0.05):
    """
    Returns the total price including tax.

    Args:
        price (float): The initial price before tax.
        tax_rate (float): The tax rate to apply. Defaults to 0.05 (5%).

    Returns:
        float: The total price including tax.
    """
    tax_amount = price * tax_rate
    total_price = price + tax_amount
    return total_price

price = 50
tax_rate = 10

print(calculate_price(50,10))