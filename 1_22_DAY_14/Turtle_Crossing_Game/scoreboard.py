from turtle import Turtle,Screen
FONT =("Times roman",25,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.hideturtle()
        self.goto(-280,250)
        self.color("black")
        self.update_score()
        self.penup()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}",align="left",font=FONT)

    def increase_score(self):
        self.score +=1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)