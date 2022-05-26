import random

another = "yes"

while another == "yes" or "yeah" or "ye":
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    print("\ncomputer: ", computer)
    print("you: ", player, end = "\n\n")

    if computer == "rock" and player == "scissors" or computer == "paper" and player == "rock" or computer == "scissors" and player == "paper":
        print("you lose")
    elif computer == player:
        print("draw!")
    else:
        print("you win!")

    another = input("would you like to play again? (yes or no) :  ").lower()
print("BYE HAVE A GOOD DAY!!!")