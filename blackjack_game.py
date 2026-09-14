# Blackjack Game
# Try to beat the dealer without going over 21.

import random


SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


def create_deck():
    """Return a shuffled deck of cards."""
    deck = [(rank, suit) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck


def card_name(card):
    """Return a readable name for a card."""
    rank, suit = card
    return f"{rank} of {suit}"


def hand_value(hand):
    """Return the best Blackjack value for a hand."""
    value = 0
    aces = 0

    for rank, _ in hand:
        if rank in ["J", "Q", "K"]:
            value += 10
        elif rank == "A":
            value += 11
            aces += 1
        else:
            value += int(rank)

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value


def display_hand(name, hand, hide_first_card=False):
    """Display a player's hand and its value."""
    if hide_first_card:
        cards = ["Hidden card"] + [card_name(card) for card in hand[1:]]
        print(f"{name}: {', '.join(cards)}")
    else:
        cards = ", ".join(card_name(card) for card in hand)
        print(f"{name}: {cards} (value: {hand_value(hand)})")


def ask_hit_or_stand():
    """Ask the player whether to draw another card."""
    while True:
        choice = input("Hit or stand? (h/s): ").strip().lower()
        if choice in ["h", "s"]:
            return choice
        print("Please enter 'h' to hit or 's' to stand.")


def play_round():
    """Play one round of Blackjack."""
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("\n=== New Round ===")
    display_hand("Dealer", dealer_hand, hide_first_card=True)
    display_hand("You", player_hand)

    while hand_value(player_hand) < 21:
        if ask_hit_or_stand() == "s":
            break
        player_hand.append(deck.pop())
        display_hand("You", player_hand)

    player_value = hand_value(player_hand)
    if player_value > 21:
        print("You busted. Dealer wins!")
        return

    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    print("\nFinal hands:")
    display_hand("Dealer", dealer_hand)
    display_hand("You", player_hand)

    dealer_value = hand_value(dealer_hand)
    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("Push! It is a tie.")


def main():
    """Run the Blackjack menu."""
    print("=== Blackjack ===")

    while True:
        print("\nOptions:")
        print("1. Play a round")
        print("2. Exit")

        choice = input("\nEnter choice (1/2): ").strip()
        if choice == "1":
            play_round()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1 or 2.")


if __name__ == "__main__":
    main()