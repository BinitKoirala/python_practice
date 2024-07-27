# Write a function calculate_monthly_payment(principal, rate, years) that calculates and returns the monthly payment for a loan given the principal amount, interest rate, and loan duration in years.

def calculate_monthly_payment(principal, annual_rate, years):
    """
    Calculates the monthly payment for a loan.
    
    Parameters:
    principal (float): The principal loan amount.
    annual_rate (float): The annual interest rate (as a decimal, e.g., 0.05 for 5%).
    years (int): The loan duration in years.
    
    Returns:
    float: The monthly payment amount.
    """
    
    monthly_rate = annual_rate / 12
    
    total_payments = years * 12
    
    monthly_payment = (principal * monthly_rate * (1 + monthly_rate)**total_payments) / ((1 + monthly_rate)**total_payments - 1)
    
    return monthly_payment


principal = 5000  
annual_rate = 0.10  
years = 40         

monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"The monthly payment is: ${monthly_payment:.2f}")
