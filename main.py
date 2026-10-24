import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("welcome to the snake game")
screen.tracer(0)

sam = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(sam.up, "Up")
screen.onkey(sam.down, "Down")
screen.onkey(sam.right, "Right")
screen.onkey(sam.left, "Left")

game_on = True
while game_on:
    sam.move()
    screen.update()
    time.sleep(0.1)

    if sam.head.distance(food) < 15:
        food.appear()
        sam.extend()
        score.increase_score()

    if sam.head.xcor() > 280 or sam.head.xcor() < -280 or sam.head.ycor() > 280 or sam.head.ycor() < -280:
        game_on = False
        score.game_over()

    for segment in sam.snakes[:-1]:
        if sam.head.distance(segment) < 10:
            game_on = False
            score.game_over()
            break

screen.exitonclick()
