#import getpass
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


def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Player 1 enter a choice ({choices_str}): "))
    action = Action(int(selection))
    return action


def get_user_selection2():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Player 2 enter a choice ({choices_str}): "))
    action = Action(int(selection))
    return action


def determine_winner(user_action1, user_action2, score1, score2):
    defeats = victories[user_action1]
    if user_action1 == user_action2:
        print(f"Both players selected {user_action1.name}. It's a tie!")
    elif user_action2 in defeats:
        print(f"{user_action1.name} beats {user_action2.name}! Player 1 wins with {user_action1.name}!")
        score1 += 1
    else:
        print(f"{user_action2.name} beats {user_action1.name}! Player 2 wins with {user_action1.name}!")
        score2 += 1

    return score1, score2


score1 = 0
score2 = 0

while True:
    try:
        user_action1 = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Please only select one number between the following{choices_str}")
        continue

    user_action2 = get_user_selection2()
    score1, score2 = determine_winner(user_action1, user_action2, score1, score2)

    print(f"Player 1 score: {score1}")
    print(f"Player 2 score: {score2}")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
