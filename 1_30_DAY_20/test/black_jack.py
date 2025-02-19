import random

def cal_cards(cards):
    if sum(cards) >= 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) >= 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def random_card():
    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(all_cards)
    return card

def compare(u_score, c_score):
    if u_score == c_score:
        print("draw.")
    elif u_score == 0:
        print("have Blackjack")
    elif c_score == 0:
        print("lose ! opponent have blackjack. ")
    elif u_score > c_score:
        print("you win")
    else:
        print(" you lose!")
    return

def game():
    user_card = []
    comp_card = []
    user_score = -1
    comp_score = -1
    is_on = True

    for _ in range(2):
        user_card.append(random_card())
        comp_card.append(random_card())

    while is_on:
        user_score = cal_cards(user_card)
        comp_score = cal_cards(comp_card)

        print(f"your cards {user_card} and your score {user_score}.")
        print(f"computer first card {comp_card[0]}.")

        if user_score >= 21 or user_score == 0 or comp_score == 0:
            is_on = False
        else:
            type = input("do you want to continue type 'y' or 'n' for no.").lower()
            if type == 'y':
                user_card.append(random_card())
            else:
                is_on = False

    while comp_score != 0 and comp_score < 17:
        comp_card.append(random_card())
        comp_score = cal_cards(comp_card)

    print(f"the final user cards are {user_card} and score {user_score}.")
    print(f"final computer card are {comp_card} and score {comp_score}.")
    print(compare(user_score, comp_score))


game1 = input("Do you want to play blackjack game?? type 'y' if you want to play or type 'n' for exit.").lower()
while game1 == 'y':
    game()
    game1 = input("do you want play again so type 'y' or type 'n' for exit:").lower()
