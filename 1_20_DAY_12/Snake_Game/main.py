#Udemy day20
import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
is_on = True
while is_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()

