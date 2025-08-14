from random import randint
from art import logo

def check_answer(your_guess,answer):
    if your_guess > answer:
        print("Too high.")
        return False
    elif your_guess < answer:
        print("Too low.")
        return False
    else:
        print(f"You got it! The answer was {answer}")
        return True

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5


def game():
    print(logo)
    answer = randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    turns = set_difficulty()
    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        your_guess = int(input("Make a guess: "))
        turns -= 1
        if check_answer(your_guess, answer):
            return
        elif turns == 0:
            print("You've run out of guesses, you lose.")
            return
        else:
            print("Guess again.")

game()