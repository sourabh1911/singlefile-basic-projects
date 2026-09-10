# Treasure Hunt
# Explore the cave, follow the hints, and find the hidden treasure!

import random


def get_board_size():
    """Return the board size for a single round."""
    return 5


def get_move():
    """Prompt for and validate a move."""
    move_map = {
        "w": (-1, 0),
        "s": (1, 0),
        "a": (0, -1),
        "d": (0, 1),
    }

    while True:
        move = input("Move (W/A/S/D) or Q to quit: ").strip().lower()

        if move == "q":
            return None

        if move in move_map:
            return move_map[move]

        print("Invalid move! Use W, A, S, or D.")


def print_board(player_row, player_col, treasure_row, treasure_col, size):
    """Display the current board with the player position."""
    print("\nBoard:")
    print("   " + " ".join(str(i) for i in range(size)))

    for row in range(size):
        cells = []
        for col in range(size):
            if row == player_row and col == player_col:
                cells.append("P")
            elif row == treasure_row and col == treasure_col:
                cells.append("T")
            else:
                cells.append(".")
        print(f"{row}  " + " ".join(cells))


def get_hint(player_row, player_col, treasure_row, treasure_col):
    """Return a clue based on distance to the treasure."""
    distance = abs(player_row - treasure_row) + abs(player_col - treasure_col)

    if distance == 0:
        return "You found the treasure!"
    if distance <= 1:
        return "Very hot! The treasure is almost under your feet!"
    if distance <= 2:
        return "Warm! You're close to the treasure."
    if distance <= 4:
        return "Cool. Keep moving in the right direction."
    return "Cold. The treasure is far away."


def play_round():
    """Play one round of Treasure Hunt."""
    size = get_board_size()
    max_moves = 10
    player_row = 0
    player_col = 0
    treasure_row = random.randint(0, size - 1)
    treasure_col = random.randint(0, size - 1)
    moves_used = 0

    print("\n=== Treasure Hunt ===")
    print(f"Find the hidden treasure on a {size}x{size} board.")
    print(f"You have {max_moves} moves to win.")

    while moves_used < max_moves:
        print_board(player_row, player_col, treasure_row, treasure_col, size)
        print(get_hint(player_row, player_col, treasure_row, treasure_col))
        print(f"Moves left: {max_moves - moves_used}")

        move = get_move()
        if move is None:
            print("You quit the hunt. Better luck next time!")
            return False

        row_change, col_change = move
        new_row = player_row + row_change
        new_col = player_col + col_change

        if not (0 <= new_row < size and 0 <= new_col < size):
            print("You hit a wall! Choose another direction.")
            continue

        player_row, player_col = new_row, new_col
        moves_used += 1

        if player_row == treasure_row and player_col == treasure_col:
            print_board(player_row, player_col, treasure_row, treasure_col, size)
            print("\n🎉 Congratulations! You found the treasure!")
            return True

        if moves_used >= max_moves:
            print_board(player_row, player_col, treasure_row, treasure_col, size)
            print("\n❌ You ran out of moves! The treasure was never found.")
            print(f"The treasure was at row {treasure_row}, column {treasure_col}.")
            return False

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
            play_round()
        elif choice == "2":
            print("Goodbye! Thanks for playing!")
            break
        else:
            print("Invalid choice! Please choose 1 or 2.")


if __name__ == "__main__":
    main()
