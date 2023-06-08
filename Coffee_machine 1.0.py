MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 120,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 250,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
def report():
    for items in resources:
        print(f"{items} : {resources[items]}")

def resources_sufficient(user_demand):
    global sufficient
    sufficient = True
    for items in resources:
        if resources[items] > MENU[user_demand]["ingredients"][items]:
            sufficient = True
        else:
            sufficient = False
            print(f"Sorry, Did'nt have much {items}")
        if sufficient == True:
            break
user_demand = input("What would you like? (espresso/latte/cappuccino): ").lower()
def result():
    resources["water"] -= MENU[user_demand]["ingredients"]["water"]
    resources["milk"] -= MENU[user_demand]["ingredients"]["milk"]
    resources["coffee"] -= MENU[user_demand]["ingredients"]["coffee"]
    resources["money"] += MENU[user_demand]["cost"]
    report()

def machine():
    seen = False
    while not seen:
        if user_demand == "report":
            report()
            seen = False
        else:
            seen = True
    resources_sufficient(user_demand)
    transaction = False

    if sufficient == True:
        money = int(input(f"\nInsert ₹{MENU[user_demand]['cost']} to the vending machine: "))
        if money < MENU[user_demand]["cost"]:
            print(f"\nSorry that's not enough money. Money refunded.")
        elif money == MENU[user_demand]["cost"]:
            transaction = True
        elif money > MENU[user_demand]["cost"]:
            refund = money - MENU[user_demand]["cost"]
            print(f"\nHere is ₹{refund} dollars in change.")
            transaction = True

    if transaction == True:
        print(f"\nResources before buying the {user_demand}")
        report()
        print(f"\nResources after buying the {user_demand}")
        result()

    print(f"\n\nHere is your {user_demand}. Enjoy!")

if user_demand !="off":
    machine()
