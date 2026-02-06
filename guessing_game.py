#This script implements a number guessing game using Python.

# Importing random module to generate a random number
import random

def generate_ranom_number():
    """
    Generates a ranom number between 1 and 100.
    Returns:
        int: A randomly selected number. 
    """
    return random.randint(1, 100)
def get_user_guess():
    """
    Prompts the user to enter their guess and validates the input.
    Returns:
        int: The user's guess as an integer.
    """
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
def main():
    """
    Main function to run the number guessing game.
    """
    print("Welcome to the Number Guessing Game!")
    random_number = generate_ranom_number()
    attempts = 0
    while True:
        user_guess = get_user_guess()
        attempts += 1
        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
            break
if __name__ == "__main__":
    main()
    
    