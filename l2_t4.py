def is_palindrome(input_str):
    # Remove spaces and punctuation and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in input_str if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

def main():
    user_input = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print("Yes, it's a palindrome.")
    else:
        print("No, it's not a palindrome.")

if __name__ == "__main__":
    main()
