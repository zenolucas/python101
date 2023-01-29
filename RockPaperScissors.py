import random


def get_choices():
    gameChoices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(gameChoices)
    player_choice = input("Enter a choice (rock, paper, scissors)\n")

    choices = {"player": player_choice, "computer": computer_choice}

    return choices


theChoices = get_choices()
player = theChoices["player"]
computer = theChoices["computer"]


def play(player, computer):
    print(f"player chose {player}, while computer chose {computer}")

    if player == computer:
        return "TIE"
    else:
        if player == "rock":
            if computer == "scissors":
                return "player wins"
            elif computer == "paper":
                return "computer wins"
        elif player == "paper":
            if computer == "rock":
                return "player wins"
            elif computer == "scissors":
                return "computer wins"
        elif player == "scissors":
            if computer == "paper":
                return "player wins"
            elif computer == "rock":
                return "computer wins"


print(play(player, computer))
