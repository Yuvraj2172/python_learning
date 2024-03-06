import random
def get_choices():
    player_choice = input("Enter player choice ? rock, paper, scissor")
    options = [
        "paper",
        "rock",
        "scissor"
    ]

    computer_choice = random.choice(options)
    choices = {
        "player": player_choice,
        "computer" : computer_choice
    }
    return choices

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissor":
            return "rock smashes scissor, You Win!"
        else:
            return "paper covers rock, You Lose!"
    elif  player == "paper":
        if computer == "rock":
            return "paper covers rock, You win!"
        else:
            return "scissor cuts paper, You Lose!"

    else:
        if computer == "paper":
            return "scissor cuts paper, You win!"
        else:
            return "rock smashes scissor, You lose!"
if __name__ == "__main__":

    print(check_win("rock", "paper"))


