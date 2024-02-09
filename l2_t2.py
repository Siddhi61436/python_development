import random

def number_guesser(min_num, max_num):
    print(f"Welcome to the Number Guesser Game!")
    print(f"I have selected a random number between {min_num} and {max_num}.")
    print("Try to guess it!")

    # Generate a random number between the specified range
    secret_number = random.randint(min_num, max_num)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Enter your guess (between {min_num} and {max_num}): "))
            attempts += 1

            if guess < min_num or guess > max_num:
                print(f"Please enter a number between {min_num} and {max_num}.")
                continue

            if guess == secret_number:
                print(f"Congratulations! You've guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    min_range = int(input("Enter the minimum number for the range: "))
    max_range = int(input("Enter the maximum number for the range: "))

    number_guesser(min_range, max_range)
