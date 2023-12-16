import random

user_action = input("enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nyou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"both players selected{user_action}. it's a tie! ")
elif user_action == "rock":
    if computer_action == "scissors" :
        print("rock smashes scissors. you win")
    else:
        print("paper covers rock. you lose")
elif user_action == "paper" :
    if computer_action == "rock" :
        print("paper covers rock. you win! ")
    else: 
        print("scissors cut paper! you lose. ")
elif user_action == "scissors" :
    if computer_action == "paper" :
        print("scissors cuts paper! you win")
    else:
        print("rock smashes scissors! you lose. ")

