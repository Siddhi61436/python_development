def count_word_occurrences(file_name):
    word_counts = {}

    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into words
            words = line.strip().split()
            # Count occurrences of each word
            for word in words:
                # Remove punctuation marks and convert to lowercase
                word = word.strip('.,!?"\'').lower()
                # Update the word count dictionary
                word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def display_word_counts(word_counts):
    # Sort the word counts dictionary by keys (words) in alphabetical order
    sorted_word_counts = sorted(word_counts.items())

    print("Word Counts:")
    print("============")
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

def main():
    file_name = input("Enter the name of the text file: ")

    try:
        word_counts = count_word_occurrences(file_name)
        display_word_counts(word_counts)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

if __name__ == "__main__":
    main()
