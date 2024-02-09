def password_strength_checker(password):
    # Define criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(not char.isalnum() for char in password)

    # Evaluate the strength of the password based on criteria
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong"
    else:
        return "Weak"

# Test the function
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    strength = password_strength_checker(user_password)
    print(f"The strength of your password is: {strength}")
