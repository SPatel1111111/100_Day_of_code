import random
is_on = True

list1 = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_card = []
comp_card = []
user_card.append(random.choice(list1))
comp_card.append(random.choice(list1))


def cards(card_random):
    random1 = random.choice(list1)
    card_random.append(random1)
    return card_random


user_sum = 0
comp_sum = 0
def sums():
    global comp_sum
    global user_sum
    user_sum=0
    comp_sum=0
    for i in user_card:
        user_sum += i
    for j in comp_card:
        comp_sum += j


def next1():
    global is_on
    if comp_sum < 17:
        cards(comp_card)
    if user_sum < 21:
        cards(user_card)
    else:
        if 11 in user_card:
            if 10 not in user_card and len(user_card) !=2:
                user_card.remove(11)
                user_card.append(1)
            # elif 10 in user_card and len(user_card) ==2:
            else:
                is_on = False
                print(f"user have blackjack.computer cards are {comp_card} ")
        else:
            is_on = False
            if user_sum == comp_sum :
                print("Game tie")
            elif user_sum < comp_sum and len(user_card) <len(comp_card):
                print("user win over computer")
            elif 11 and 10 in comp_card and comp_sum ==21 and len(comp_card)==2:
                print(f"computer have blackjack.computer cards are {comp_card} ")
            else:
                print(f"computer win over user.computer cards are {comp_card} ")

    # if user_sum >= 21:
    #     return f"user lose,{comp_sum}"


def printing():
    global x
    if len(user_card) ==1:
        for i in user_card:
            x = i
        print(f"user cards are {user_card} and sum of card {x}")
    else:
        print(f"user cards are {user_card} and sum of card {user_sum}")
    print(f"computer first card {comp_card[0]}")
    return

def repeat():
    print("if you want to continue.")
    while is_on:
        next1()
        if is_on:
            sums()
            printing()

print("BlACK-JACK GAME")
type = input("Do you want to play blackjack game??? if yes then type 'y' or not for 'n'. ").lower()
if type == 'y':
    printing()
    repeat()

    # is_on = True
    # while is_on:
    #     next1()
    #     sums()
    #     printing()
elif type == 'n':
    print("END")
else:
    print("enter valid input.")
