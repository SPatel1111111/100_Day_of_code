from Menu import Menu
from coffee_maker import CoffeeMaker
from Money_machine import MoneyMachine

money_machine =MoneyMachine()
coffee_maker =CoffeeMaker()
menu =Menu()
is_on =True

while is_on:
    option=menu.get_items()
    choice = input("What would you like?(Espresso/latte/cappuccino)or for the report and off the machine(off/report):").lower()
    if choice == "off":
        is_on =False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink_choice=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink_choice):
            if money_machine.make_payment(drink_choice.cost):
                coffee_maker.make_coffee(drink_choice)


