import colorgram
import turtle
import random

colors = colorgram.extract("hirst_pain.jpg", 30)
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)
print(color_list)

turtle.colormode(255)
timm = turtle.Turtle()
timm.penup()
timm.hideturtle()
timm.speed("fastest")
timm.setheading(225)
timm.forward(300)
timm.setheading(0)
total_dots = 400
for dot_count in range(1, total_dots+1):
    timm.dot(10, random.choice(color_list))
    timm.forward(20)

    if dot_count % 20 == 0:
        timm.setheading(90)
        timm.forward(20)
        timm.setheading(180)
        timm.forward(400)
        timm.setheading(0)

src = turtle.Screen()
src.exitonclick()
