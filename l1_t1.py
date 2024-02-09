def reverse_string(input_str):
    return input_str[::-1]

def main():
    input_string = input("Enter a string: ")
    reversed_string = reverse_string(input_string)
    print("Reversed string:", reversed_string)

if __name__ == "__main__":
    main()
