#Udemy day21
import time
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
food = Food()
scoreboard = ScoreBoard()

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
scoreboard.start_scoreboard()

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_scoreboard()
        snake.extend()
        food.refresh()

    # collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

