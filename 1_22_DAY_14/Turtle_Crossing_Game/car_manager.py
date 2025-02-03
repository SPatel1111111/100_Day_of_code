from turtle import Turtle, Screen
import random

COLORS = ["red", "green", "blue", "violet", "indigo", "orange", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()
        self.moving_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.moving_speed)

    def level_up(self):
        self.moving_speed += MOVE_INCREMENT