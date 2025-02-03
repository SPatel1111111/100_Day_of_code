from turtle import Turtle, Screen

STARING_POSITION=(0,-280)
MOVING_DISTANCE =10
Y_FINISHING_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto_starting()

    def go_up(self):
        self.forward(MOVING_DISTANCE)

    def goto_starting(self):
        self.goto(STARING_POSITION)

    def is_finishing_line(self):
        if self.ycor() > Y_FINISHING_LINE:
            return True
        else:
            return False


