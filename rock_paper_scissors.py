import random

print("Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nEnter rock, paper, or scissors (or quit): ").lower().strip()

    if user == "quit":
        print("Thanks for playing!")
        break

    # Accept singular "scissor" too
    if user == "scissor":
        user = "scissors"

    if user not in choices:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue

    computer = random.choice(choices)
    print("Computer:", computer)

    if user == computer:
        print("It's a tie.")
    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
