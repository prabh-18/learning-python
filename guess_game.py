import random

# --- Constants ---
# Maximum number of guesses the user gets per round
MAX_ATTEMPTS = 7
# Range for the secret number: 1 to 100 (inclusive)
LOW, HIGH = 1, 100


def play_round() -> bool:
    """
    Play one round of the guessing game.
    Returns True if the user won, False if they ran out of attempts.
    """
    # Computer picks a random integer between LOW and HIGH (inclusive)
    secret = random.randint(LOW, HIGH)
    # Track how many attempts the user has used
    attempts_used = 0

    print(f"\nI'm thinking of a number between {LOW} and {HIGH}. You have {MAX_ATTEMPTS} tries.")

    # Keep asking for guesses until user runs out of attempts
    while attempts_used < MAX_ATTEMPTS:
        guess_input = input("Your guess: ").strip()

        # Convert input to integer; handle invalid input (e.g. letters)
        try:
            guess = int(guess_input)
        except ValueError:
            print("Please enter a whole number.")
            continue  # Don't count this as an attempt

        # Make sure guess is in the valid range (1-100)
        if guess < LOW or guess > HIGH:
            print(f"Please enter a number between {LOW} and {HIGH}.")
            continue

        # This guess counts as one attempt
        attempts_used += 1

        if guess == secret:
            print(f"You win! You got it in {attempts_used} attempt(s).")
            return True
        elif guess > secret:
            print("Too high.")
        else:
            print("Too low.")

    # If we get here, user used all 7 attempts without guessing correctly
    print(f"Game over. The number was {secret}.")
    return False


def main() -> None:
    print("Welcome to the Number Guessing Game!")

    while True:
        play_round()

        # Ask if user wants to play again
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
