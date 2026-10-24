from turtle import Turtle
class Snake:
    def __init__(self) :
        self.snakes = []
        self.position = [(-40,0),(-20,0),(0,0)]
        self.create_snake()
        self.head=self.snakes[-1]
    def create_snake(self):
        for i in range (len(self.position)): 
            new_turtle = Turtle("circle")
            new_turtle.color("yellow")
            new_turtle.penup()
            new_turtle.goto(self.position[i])
            self.snakes.append(new_turtle)
    def extend(self):
        new_segment = Turtle("circle")
        new_segment.color("yellow")
        
        new_segment.penup()
        new_segment.goto(self.snakes[0].pos())
        self.snakes.insert(0,new_segment)
    def move(self):
        for i in range(len(self.snakes)-1):
            self.snakes[i].goto(self.snakes[i+1].pos())
        self.head.forward(20)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        