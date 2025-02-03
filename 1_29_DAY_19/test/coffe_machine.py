MENU = {
    "latte": {"ingredients": {"water": 150, "milk": 100, "coffee": 50}, "cost": 5},
    "cappuccino": {"ingredients": {"water": 150, "milk": 200, "coffee": 50}, "cost": 10},
    "expresso": {"ingredients": {"water": 200,"milk":0, "coffee": 50}, "cost": 15}
}

resources = {"milk": 300, "water": 300, "coffee": 100}

profit =0
def enough_resource(order_resource):
    for item in order_resource:
        if order_resource[item] > resources[item]:
            print("Sorry not enough resources.")
            return False
        return True

def amount():
    total = float(input("enter money:"))
    return total


def check_tansaction(given_money,drink_cost):
    if given_money < drink_cost:
        print("sorry not enough money is given.")
        return False
    else:
        change = given_money-drink_cost
        print(f"here your change {change}.")
        global profit
        profit += drink_cost
    return True

def coffe_make(drink_ingred,resource_ingred):
    for i in resource_ingred:
        resource_ingred[i] = resource_ingred[i] - drink_ingred[i]
    return True

is_on = True

while is_on:
    print("Do you want order coffee?")
    order = input(
        "options are (latte/cappuccino/expresso).if you want to make coffee,enter coffee name or for the ingredients report type 'report' or for off the machine type 'off'.").lower()
    if order == 'off':
        is_on = False
    elif order == 'report':
        print(f"milk:{resources["milk"]} \nwater:{resources["water"]} \ncoffee:{resources["coffee"]} \nprofit:{profit}")
    else:
        drink = MENU[order]
        if enough_resource(order_resource=drink["ingredients"]):
            pyment = amount()
            if check_tansaction(given_money=pyment,drink_cost=drink["cost"]):
                if coffe_make(drink_ingred=drink["ingredients"],resource_ingred=resources):
                    print(f" here your order {order}.")

