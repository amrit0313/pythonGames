from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()


screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)
decision = int(screen.textinput(title="Winning score" ,prompt="Enter the score, that decides the winner"))

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")

screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce()
    if ball.distance(paddle_1) < 50 and ball.xcor()>320 or ball.distance(paddle_2)<50  and ball.xcor()<-320 :
        ball.paddle_bounce()
    if ball.xcor()>380:
        ball.reset_position()
        score.l_scored()

    if ball.xcor()<-380:
        ball.reset_position()
        score.r_scored()

    if score.r_score == decision:
        game_is_on = False
        print("right one wins")
        ball.write("Game over, right one wins", align="center", font=('courier', 20, 'normal'))
    if score.l_score ==decision:
        game_is_on = False
        ball.write("Game over, left one wins", align="center", font=('courier', 20, 'normal'))

        print("left one work")



screen.exitonclick()