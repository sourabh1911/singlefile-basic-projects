import random

def guessing_game():
    number = random.randint(1, 100)
    attempts = 0

    print("🎮 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("📈 Too low! Try a bigger number.")

        elif guess > number:
            print("📉 Too high! Try a smaller number.")

        else:
            print("🎉 Congratulations!")
            print("You guessed the number:", number)
            print("Number of attempts:", attempts)
            break


guessing_game()