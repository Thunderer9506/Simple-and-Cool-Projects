from turtle import Turtle, Screen
import random
timmy = Turtle()
screen = Screen()
direction = [0,90,180,270]
screen.colormode(255)
timmy.pensize(10)
timmy.speed("fastest")

for i in range(100):
    timmy.setheading(random.choice(direction))
    timmy.forward(20)
    timmy.pencolor(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

screen = Screen()
screen.exitonclick()