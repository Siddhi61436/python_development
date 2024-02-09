def generate_fibonacci_sequence(num_terms):
    fibonacci_sequence = []
    if num_terms <= 0:
        return fibonacci_sequence
    elif num_terms == 1:
        fibonacci_sequence.append(0)
    elif num_terms == 2:
        fibonacci_sequence.extend([0, 1])
    else:
        fibonacci_sequence.extend([0, 1])
        for _ in range(2, num_terms):
            next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_term)
    return fibonacci_sequence

def main():
    try:
        num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_sequence = generate_fibonacci_sequence(num_terms)
            print("Fibonacci Sequence:")
            print(fibonacci_sequence)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
