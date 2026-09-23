import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
def new_func():
    screen = turtle.Screen ()
    return screen

screen = new_func()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("welcome to the snake game")
screen.tracer(0)

sam = Snake()
food = Food()
score = Scoreboard()
game_on = True
while game_on:
    sam.move()
    screen.update()
    time.sleep(0.1)
    screen.listen()
    screen.onkey(sam.up,"Up")
    screen.onkey(sam.down,"Down")
    screen.onkey(sam.right,"Right")
    screen.onkey(sam.left,"Left")
    if sam.head.distance(food) < 15:
       food.appear()
       sam.extend()
       score.intcrease_score()
    if sam.head.xcor() > 280 or sam.head.xcor() < -280 or sam.head.ycor() > 280 or sam.head.ycor() < -280 :
        game_on = False
        score.game_over()
    for segment in sam.snakes[:-1]:
        if sam.head.distance(food)< 10:
            game_on = False
            score.game_over()


screen.exitonclick() 