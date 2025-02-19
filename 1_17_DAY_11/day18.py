import turtle
from turtle import Turtle
import random

# 1
tim = Turtle()
tim.shape("turtle")


# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# import heroes
# print(heroes.gen())
# print(heroes.genarr(3))
# 2
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# 3

# colours =["spring green","salmon","purple","light blue","crimson","black","dark slate blue"]
# def move(number_side):
#     angle =360/number_side
#     for _ in range(number_side):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape in range(3,11):
#     tim.color(random.choice(colours))
#     move(shape)

# 4
# turtle.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color1 = (r, g, b)
#     return random_color1
#
#
# direction = [0, 90,180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(20)
#     tim.setheading(random.choice(direction))

# #5
# turtle.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color1 = (r, g, b)
#     return random_color1
#
# tim.speed("fastest")
#
# for _ in range(100):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(tim.heading()+10)