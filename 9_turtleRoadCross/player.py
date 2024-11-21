from turtle import Turtle

from six import moves

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
MOVE_INCREMENT = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.goto(0, -280)
        self.car_speed = MOVE_DISTANCE

    def go_up(self):
        self.forward(self.car_speed)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor()>270:
            return True
        else:
            return False
    def level_up(self):
        self.car_speed += MOVE_INCREMENT