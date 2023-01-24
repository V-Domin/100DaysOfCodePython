from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
latte = MenuItem("latte", 200, 150, 24, 2.5)
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)



coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True

while is_on:
    choice = input(f"What would you like?: {menu.get_items()} ")


    if choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == "off":
        is_on = False

    else:
        order = menu.find_drink(choice)
        try:
            if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
        except:
            continue


