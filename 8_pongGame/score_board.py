from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(300, 260)
        self.write(self.r_score, align="right", font=('courier', 20, 'normal'))
        self.goto(-300, 260)
        self.write(self.r_score, align="left",font=('courier', 20, 'normal') )

    def update_score(self):
        self.clear()
        self.goto(300, 260)
        self.write(self.r_score, align="right", font=('courier', 20, 'normal'))
        self.goto(-300, 260)
        self.write(self.l_score, align="left",font=('courier', 20, 'normal') )

    def r_scored(self):
        self.r_score +=1
        self.update_score()


    def l_scored(self):
        self.l_score +=1
        self.update_score()
