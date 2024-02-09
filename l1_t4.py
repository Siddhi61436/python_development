def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def modulo(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x % y

def calculator():
    print("Welcome to Basic Calculator Program")
    print("===================================")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /, %): ")

            if operator == '+':
                print("Result:", add(num1, num2))
            elif operator == '-':
                print("Result:", subtract(num1, num2))
            elif operator == '*':
                print("Result:", multiply(num1, num2))
            elif operator == '/':
                print("Result:", divide(num1, num2))
            elif operator == '%':
                print("Result:", modulo(num1, num2))
            else:
                print("Invalid operator!")

            another_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if another_calculation.lower() != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    calculator()