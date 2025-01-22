import random

def calculate_cards(cards):
    if sum(cards) > 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def choose():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif u_score == 0:
        return "win with blackjack"
    elif c_score == 0:
        return "lose ,opponent have black jack"
    elif u_score > 21:
        return "you went over,you lose"
    elif c_score > 21:
        return "opponent went over, you win"
    elif u_score < c_score:
        return "win"
    else:
        return "lose"


def game_1():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_over =   False

    for _ in range(2):
        user_cards.append(choose())
        computer_cards.append(choose())

    while not is_over:
        user_score = calculate_cards(user_cards)
        computer_score = calculate_cards(computer_cards)

        print(f"your cards {user_cards} and the total is {user_score}")
        print(f" computer first card is {computer_cards[0]}")

        if user_score > 21 or user_score == 0 or computer_score == 0:
            is_over = True
        else:
            type = input("type 'y' if you want to continue or 'n' for the pass.").lower()
            if type == 'y':
                user_cards.append(choose())
            else:
                is_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(choose())
        computer_score = calculate_cards(computer_cards)


    print(f"you final cards{user_cards}and final score{user_score}")
    print(f"computer final cards{computer_cards} and the final score{computer_score}")
    print(compare(user_score, computer_score))


game = input("do you want to play blackjack.'y' if you wanna to play or say 'n' for no:").lower()
while game == 'y':
    game_1()
    game = input("Do you want to play again? Type 'y' to play or 'n' to exit: ").lower()
