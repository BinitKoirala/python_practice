# Write a function generate_multiplication_table(n) that prints the multiplication table of a given number n from 1 to 10.

def generate_multiplication_table(n):
    """
    Prints the multiplication table of a given number n from 1 to 10.

    Args:
        n (int): The number for which to generate the multiplication table.
    """
    for i in range(1, 10 + 1):
        product = n * i
        print(f"{n} x {i} = {product}")
        
generate_multiplication_table(5)