import random


def cal_card(cards):
    if sum(cards) > 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def random_card():
    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(all_cards)
    return card


def compare_cards():
    pass


def game():
    user_cards = []
    comp_cards = []
    user_score = -1
    comp_score = -1
    is_over = False

    for _ in range(2):
        user_cards.append(random_card())
        comp_cards.append(random_card())

    while is_over:
        user_score = cal_card(user_cards)
        comp_score = cal_card(comp_cards)

        if user_score > 21 or user_score ==0 or comp_score==0:
            pass


game1 = input("Do you want to play Blackjack? type 'y' for playing the game and type 'n' for exit:")
while game1 == 'y':
    game()
    input(" if you want to continue type 'y' for exit 'n':")
