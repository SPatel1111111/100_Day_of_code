import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-250, 250)
        y_cor = random.randint(-250, 250)
        self.goto(x_cor, y_cor)
