# Word Scramble
# Unscramble the letters and guess the hidden word before time runs out!

import random


WORDS = [
    "planet",
    "forest",
    "puzzle",
    "garden",
    "rocket",
    "python",
    "library",
    "diamond",
    "sunrise",
    "journey",
    "treasure",
    "harvest",
    "captain",
    "whistle",
    "lantern",
]


def scramble_word(word):
    """Return a shuffled version of a word."""
    shuffled = word
    while shuffled == word:
        shuffled = "".join(random.sample(word, len(word)))
    return shuffled


def play_round(score):
    """Play one round of the game and return the updated score."""
    word = random.choice(WORDS)
    clue = scramble_word(word)

    print(f"\nUnscrambled word: {clue}")
    guess = input("Your guess: ").strip().lower()

    if guess == "quit":
        print(f"Thanks for playing! Final score: {score}")
        return None

    if guess == word:
        score += 1
        print("Correct! Great job!")
    else:
        print(f"Not quite. The word was: {word}")

    print(f"Current score: {score}")
    return score


def play_game():
    """Main loop for the Word Scramble game."""
    score = 0
    rounds = 0

    print("\n=== Welcome to Word Scramble ===")
    print("Type 'quit' at any time to stop playing.")

    while True:
        result = play_round(score)
        if result is None:
            return

        score = result
        rounds += 1

        if rounds >= 5:
            print(f"\nGame over! You scored {score} point(s) out of 5 rounds.")
            play_again = input("Play again? (y/n): ").strip().lower()
            while play_again not in ["y", "n"]:
                print("Please enter 'y' or 'n'.")
                play_again = input("Play again? (y/n): ").strip().lower()

            if play_again == "n":
                print("Thanks for playing!")
                return

            score = 0
            rounds = 0


def main():
    """Menu loop for the game."""
    print("=== Word Scramble ===")

    while True:
        print("\nOptions:")
        print("1. Play")
        print("2. Exit")

        choice = input("\nEnter choice (1/2): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1 or 2.")


if __name__ == "__main__":
    main()
