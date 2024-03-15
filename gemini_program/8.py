import random
import time
import os

# Set of words for typing practice
WORDS = ['apple', 'banana', 'cherry', 'dog', 'elephant', 'fire', 'grape', 'horse', 'ice', 'juice', 'kiwi', 'lion', 'monkey', 'nest', 'orange', 'parrot', 'queen', 'rabbit', 'sun', 'tiger', 'umbrella', 'violin', 'watermelon', 'xylophone', 'yacht', 'zebra']

# Difficulty levels
EASY = 1
MEDIUM = 2
HARD = 3

# Set of punctuation marks for challenge mode
PUNCTUATION = '.,!?"\':;-_()[]'

# Function to generate a typing test
def generate_test(difficulty, length):
    """Generates a typing test.

    Args:
        difficulty: The difficulty of the test.

      length: The length of the test in words.

    Returns:
        A string of words to be typed.
    """

    # word_list = random.sample(WORDS, length)
    word_list = []

    # Adjust the difficulty of the test by adding punctuation marks
    if difficulty == EASY:
        word_list = random.sample(WORDS, length)
    elif difficulty == MEDIUM:
        for word in random.sample(WORDS, length):
            if random.random() < 0.25:
                word_list.append(word + random.choice(PUNCTUATION))
            else:
                word_list.append(word)
    elif difficulty == HARD:
        for word in random.sample(WORDS, length):
            if random.random() < 0.5:
                word_list.append(word + random.choice(PUNCTUATION))
            else:
                word_list.append(word.upper())

    return ' '.join(word_list)


# Function to get user input and calculate accuracy
def get_user_input(test_string):
    """Gets user input and calculates accuracy.

    Args:
        test_string: The string of words to be typed.

    Returns:
        A tuple containing the user's input, the accuracy, and the time taken.
    """

    start_time = time.time()
    user_input = input(test_string)
    end_time = time.time()

    # Calculate accuracy
    accuracy = sum(1 for i in range(len(test_string)) if test_string[i] == user_input[i]) / len(test_string)

    return user_input, accuracy, end_time - start_time


# Function to print results
def print_results(user_input, accuracy, time):
    """Prints the results of a typing test.

    Args:
        user_input: The user's input.
        accuracy: The accuracy of the test.

 time: The time taken to complete the test.
    """

    print()
    print('Your input:', user_input)
    print('Accuracy:', accuracy * 100, '%')
    print('Time taken:', time, 'seconds')


# Function to save progress
def save_progress(accuracy, time):
    """Saves the user's progress to a file.

    Args:
        accuracy: The accuracy of the test.
        time: The time taken to complete the test.
    """
    with open('progress.txt', 'a') as f:
        f.write(f'{accuracy * 100:.2f},{time:.2f}\n')


# Function to load progress
def load_progress():
    """Loads the user's progress from a file.

    Returns:
        A list of tuples containing the user's accuracy and time for each test.
    """
    progress = []
    try:
        with open('progress.txt', 'r') as f:
            for line in f:
                accuracy, time = line.strip().split(',')
                progress.append((float(accuracy), float(time)))
    except FileNotFoundError:
        pass
    return progress


# Function to clear the screen
def clear_screen():
    """Clears the screen."""

    os.system('cls' if os.name == 'nt' else 'clear')


# Main function
def main():
    """Runs the typing practice program."""

    # Load progress
    progress = load_progress()

    # Display the main menu
    while True:
        clear_screen()

        print('Typing Practice')
        print('1. Start a new test')
        print('2. View progress')
        print('3. Quit')


        choice = input('> ')

        # Start a new test
        if choice == '1':
            # Get the difficulty level
            difficulty = int(input('Choose a difficulty level (1 for easy, 2 for medium, 3 for hard): '))

            # Get the length of the test
            length = int(input('Enter the length of the test (in words): '))

            # Generate the test
            test_string = generate_test(difficulty, length)

            # Get user input and calculate accuracy
            user_input, accuracy, time = get_user_input(test_string)


           # Print the results
            print_results(user_input, accuracy, time)

            # Save progress
            save_progress(accuracy, time)

        # View progress
        elif choice == '2':
            clear_screen()
            print('Progress:')

            for accuracy, time in progress:
                print(f'Accuracy: {accuracy:.2f}%, Time: {time:.2f} seconds')

            # Quit
        elif choice == '3':
            break

        # Invalid input
        else:
            print('Invalid choice. Please try again.')


        input('Press any key to continue...')


if __name__ == '__main__':
    main()