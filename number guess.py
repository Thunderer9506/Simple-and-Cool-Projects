import random
import os

print("Welcome to number guessing game")

def play():
    number =  random.randrange(1,100)

    difficulty = input("Choose your difficulty level - 'Easy' or 'Hard' : ").lower()
    if difficulty == 'easy':
        print("You have 10 lives")
        difficulty = 10
    elif difficulty == 'hard':
        print("You have 5 lives")
        difficulty = 5
    else:
        print("Invalid")

    a = 0
    win = False
    while a < difficulty:
        while not win:
            user = int(input("Guess the number: "))
            if user == number:
                print("You have win")
                win = True
                difficulty = -1
            elif number > user:
                print("Too low")
                difficulty -= 1
                print(f"You have {difficulty} lives left")
            elif number < user:
                print("Too high")
                difficulty -= 1
                print(f"You have {difficulty} lives left")
            break

    if a == difficulty:
        print("You have lost")

play()

again = False
while not again:
    ask = input("Want to play again? 'Yes' or 'No' ").lower()
    if ask == "yes":
        again = False
        os.system('cls')
        play()
    else:
        again = True
