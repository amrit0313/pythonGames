from turtle import Turtle, Screen
import random

game_is_on = False
screen = Screen()
screen.setup(width = 600, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race?choose a color: ")
color = ['red', 'blue', 'yellow', "green", 'violet', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.hideturtle()
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=y_position[turtle_index])
    new_turtle.showturtle()
    all_turtles.append(new_turtle)


if user_bet:
    game_is_on= True

while game_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            game_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won the bet")
            else:
                print(f'you got wrong, {winning_color} won')    
            
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()