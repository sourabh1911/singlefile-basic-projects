# Treasure Hunt
# Search the island and find the hidden treasure before your turns run out.

import random


def generate_board(size=5):
    """Create a board with a hidden treasure position."""
    return random.randint(0, size - 1), random.randint(0, size - 1)


def get_hint(row, col, treasure_row, treasure_col):
    """Return a warm/cold hint based on the distance to the treasure."""
    distance = abs(row - treasure_row) + abs(col - treasure_col)

    if distance == 0:
        return "You found the treasure!"
    if distance <= 1:
        return "Very hot! The treasure is almost on top of you."
    if distance <= 2:
        return "Warm! You're close."
    if distance <= 4:
        return "Cool. Keep searching."
    return "Cold! The treasure is far away."


def print_board(guesses, size=5):
    """Display the current board with marks for guessed tiles."""
    print("\n  " + " ".join(str(i) for i in range(size)))
    for row in range(size):
        line = [str(row)]
        for col in range(size):
            if (row, col) in guesses:
                line.append("X")
            else:
                line.append(".")
        print(" ".join(line))


def play_game():
    """Play one full Treasure Hunt round."""
    size = 5
    max_attempts = 10
    treasure_row, treasure_col = generate_board(size)
    guesses = set()

    print("\n=== Treasure Hunt ===")
    print(f"Find the hidden treasure on a {size}x{size} grid.")
    print(f"You have {max_attempts} attempts.")
    print("Enter coordinates as row col (for example: 2 3)")

    for attempt in range(1, max_attempts + 1):
        print_board(guesses, size)

        while True:
            try:
                raw = input(f"\nAttempt {attempt}/{max_attempts}: Enter row and column: ").strip()
                row_str, col_str = raw.split()
                row = int(row_str)
                col = int(col_str)
            except ValueError:
                print("Please enter two numbers separated by a space, like '2 3'.")
                continue

            if not (0 <= row < size and 0 <= col < size):
                print(f"Choose coordinates between 0 and {size - 1}.")
                continue

            if (row, col) in guesses:
                print("You already guessed that tile. Pick a different spot.")
                continue

            guesses.add((row, col))
            break

        if row == treasure_row and col == treasure_col:
            print_board(guesses, size)
            print(f"\n🎉 You found the treasure at ({row}, {col}) in {attempt} guesses!")
            return True

        print(get_hint(row, col, treasure_row, treasure_col))

    print_board(guesses, size)
    print(f"\n💥 Game over! The treasure was at ({treasure_row}, {treasure_col}).")
    return False


def main():
    """Main menu loop for the game."""
    print("=== Treasure Hunt ===")

    while True:
        print("\nOptions:")
        print("1. Play")
        print("2. Exit")

        choice = input("\nEnter choice (1/2): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye! Thanks for playing.")
            break
        else:
            print("Invalid choice! Please choose 1 or 2.")


if __name__ == "__main__":
    main()
