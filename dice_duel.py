# Dice Duel
# Roll the dice and beat the computer to win the match!

import random


def roll_dice():
    """Return the result of rolling a six-sided die."""
    return random.randint(1, 6)


def play_round(player_score, computer_score):
    """Play one round and return the updated scores."""
    print("\nRolling the dice...")

    player_total = roll_dice() + roll_dice()
    computer_total = roll_dice() + roll_dice()

    print(f"You rolled: {player_total}")
    print(f"Computer rolled: {computer_total}")

    if player_total > computer_total:
        player_score += 1
        print("You win this round!")
    elif computer_total > player_total:
        computer_score += 1
        print("Computer wins this round!")
    else:
        print("This round is a draw!")

    return player_score, computer_score


def play_game():
    """Main game loop for the Dice Duel."""
    player_score = 0
    computer_score = 0
    round_number = 1

    print("\n=== Welcome to Dice Duel ===")
    print("First to win 5 rounds wins the match!")

    while player_score < 5 and computer_score < 5:
        print(f"\nRound {round_number}")
        player_score, computer_score = play_round(player_score, computer_score)
        round_number += 1

        print(f"\nScore: You {player_score} - {computer_score} Computer")

        if player_score >= 5 or computer_score >= 5:
            break

        again = input("Roll again? (y/n): ").strip().lower()
        while again not in ["y", "n"]:
            print("Please enter 'y' or 'n'.")
            again = input("Roll again? (y/n): ").strip().lower()

        if again == "n":
            print("Thanks for playing!")
            return

    if player_score > computer_score:
        print("\n🎉 You won the match!")
    elif computer_score > player_score:
        print("\n💻 Computer won the match!")
    else:
        print("\nIt's a draw!")

    print(f"Final score: You {player_score} - {computer_score} Computer")


def main():
    """Menu loop for the game."""
    print("=== Dice Duel ===")

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
