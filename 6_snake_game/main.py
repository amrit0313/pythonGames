import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("naagin dance")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.xcor() > 300 or snake.head.ycor()> 300 or snake.head.xcor()< -300 or snake.head.ycor()< -300:
        game_is_on = False
        score.game_over()
        print(f"your score is {score.score}")

    if snake.head.distance(food) < 15:
        food.new_place()
        snake.extend()
        score.increase_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            score.game_over()
        print(f"your score is {score.score}")


screen.exitonclick()