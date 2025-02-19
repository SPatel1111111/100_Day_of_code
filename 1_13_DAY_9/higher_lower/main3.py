from game_data import data
import random

def profile(data1):

    name=data1['name']
    description= data1['description']
    country = data1['country']
    return f"{name} a {description}, from {country}"

def check_answer(guess,a_foll,b_foll):
    if a_foll > b_foll:
        return guess =="a"
    else:
        return guess =="b"

account_b = random.choice(data)

score = 0
game_continue = True
while game_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b =random.choice(data)

    print(f"compare A:{profile(account_a)}")
    print("VS")
    print(f"Against B:{profile(account_b)}")

    guess1=input("GUESS, WHO CAN HAVE MORE FOLLOWERS? A OR B:").lower()

    a_follower=account_a['follower_count']
    b_follower=account_b['follower_count']
    is_correct =check_answer(guess1,a_follower,b_follower)

    if is_correct:
        score+=1
        print(f"you are correct. your current score {score}.")
        print(".............")
    else:
        print(f"you are wrong. your last score {score}.")
        game_continue =False


