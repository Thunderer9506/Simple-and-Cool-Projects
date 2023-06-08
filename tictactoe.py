print('''Welcome to Python Tic Tac Toe game''')

rows = [['_','_','_'],
        ['_','_','_'],                                #structure of the game
        ['_','_','_'],]

def condition():                                                                    #function to check condition who win the game
    if rows[0][0] == 'O' and rows[1][0] == 'O' and rows[2][0] == 'O':
        return True
    elif rows[0][1] == 'O' and rows[1][1] == 'O' and rows[2][1] == 'O':
        return True
    elif rows[0][2] == 'O' and rows[1][2] == 'O' and rows[2][2] == 'O':
        return True
    elif rows[0][0] == 'O' and rows[0][1] == 'O' and rows[0][2] == 'O':
        return True
    elif rows[1][0] == 'O' and rows[1][1] == 'O' and rows[1][2] == 'O':
        return True
    elif rows[2][0] == 'O' and rows[2][1] == 'O' and rows[2][2] == 'O':
        return True 
    elif rows[0][0] == 'O' and rows[1][1] == 'O' and rows[2][2] == 'O':            
        return True
    elif rows[0][2] == 'O' and rows[1][1] == 'O' and rows[2][0] == 'O':
        return True
    elif rows[0][0] == 'X' and rows[1][0] == 'X' and rows[2][0] == 'X':
        return True
    elif rows[0][1] == 'X' and rows[1][1] == 'X' and rows[2][1] == 'X':
        return True
    elif rows[0][2] == 'X' and rows[1][2] == 'X' and rows[2][2] == 'X':
        return True
    elif rows[0][0] == 'X' and rows[0][1] == 'X' and rows[0][2] == 'X':
        return True
    elif rows[1][0] == 'X' and rows[1][1] == 'X' and rows[1][2] == 'X':
        return True
    elif rows[2][0] == 'X' and rows[2][1] == 'X' and rows[2][2] == 'X':
        return True
    elif rows[0][0] == 'X' and rows[1][1] == 'X' and rows[2][2] == 'X':
        return True
    elif rows[0][2] == 'X' and rows[1][1] == 'X' and rows[2][0] == 'X':
        return True
    elif i == 9:
        return True

end = False
i = 0

for items in rows:                                    #will print structure for the initially
    print(items)

player = str(input("What do you wanna choose? 'O' or 'X': ").upper())      #ask the player what he want to choose initially

while not end:
    yaxis = int(input("Choose y-axis between 0-2: "))                            #will ask for the axis to the user every time
    xaxis = int(input("Choose x-axis between 0-2: "))
    for items in rows:
        rows[yaxis][xaxis] = player                         #will show how the structure will look
        print(items)

    if condition() == True:
        print(player + " Win the game")                      #check if the game is over or not
        end = True
        break

    if player == 'X':
        player = 'O'
        print(f"Player {player} turn \n")
    elif player == 'O':
        player = 'X'                                   #switch between 'o' and 'x' player
        print(f"Player {player} turn \n")
    else:
        print(f"Player {player} turn \n")

    i += 1