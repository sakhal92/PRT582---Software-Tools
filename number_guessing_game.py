"""
This program generates a random 4 digit number.
The player receives hints after each guess to help them
figure out the correct number generated. The game continues
until the player either guesses the correct number or decides to quit.
Once the game ends, the player is given option to play again or exit.
"""

import random


def play_game():
    """
    Generates a random number, asks the user for a guess or to quit
    Calls provide_hints function to check if the guessed number is correct
    Asks the user if they want to play again once the game ends.
    """
    while True:
        # Generate a new random four-digit number
        actual_number = ''.join(random.sample('0123456789', 4))
        attempts = 0
        print("Welcome to the Number Guessing Game!")
        while True:
            guess = input("Enter your guess (or 'quit' to exit): ")
            if guess.lower() == 'quit':
                print("Thanks for playing!")
                return
            if len(guess) != 4 or not guess.isdigit():
                print("Invalid input. Please enter a 4-digit number.")
                continue
            attempts += 1
            hints = provide_hints(actual_number, guess)
            if all(hint == 'circle' for hint in hints):
                print(f"Yay! You guessed the number in {attempts} attempts.")
                while True:
                    play_again = input("Do you want to play again? (yes/no): ")
                    if play_again.lower() == 'no':
                        print("Thanks for playing!")
                        return  # ends the game.
                    if play_again.lower() == 'yes':
                        actual_number = ''.join(random.sample('0123456789', 4))
                        attempts = 0
                        break  # Restart the game
            else:
                hint_str = " ".join(hints)
                print("Hints:", hint_str)


def provide_hints(actual_number, guess):
    """
    create a list to store hints
    Compare each digit in the actual number with the guessed number
    """
    hints = []
    for actual_digit, guessed_digit in zip(actual_number, guess):
        if actual_digit == guessed_digit:
            hints.append('circle')
            # If the digit is correct and in the right spot, add 'circle'
        elif guessed_digit in actual_number:
            hints.append('x')
            # If the digit is correct but in the wrong spot, add 'x'
        else:
            hints.append('-')
            # If the digit is not correct, add '-'
    return hints


# Run the game
play_game()
