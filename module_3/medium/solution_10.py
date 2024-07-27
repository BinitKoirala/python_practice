# Write a function send_email(to, subject="No Subject") that sends an email. For this challenge, simply return a formatted string stating the email was sent.

def send_email(to, subject="No Subject"):
    """
    Simulates sending an email by returning a formatted string.
    
    Parameters:
    to (str): The recipient's email address.
    subject (str): The subject of the email. Default is "No Subject".
    
    Returns:
    str: A formatted string stating the email was sent.
    """
    return f"Email sent to {to} with subject '{subject}'."

print (send_email("Ram"))
print (send_email("Hari", "python class"))
