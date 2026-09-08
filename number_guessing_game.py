# Number Guessing Game
# Try to guess the hidden number before you run out of attempts.
# Guess the secret number before you run out of attempts.

import random


def play_round():
    """Play one round of the number guessing game."""
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("\n=== Guess the Number ===")
    print(f"I picked a number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return True

        if guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Attempts left: {remaining}")

    print(f"Sorry, you ran out of attempts. The number was {secret_number}.")
DIFFICULTIES = {
    "1": ("Easy", 50, 10),
    "2": ("Medium", 100, 7),
    "3": ("Hard", 200, 6),
}


def choose_difficulty():
    """Return the selected difficulty settings."""
    while True:
        print("\nChoose a difficulty:")
        print("1. Easy (1-50, 10 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard (1-200, 6 attempts)")

        choice = input("Enter choice (1/2/3): ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]

        print("Invalid choice! Please choose 1, 2, or 3.")


def get_guess(lower_bound, upper_bound):
    """Read and validate a guess within the current number range."""
    while True:
        guess = input(
            f"Enter your guess ({lower_bound}-{upper_bound}): "
        ).strip()

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if lower_bound <= guess <= upper_bound:
            return guess

        print(f"Your guess must be between {lower_bound} and {upper_bound}.")


def play_round():
    """Play one round and return whether the player won."""
    difficulty, upper_bound, max_attempts = choose_difficulty()
    secret_number = random.randint(1, upper_bound)

    print(f"\n{difficulty} mode: I picked a number from 1 to {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess it.")

    for attempt in range(1, max_attempts + 1):
        guess = get_guess(1, upper_bound)

        if guess == secret_number:
            print(f"Correct! You found it in {attempt} attempt(s).")
            return True

        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        remaining = max_attempts - attempt
        if remaining:
            print(f"Attempts remaining: {remaining}")

    print(f"Out of attempts! The number was {secret_number}.")
    return False


def main():
    """Main menu for the game."""
    print("=== Number Guessing Game ===")

    while True:
        print("\nOptions:")
        print("1. Play")
        print("2. Exit")

        choice = input("\nEnter choice (1/2): ")

        if choice == "1":
            play_round()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1 or 2.")


if __name__ == "__main__":
    main()
    """Run the game menu."""
    print("=== Number Guessing Game ===")

    while True:
        play_round()

        while True:
            again = input("\nPlay again? (y/n): ").strip().lower()
            if again in ["y", "n"]:
                break
            print("Please enter 'y' or 'n'.")

        if again == "n":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
