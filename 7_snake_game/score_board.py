from turtle import Turtle

from certifi import contents

FONT = ('courier', 20, 'normal')
ALIGNMENT = "CENTER"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("high_score.txt") as f:
            self.high_score = int(f.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score = {self.score} High Score: {self.high_score}" , align= ALIGNMENT ,move=False,  font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
            if self.score>self.high_score:
                self.high_score = self.score
            with (open("high_score.txt",mode="w") as f):
                f.write(f"{self.high_score}")
            self.score = 0
            self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("game over", align= ALIGNMENT ,move=False,  font=FONT)

