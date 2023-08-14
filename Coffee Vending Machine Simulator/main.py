from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    userInput = input("What would you like? (" + menu.get_items() + "):")
    if userInput == "off":
        break
    elif userInput == "report":
        coffee_maker.report()
    else:
        obj = menu.find_drink(userInput)
        if obj:
            if money_machine.make_payment(obj.cost):
                if coffee_maker.is_resource_sufficient(obj):
                    coffee_maker.make_coffee(obj)
