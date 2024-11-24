import turtle
import pandas

from fontTools.afmLib import readlines
from uaclient.data_types import data_list

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_coordinates(x, y):
#     print(x, y)
# screen.onscreenclick(get_coordinates)  #these are  for getting coordinates


data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []
while len(guessed_states) <50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 guessed ", prompt="Guess the state ").title()
    if answer == "Exit":
        missing_states = []
        for state in states:
            if state not  in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states to learn.csv")
        break
    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(state_data.state.item())

