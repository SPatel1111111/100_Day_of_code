MENU = {"cappuccino": {"ingredients": {"milk": 100, "water": 150, "coffee": 50}, "cost": 10},
        "latte": {"ingredients": {"milk": 150, "water": 100, "coffee": 50}, "cost": 7},
        "expresso": {"ingredients": {"milk": 0, "water": 200, "coffee": 50}, "cost": 15}
        }

resources = {"milk": 300, "water": 300, "coffee": 200}
profit = 0

def enough_resource(order_reso):
    for item in order_reso:
        if order_reso[item] > resources[item]:
            print("sorry not enough resource.")
            return False
    return True

def amount():
    x = float(input("enter rupees:"))
    return x


def check_tansaction(money_received, drink_cost):
    if money_received < drink_cost:
        print("this is not enough money to buy coffee.")
        return False
    else:
        change = money_received - drink_cost
        print(f"your order is accepted. here your change {change} rupee.")
        global profit
        profit += drink_cost
        return True

def make_coffee(drink_resource,machine_resource):
    for i in machine_resource:
        machine_resource[i]=machine_resource[i]-drink_resource[i]


is_on = True

while is_on:
    print("Do you want to buy coffee??")
    choice = input(
        "for the coffee type(latte/expresso/cappuccino) and for the report type 'report' and for the off type 'off': ")
    if choice == 'report':
        print(f"milk:{resources["milk"]} \nwater:{resources["water"]} \ncoffee:{resources["coffee"]} \nprofit:{profit}")
    elif choice == 'off':
        is_on = False
    else:
        drink = MENU[choice]
        if enough_resource(order_reso=drink["ingredients"]):
            money = amount()
            if check_tansaction(money_received=money,drink_cost=drink["cost"]):
                if make_coffee(drink_resource=drink["ingredients"],machine_resource=resources):
                    print(f"here your order {choice}.")

