import random

# List of predefined words
words = ["python", "coding", "computer", "program", "developer"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect attempts
max_attempts = 6
wrong_attempts = 0

print("Welcome to Hangman Game!")

while wrong_attempts < max_attempts:

    # Display the current word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player won
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word!")
        break

    # Get user input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_attempts += 1
        print("Wrong guess!")

        print("Attempts remaining:", max_attempts - wrong_attempts)

# Check if the player lost
if wrong_attempts == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", secret_word)