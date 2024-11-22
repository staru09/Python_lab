import re

def validate_name(name):
    """
    Validates the user name.
    - Not empty
    - Not exceed 15 characters
    - Only alphabets
    """
    if not name:
        return False
    if len(name) > 15:
        return False
    if not name.isalpha():
        return False
    return True

def validate_phone_no(phoneno):
    """
    Validates the phone number.
    - Should have exactly 10 digits
    - Should not have special characters or alphabets
    - All digits should not be the same
    """
    if not re.fullmatch(r'\d{10}', phoneno): 
        return False
    if len(set(phoneno)) == 1:
        return False
    return True

def validate_email_id(email_id):
    """
    Validates the email ID.
    - Contains one '@' character
    - Ends with '.com'
    - Domain name is 'gmail', 'yahoo', or 'hotmail'
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@(gmail|yahoo|hotmail)\.com$'
    if not re.fullmatch(pattern, email_id):
        return False
    return True

# Test cases
print(validate_name("JohnDoe"))  
print(validate_name(""))  
print(validate_name("JohnDoe123"))  
print(validate_name("A" * 16))  

print(validate_phone_no("9876543210"))  
print(validate_phone_no("9999999999"))  
print(validate_phone_no("98765abcd0"))  
print(validate_phone_no("123"))  

print(validate_email_id("user@gmail.com"))  
print(validate_email_id("user@yahoo.com"))  
print(validate_email_id("user@hotmail.com"))  
print(validate_email_id("user@unknown.com"))  
print(validate_email_id("user@gmail.org"))  






'''name = input("Enter your name (max 15 characters, only alphabets): ")
phoneno = input("Enter your phone number (10 digits, no special characters): ")
email_id = input("Enter your email ID (must be @gmail.com, @yahoo.com, or @hotmail.com): ")

# Validate inputs
if validate_name(name):
    print("Name is valid.")
else:
    print("Invalid name. Ensure it's not empty, within 15 characters, and contains only alphabets.")

if validate_phone_no(phoneno):
    print("Phone number is valid.")
else:
    print("Invalid phone number. Ensure it's 10 digits, no special characters, and digits are not all the same.")

if validate_email_id(email_id):
    print("Email ID is valid.")
else:
    print("Invalid email ID. Ensure it's in the format username@domain.com with domain as gmail, yahoo, or hotmail.")'''