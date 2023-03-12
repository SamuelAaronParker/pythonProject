import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


victories = {
    Action.Scissors: [Action.Paper],
    Action.Paper: [Action.Rock],
    Action.Rock: [Action.Scissors]
}


def get_user_selection(player):
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = input(f"{player} enter a choice ({choices_str}): ")
    try:
        action = Action(int(selection))
    except ValueError:
        print("Invalid selection. Please try again.")
        return get_user_selection(player)
    return action

def get_user_selection_2p(player):
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = input(f"{player} enter a choice ({choices_str}): ")
    try:
        action = Action(int(selection))
    except ValueError:
        print("Invalid selection. Please try again.")
        return get_user_selection_2p(player)
    return action

def get_computer_selection():
    return random.choice(list(Action))


def determine_winner(user_action, computer_action, player):
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
        return "tie"
    elif computer_action in victories[user_action]:
        print(f"{user_action.name} beats {computer_action.name}! {player} wins!")
        return player
    else:
        print(f"{computer_action.name} beats {user_action.name}! Computer wins!")
        return "computer"

def determine_winner_player(user_action, user_action2, player1, player2):
    if user_action == user_action2:
        print(f"Both players selected {user_action.name}. It's a tie!")
        return "tie"
    elif user_action2 in victories[user_action]:
        print(f"{user_action.name} beats {user_action2.name}! {player1} wins!")
        return player1
    else:
        print(f"{user_action2.name} beats {user_action.name}! {player2} wins!")
        return player2


print("""
************************************************************
*        Welcome to the Rock, Paper, Scissors Game!        *
************************************************************
""")
while True:
    mode = input("Select a mode (1 for two-player, 2 for against computer): ")
    if mode == "1":
        player1 = input("Enter player 1 name: ")
        player2 = input("Enter player 2 name: ")
        score1 = 0
        score2 = 0
        while True:
            user_action1 = get_user_selection_2p(player1)
            user_action2 = get_user_selection_2p(player2)
            result = determine_winner_player(user_action1, user_action2, player1, player2)
            if result == player1:
                score1 += 1
            elif result == player2:
                score2 += 1

            print(f"{player1} score: {score1}")
            print(f"{player2} score: {score2}")

            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                play_again = input("Do you want to exit? (y/n): ")

                if play_again.lower() != "n":
                    exit("Thanks for playing! Goodbye")
                else:
                    break

    elif mode == "2":
        player = input("Enter player name: ")
        score = 0
        compscore = 0
        while True:
            user_action = get_user_selection(player)
            computer_action = get_computer_selection()
            result = determine_winner(user_action, computer_action, player)
            if result == player:
                score += 1
            elif result == "computer":
                compscore += 1

            print(f"{player} score: {score}\nComputer score: {compscore}")

            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                play_again = input("Do you want to exit? (y/n): ")

                if play_again.lower() != "n":
                    exit("""************************************************************
*                Thanks for playing! Goodbye!              *
************************************************************""")
                else:
                    break

    else:
        print("Invalid mode. Please try again.")
