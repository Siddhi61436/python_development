import re

def validate_email():
    
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

   
    email = input("Enter an email address: ")

   
    if re.match(pattern, email):
        return True
    else:
        return False


if validate_email():
    print("Valid email address.")
else:
    print("Invalid email address.")
