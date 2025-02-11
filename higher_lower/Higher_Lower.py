from data_of_HigherLower import data
import random
import os
 
print("Welcome to Higher Lower game")
def choose():
    A =random.choice(data)
    return A

A = choose()
print(f"A = {A['name']} a {A['description']} from {A['country']}")
print("vs")
B = choose()
print(f"B = {B['name']} a {B['description']} from {B['country']}")

wins = 0
out = False
while not out:
    ask = input("Who's followers are more? 'A' or 'B': ").lower()
    if ask == 'a' and A['follower_count'] > B['follower_count']:
        result = True
    elif ask == 'b' and B['follower_count'] > A['follower_count']:
        result = True
    else:
        result = False

    if result == True:
        os.system('cls')
        wins += 1
        A = B
        print(f"A = {A['name']} a {A['description']} from {A['country']}")
        print("vs")
        B = choose()
        print(f"B = {B['name']} a {B['description']} from {B['country']}")
        out = False
    elif result == False:
        out = True
        if wins <= 5 and wins >= 0:
            print(f"Your score was {wins}, Better luck next time")
        elif wins > 5 and wins <=10:
            print(f"Your score was {wins}, Not Bad")
        elif wins > 10:
            print(f"Your score was {wins}, OOPS! You were having a great strik but ...")