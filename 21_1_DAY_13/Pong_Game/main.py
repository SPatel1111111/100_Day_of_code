from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


# def r_paddle_move(x, y):
#     # r_paddle.goto(r_paddle.xcor(), y)
#     if y > r_paddle.ycor():
#         r_paddle.go_up()
#     else:
#         r_paddle.go_down()
#
#
# def l_paddle_move(x, y):
#     # l_paddle.goto(l_paddle.xcor(), y)
#     if y > l_paddle.ycor():
#         l_paddle.go_up()
#     else:
#         l_paddle.go_down()


# screen.listen()
# screen.onclick(l_paddle_move, btn=1)
# screen.onclick(r_paddle_move, btn=3)

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_time)
    screen.update()
    ball.move()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_move()

    # left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_move()

screen.exitonclick()
