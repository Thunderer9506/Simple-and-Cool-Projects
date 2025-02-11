import turtle
import pandas

image = "india-map.gif"                                           #
screen = turtle.Screen()                                                            #
screen.title("India State Game")                                                    # create screen in the turtle        
screen.addshape(image)
screen.setup(700, 700)
turtle.shape(image)                                                                 #    

file = pandas.read_csv("indian_state.csv")                                  # read_csv
state = file["state"].tolist()                                                                #state in the file to list
x_y = list(zip(file.x, file.y))                                                               #x,y in the file to list

txt = turtle.Turtle()                                                                         #a new turtle as a text
gussed_state = []                                                                             #gussed_state

while len(gussed_state) <= 50:
    answer_state = screen.textinput(title = f"{len(gussed_state)}/30 Guess the State", prompt="Enter the States name? or enter 'exit' to exit").title()
    if answer_state == "Exit":
        left_state = [states for states in state if states not in gussed_state]
        new_data = pandas.DataFrame(left_state)
        new_data.to_csv("learn.csv")
        break
    if answer_state in state:                                                                       #in the while loop user will be asked to enter state every 
        gussed_state.append(answer_state)                                                           #time till the user entered "exit"
        index = state.index(answer_state)
        txt.hideturtle()
        txt.penup()
        txt.goto(x_y[index])
        txt.write(answer_state)