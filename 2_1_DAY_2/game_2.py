import random
print(" ROCK PAPER SCISSORS")
user = int(input("enter the rock 0 ,paper 1 and scissor 2:"))

computer = random.randint(0,2)
print(f"computer input:{computer}")
if computer == user:
    print("draw")
elif computer == 0 and user == 2:
    print("you lose")
elif computer == 2 and user == 0:
    print("you win")
elif user >= 3:
    print(" invalid number34")
elif computer > user:
    print("you lose")
else:
    print("you win")