from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_decision = random.randint(1, 6)
        if random_decision == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(x=270,y=random_y)
            self.all_cars.append(car)


    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

