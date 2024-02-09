def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Conversion Program")
    print("==============================")

    while True:
        try:
            temperature = float(input("Enter the temperature value: "))
            unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").upper()

            if unit == 'C':
                converted_temperature = celsius_to_fahrenheit(temperature)
                print(f"{temperature} Celsius is equal to {converted_temperature} Fahrenheit.")
            elif unit == 'F':
                converted_temperature = fahrenheit_to_celsius(temperature)
                print(f"{temperature} Fahrenheit is equal to {converted_temperature} Celsius.")
            else:
                print("Invalid unit of measurement. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

            break  # Exit the loop after successful conversion
        except ValueError:
            print("Invalid input. Please enter a valid temperature value.")

if __name__ == "__main__":
    main()
