# coffee machine

MENU = {
    "espresso": {
        "ingredients": {
            "milk":0,
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
profit =0

def check_resource_sufficient(ordered_resource):
    for item in ordered_resource:
        if ordered_resource[item] >= resources[item]:
            print(f"Sorry! there is not enough {item}")
            return False
    return True

def process_coin():
    print("enter total coins:")
    total = int(input(" how many pennies(0.01)?:")) * 0.01
    total += int(input(" how many nickles(0.05)?:")) * 0.05
    total += int(input(" how many quarters(0.25)?:")) * 0.25
    total += int(input(" how many dimes(0.1)?:")) * 0.10
    return total

def check_transaction(recived_cost,drink_cost):
    if recived_cost<= drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change=recived_cost-drink_cost
        print(f"your {change}$ change is here.")
        global profit
        profit += drink_cost
        return True

def make_coffee(drink_name,order_ingredients):
    for items in order_ingredients:
        resources[items]-=order_ingredients[items]
    print(f" here your {drink_name}.")

is_this =True

while is_this:
    choice=input("What would you like?(Espresso/latte/cappuccino)or for the report and off the machine(off/report):").lower()
    if choice =="off":
        is_this = False
    elif choice=="report":
        print("here the remaining ingredients are left and total profit we gain.")
        print(f"milk:{resources["milk"]}")
        print(f"water:{resources["water"]}")
        print(f"coffee:{resources["coffee"]}")
        print(f"cost:${profit}")
    else:
        drink=MENU[choice]
        if check_resource_sufficient(drink['ingredients']):
            payment = process_coin()
            if check_transaction(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])





