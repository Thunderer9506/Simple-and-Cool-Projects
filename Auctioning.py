import os

anyone_else = False
Bid = {}

while not anyone_else:
    name = str(input("Whats your name? "))
    money = int(input("Whats your bid? $"))
    anyone_else = input("Is there any one else? ").lower()
    Bid[name] = money
    if anyone_else == "yes":
        anyone_else = False
        os.system('cls')
    elif anyone_else == "no":
        print(Bid)
        anyone_else = True
    
os.system('cls')
biggest = max(Bid.values())

key_list=list(Bid.keys())
val_list=list(Bid.values())
ind=val_list.index(biggest)
winner = key_list[ind]

print(f"The winner is {winner}, with the bid of ${biggest}")
