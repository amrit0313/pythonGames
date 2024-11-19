from turtle import Turtle, Screen
FONT = ('courier', 20, 'normal')
ALIGNMENT = "CENTER"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score = {self.score}", align= ALIGNMENT ,move=False,  font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("game over", align= ALIGNMENT ,move=False,  font=FONT)

