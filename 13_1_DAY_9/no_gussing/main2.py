import random
HARD_GUESS =5
EASY_GUESS =10

# checke guesses
def check_guess(user_guess, actual_answer):
    if user_guess < actual_answer:
        print("to low.")
    elif user_guess >actual_answer:
        print("too high.")
    else:
        print("you got it!!")
# difficulty
def diff():
    type= input("choose dificulty. type 'easy' or 'hard':").lower()
    if type =='easy':
        return EASY_GUESS
    elif type =='hard':
        return HARD_GUESS
    else:
        return "TYPE AGAIN"

def game():
    print("number to the the guessing game.")
    print("guessing number between 1 to 100")
    answer =random.randint(1,100)
    print(answer)

    #GUESS
    turns =diff()

    print(f"you have {turns} attempts remaining.")
    for i in range(turns):
        predicted = int(input("Make guess:"))
        check_guess(predicted, answer)
        if predicted == answer:
            print(f"you got it. the answer is{answer}.")
            return
        print('guess again')
    print(f"you run out of guesses. start again.")


    yep=input("if you want play again type 'y' or for exit type 'n':").lower()
    while yep == 'y':
        game()

game()






