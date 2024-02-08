import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

user_cards = []
computer_cards = []

for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    computer_cards.append(deal_card())

def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score == computer_score:
        return "It's a draw!"
    elif user_score == 0:
        return "Blackjack! You win!"
    elif computer_score == 0:
        return "Computer has a blackjack. You lose."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

def blackjack_game():
    while True:
        # Clear the console for a new game
        os.system('cls' if os.name == 'nt' else 'clear')

        # Initial setup
        user_cards = [deal_card(), deal_card()]
        computer_cards = [deal_card(), deal_card()]
        game_over = False

        while not game_over:
            # Calculate scores
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)

            # Check for blackjack or if user's score is over 21
            if user_score == 0 or computer_score == 0 or user_score > 21:
                game_over = True
            else:
                # Ask the user if they want to draw another card
                user_input = input("Type 'y' to get another card, or 'n' to pass: ").lower()
                if user_input == 'y':
                    user_cards.append(deal_card())
                else:
                    game_over = True

        # Let the computer play
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        # Show the final hands and scores
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

        # Compare scores and determine the winner
        result_message = compare(user_score, computer_score)
        print(result_message)

        # Ask the user if they want to restart the game
        restart = input("Do you want to play again? Type 'y' for yes, 'n' for no: ").lower()
        if restart != 'y':
            print("Goodbye!")
            break

# Start the game
blackjack_game()
