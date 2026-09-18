"""Memory Match game played in the terminal."""

import random
import time


SYMBOLS = ["A", "B", "C", "D", "E", "F", "G", "H"]


def build_deck(symbols=None):
    """Create a shuffled deck of matching pairs."""
    choices = list(symbols or SYMBOLS)
    deck = choices * 2
    random.shuffle(deck)
    return deck


def display_board(board, revealed):
    """Print the current board with hidden cards covered."""
    print("\n  1  2  3  4")
    for row in range(4):
        cells = []
        for col in range(4):
            idx = row * 4 + col
            if revealed[idx]:
                cells.append(board[idx])
            else:
                cells.append("#")
        print(f"{row + 1} {' '.join(cells)}")
    print()


def get_choice(prompt, revealed, matched):
    """Validate and return a card index from 1 to 16."""
    while True:
        choice = input(prompt).strip()
        if not choice or not choice.isdigit():
            print("Please enter a number from 1 to 16.")
            continue

        idx = int(choice) - 1
        if not 0 <= idx < 16:
            print("Number must be between 1 and 16.")
            continue

        if revealed[idx] or idx in matched:
            print("That card is already matched or revealed. Choose another one.")
            continue

        return idx


def play_memory_match(deck=None):
    """Run one game and return the number of moves used."""
    if deck is None:
        deck = build_deck()

    revealed = [False] * len(deck)
    matched = []
    moves = 0

    print("\n=== Memory Match ===")
    print("Flip two cards at a time and match all pairs before you run out of turns.")
    print("Cards are numbered from 1 to 16, left to right, top to bottom.")

    while len(matched) < len(deck):
        display_board(deck, revealed)
        first = get_choice("Choose first card (1-16): ", revealed, matched)
        revealed[first] = True

        display_board(deck, revealed)
        second = get_choice("Choose second card (1-16): ", revealed, matched)
        revealed[second] = True
        moves += 1

        print("You flipped:", deck[first], "and", deck[second])

        if deck[first] == deck[second]:
            print("Nice match!")
            matched.extend([first, second])
            revealed[first] = True
            revealed[second] = True
        else:
            print("No match this time. Keep trying!")
            time.sleep(1.2)
            revealed[first] = False
            revealed[second] = False

        if len(matched) == len(deck):
            break

        print("Press Enter to continue...")
        input()

    print("\nCongratulations! You matched every card in", moves, "moves.")
    return moves


def main():
    """Display the menu and play repeatedly."""
    while True:
        print("\n=== Memory Match Menu ===")
        print("1. Play Memory Match")
        print("2. Exit")

        choice = input("\nEnter choice (1/2): ").strip()

        if choice == "1":
            play_memory_match()
            again = input("\nPlay again? (y/n): ").lower()
            if again != "y":
                print("Thanks for playing!")
                break
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1 or 2.")


if __name__ == "__main__":
    main()
