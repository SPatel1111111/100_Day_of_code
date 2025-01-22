from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Times New Roman", 25, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Times New Roman", 25, "normal"))

    def l_move(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_move(self):
        self.r_score += 1
        self.update_scoreboard()
