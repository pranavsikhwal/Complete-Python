menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 300,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 350,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def sufficient(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items]>resources[items]:
            print(f"Sorry there is not enough {items}")
            return False
    return True
def process_coins():
    print("Welcome to the coffee machine . Please insert coins .")
    total = int(input("How many 10 rupees notes . "))*10
    total +=  int(input("How many 50 rupees notes . "))*50
    total +=  int(input("How many 100 rupees notes . "))*100
    total +=  int(input("How many 500 rupees notes . "))*500
    return total
def is_transaction_successful(money_received,drink_cost):
    if money_received < drink_cost:
        print(f"Sorry there is not enough money received. Money refunded")
        return False
    else:
        change = round(money_received - drink_cost,2)
        global profit
        profit += drink_cost
        print(f"here is the change :{change}")
        return True
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Enjoy your coffee")
is_coffee_continue = True
while is_coffee_continue:
    user_choice = input("What would you like? Espresso, latte,cappuccino: \n").lower()
    if user_choice == "off":
        is_coffee_continue = False
    elif user_choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk:{resources['milk']} ml")
        print(f"Coffee:{resources['coffee']} ml")
        print(f"Money:{profit} rupees")
    else:
        drink = menu[user_choice]
        if sufficient(drink["ingredients"]):
           payment =  process_coins()
           if is_transaction_successful(payment,drink["cost"]):
              make_coffee(user_choice,drink["ingredients"])



