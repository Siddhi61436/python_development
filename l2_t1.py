import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess it!")

    
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
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
    guessing_game()
