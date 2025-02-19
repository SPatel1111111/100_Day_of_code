#Udemy day19
import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "deep pink", "dim gray", "sienna"]
user_bet = screen.textinput(title="Make your Bet",
                            prompt="What do you think about which color of turtle win the race ?? Enter the number (1-10):")

y_position = [-140, -110, -80, -50, -20, 20, 50, 80, 110, 140]
all_turtle = []
def my():
    for turtle_count in range(0, 10):
        tim = Turtle(shape="turtle")
        tim.penup()
        tim.color(colors[turtle_count])
        tim.goto(x=-240, y=y_position[turtle_count])
        all_turtle.append(tim)

global is_race_on
# is_race_on =False
# if user_bet and user_bet in colors:
if 0 < int(user_bet) <= 10:
    is_race_on = True
else:
    print("invalid user input.enter valid number.")
    is_race_on = False


while is_race_on:
    my()
    for tur in range(len(all_turtle)):
        # 250 - (40/2) =230
        if all_turtle[tur].xcor() > 230:
            is_race_on = False
            winning_turtle = tur + 1
            if winning_turtle == user_bet:
                print(f"you win!!, winning turtle  number{winning_turtle} and color of the turtle is {colors[winning_turtle-1]}.")
            else:
                print(f"you lost!!, winning turtle  number  {winning_turtle} and color of turtle is  {colors[winning_turtle-1]}.")

        rand_distance = random.randint(0, 10)
        all_turtle[tur].forward(rand_distance)

screen.exitonclick()
