from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


print(menu.find_drink("latte"))
print(menu.find_drink("espresso"))
print(menu.find_drink("cappuccino"))

is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f"What would you like to order {option}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(menu.find_drink(choice).cost)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            is_on = False

