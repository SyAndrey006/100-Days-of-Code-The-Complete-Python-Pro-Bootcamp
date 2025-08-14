from art import logo, vs
from game_data import data
import random

def compare_people(first_account, second_account):
    if first_account["follower_count"] > second_account["follower_count"]:
        return "a"
    else:
        return "b"

def account_info(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def game():
    score = 0
    continue_game = True
    second_account = random.choice(data)
    while continue_game:
        first_account = second_account
        second_account = random.choice(data)
        while first_account == second_account:
            first_account = random.choice(data)
        print(f"Compare A: {account_info(first_account)}.")
        print(vs)
        print(f"Against B: {account_info(second_account)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        print("\n" * 20)

        if guess == compare_people(first_account, second_account):
            print(logo)
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            continue_game = False

print(logo)
game()