from turtle import Turtle,Screen
import random

race = False
screen = Screen()
screen.setup(width=500, height=500)
user = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ['red','orange','yellow','green','blue','purple']
tur = []

y_pos = [-70,-40,-10,20,50,80]
for turt in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turt])
    tim.goto(x=-230,y=y_pos[turt])
    tur.append(tim)

if user:
    race = True

while race:
    for turtle in tur: 
        if turtle.xcor()>230:
            race = False
            winning_color = turtle.pencolor()
            if winning_color == user:
                print(f"you've won! the {winning_color} turtle is the winner!")
            else:
                print(f"you've lost! the {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()