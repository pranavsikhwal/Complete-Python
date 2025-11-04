import random
from game_data import data
score = 0
#defining a function contains the information of random account which we have to show on screen
def account_info(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name} ,a { account_description}, from { account_country}"
#select two random accounts
should_game_continue = True
account_2 =random.choice(data)
while should_game_continue:
    account_1 = account_2
    account_2 = random.choice(data)
    if account_1 == account_2:
        account_2 = random.choice(data)

    print(f"Compare A : {account_info(account_1)}")
    print("vs")
    print(f"Compare B : {account_info(account_2)}")

    #ask user for guess
    guess  = input("Who has more followers ? A or B \n").lower()
    #check the user for correct
    if account_1["follower_count"]>account_2["follower_count"]:
        follower = "a"
    else:
        follower = "b"

    if guess == follower:
        score += 1
        print(f"You are right . your score is {score}")
    else:
        print(f"You are wrong . Final score is {score}")
        should_game_continue = False