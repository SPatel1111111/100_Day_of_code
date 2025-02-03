from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.higher_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        # self.start_scoreboard()

    def start_scoreboard(self):
        self.clear()
        self.read_file()
        self.write(f"Score: {self.score} Higher_Score:{self.higher_score}", align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.start_scoreboard()

    def reset(self):
        if self.score > self.higher_score:
            self.higher_score = self.score
            self.write_file()
        self.score = 0
        self.start_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)
    def read_file(self):
        with open("data.txt") as data:
            self.higher_score =int(data.read())

    def write_file(self):
        with open("data.txt",mode="w") as data:
            data.write(f"{self.higher_score}")
