from turtle import Turtle,Screen
turtle =Turtle()
screen =Screen()
screen.onclick(turtle.goto) # Subsequently clicking into the TurtleScreen will
                            # make the turtle move to the clicked point.
# screen.onclick()
#
# screen.exitonclick()

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
