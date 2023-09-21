from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()



machine="on"

while machine=="on":
    option=menu.get_items()
    choice=input(f"What Would you Like? {option}")
    if choice=="off":
        machine="off"
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        
