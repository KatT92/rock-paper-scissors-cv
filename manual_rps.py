import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def get_user_choice():
    print("type either rock, paper or scissors")
    rps_array = ['rock', 'paper', 'scissors']
    userInput = input()
    while userInput.lower() not in rps_array:
        print("type either rock, paper or scissors")
        userInput = input()
    return userInput.lower()


def get_winner(computer_choice, user_choice):
    rps = ["rock", "paper", "scissors"]
    cIndex = rps.index(computer_choice)
    uIndex = rps.index(user_choice)

    print(f"you chose {user_choice}, computer chose {computer_choice}")

    # maybe a way to cut down on code using index - 1?
    if cIndex == uIndex:
        print("draw")
    elif cIndex == uIndex + 1 or cIndex == uIndex - 2:
        print("lose")
    elif cIndex == uIndex - 1 or cIndex == uIndex + 2:
        print("win")
    else:
        print("something went wrong")


def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)


play()
