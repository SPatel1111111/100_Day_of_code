MENU = {
    "latte": {"ingredients": {"milk": 100, "water": 150, "coffee": 50}, "cost": 10},
    "cappuccino": {"ingredients": {"milk": 100, "water": 150, "coffee": 50}, "cost": 30},
    "expresso": {"ingredients": {"milk": 0, "water": 200, "coffee": 50}, "cost": 20}
}

resources = {"milk": 300, "water": 300, "coffee": 200}
profit =0
def enough_resource(order_res):
    for item in order_res:
        if order_res[item] > resources[item]:
            print("sorry not enough amount of resources.")
            return False
    return True

def amount():
    x= float(input("enter the money:"))
    return x
def check_trascation(given_money,drink_cost):

    if given_money < drink_cost:
        print("this is not enough money to buy coffee.")
        return False
    else:
        change = given_money - drink_cost
        print(f" here your change {change} rupee.")
        global profit
        profit += drink_cost
        return True

def make_coffee(order_resource,machine_resource):
    for i in machine_resource:
        machine_resource[i]=machine_resource[i]-order_resource[i]
    return True

is_on =True
while is_on:
    print("do you want drink coffee.(latte/cappuccino/expresso).")
    choice = input("enter the coffee name or 'report' or 'off' for the off the machine.:")
    if choice == 'off':
        is_on =False
    elif choice == 'report':
        print(f" milk:{resources["milk"]} \nwater:{resources["water"]} \ncoffee:{resources["coffee"]} \n profit:{profit}")
    else:
        drink=MENU[choice]
        if enough_resource(order_res=drink["ingredients"]):
            money =amount()
            if check_trascation(given_money=money,drink_cost=drink["cost"]):
                if make_coffee(order_resource=drink["ingredients"],machine_resource=resources):
                    print(f"here your order {choice}.")

