# Introduction
import random


def get_choice():
    player_choice = input("Enter a choice : (rock, paper, scissors)")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    random_choices = {"player": player_choice, "computer": computer_choice}
    return random_choices


def greeting():
    return "Hi"


bio = {"name": "Madusanka", "age": 26, "school": "Ananda College"}


def check_win(player, computer):
    print(f'You chose {player}')
    print(f'computer chose {computer}')
    if player == computer:
        return "It's a tie"
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissors! you win!"
    elif player == "rock" and computer == "paper":
        return "Paper covers rock! you lose!"
    else:
        return [player, computer]


choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)
# print(choices)
# print(bio)
# b_name = bio["name"]
# b_school = bio["school"]
# print(b_name+" "+b_school)
# print(result)


