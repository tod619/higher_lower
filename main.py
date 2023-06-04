# Higher lower game
# 02/06/2023
from art import logo, vs
from game_data import data
import random


def format_data(account):
    """ takes the account data and returns it in a usuable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """ Take the user guess and the account followers and return wether the user were correct """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True

while game_should_continue:
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers 'A' or 'B'?: ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right!! Current Score: {score}")
    else:
        game_should_continue = False
        print(f"You got it wrong! Final Scoe: {score}")
