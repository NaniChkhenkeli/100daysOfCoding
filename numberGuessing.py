import random

def choose_difficulty():
    """Choose the difficulty level and return the maximum number of turns."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5
    else:
        print("Invalid input. Defaulting to easy difficulty.")
        return 10

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    answer = random.randint(1, 100)

    # Choose the difficulty level
    max_turns = choose_difficulty()

    # Initialize the number of turns
    turns = max_turns

    while turns > 0:
        # Get user's guess
        guess = int(input("Make a guess: "))

        # Check user's guess
        if guess == answer:
            print(f"Congratulations! You guessed the correct number, which was {answer}.")
            break
        elif guess > answer:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")

        # Decrement the number of turns
        turns -= 1
        print(f"You have {turns} {'turns' if turns != 1 else 'turn'} left.")

    if turns == 0:
        print(f"Sorry, you've run out of turns. The correct number was {answer}.")

# Start the game
play_game()
