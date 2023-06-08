from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

screen.colormode(255)
timmy.speed("fastest")

def spiro(gap):
    for i in range(int(360/gap)):
        timmy.pencolor(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.seth(current_heading + gap)

spiro(int(input("Enter the gaps: ")))

screen.exitonclick()