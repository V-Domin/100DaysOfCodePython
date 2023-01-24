MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {

            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#come up with the system to count resources

profit = 0
water = 300
milk = 200
coffee = 100


while True:

    start = input("What would you like? (espresso/latte/cappuccino):")

    #ESPRESSO
    if start == "espresso":
        if water > 50 and coffee > 18:
            cost = 1.5
            print(f"Price: ${cost} \nPlease insert coins.")

            try:
                quarters = int(input("How many quarters? ")) * 0.25
                dimes = int(input("How many dimes? ")) * 0.10
                nickles = int(input("How many nickles? ")) * 0.05
                pennies = int(input("How many pennies? ")) * 0.01
            except:
                print("That is not money. Give me your money if you want some coffee!")
                continue

            total = quarters + dimes + nickles + pennies
            change = total - cost
            if total < cost:
                print(f"Sorry that's not enough money. Money refunded: ${total}")
            elif total >= cost:
                    #count resources
                    water = water - 50
                    coffee = coffee - 18
                    profit = profit + 1.5
                    print(f"Here is ${round(change, 2)} in change. \nHere is your espresso! Enjoy!")
        else:
            print("Not enough resources")


    # LATTE
    elif start == "latte":
        if water > 50 and coffee > 18 and milk > 150:
            cost = 2.5
            print(f"Price: ${cost} \nPlease insert coins.")

            try:
                quarters = int(input("How many quarters? ")) * 0.25
                dimes = int(input("How many dimes? ")) * 0.10
                nickles = int(input("How many nickles? ")) * 0.05
                pennies = int(input("How many pennies? ")) * 0.01
            except:
                print("That is not money. Give me your money if you want some coffee!")
                continue

            total = quarters + dimes + nickles + pennies
            change = total - cost
            if total < cost:
                print(f"Sorry that's not enough money. Money refunded: ${total}")
            elif total >= cost:
                    # count resources
                    water = water - 200
                    milk = milk - 150
                    coffee = coffee - 24
                    profit = profit + 2.5
                    print(f"Here is ${round(change, 2)} in change. \nHere is your espresso! Enjoy!")
        else:
            print("Not enough resources")

    #CAPPUCCINO
    elif start == "cappuccino":
        if water > 50 and coffee > 18 and milk > 100:
            cost = 3.0
            print(f"Price: ${cost} \nPlease insert coins.")
            try:
                quarters = int(input("How many quarters? ")) * 0.25
                dimes = int(input("How many dimes? ")) * 0.10
                nickles = int(input("How many nickles? ")) * 0.05
                pennies = int(input("How many pennies? ")) * 0.01
            except:
                print("That is not money. Give me your money if you want some coffee!")
                continue

            total = quarters + dimes + nickles + pennies
            change = total - cost
            if total < cost:
                print(f"Sorry that's not enough money. Money refunded: ${total}")
            elif total >= cost:
                    # count resources
                    water = water - 250
                    milk = milk - 100
                    coffee = coffee - 24
                    profit = profit + 3.0
                    print(f"Here is ${round(change, 2)} in change. \nHere is your espresso! Enjoy!")
        else:
            print("Not enough resources")

    elif start == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nProfit: ${profit}")
    elif start == "off":
        break
    else:
        print("Invalid input. Please, try once more!")

