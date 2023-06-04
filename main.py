# Higher lower game
# 02/06/2023
from art import logo
from game_data import data
import random


def format_data(account):
    """ Format the account data into a usuable form"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    print(f"{account_name}, a {account_descr}, from {account_country}")


print(logo)

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)


format_data(account_a)
format_data(account_b)
