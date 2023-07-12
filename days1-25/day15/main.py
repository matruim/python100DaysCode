MENU = {
    "espresso": {
        "ingredients": {
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
    "money": 0
}

def checkResources(drink: dict, currentStock: dict):
    lackingResources = [
        ingredient.capitalize()
        for ingredient, required_quantity in drink["ingredients"].items()
        if ingredient not in currentStock or required_quantity > currentStock[ingredient]
    ]
    return lackingResources

def makeDrink(drink: dict, currentStock: dict, total: float):
    change = total - drink["cost"]
    for ingredient, required_quantity in drink["ingredients"].items():
        currentStock[ingredient] -= required_quantity
    currentStock["money"] += drink["cost"]
    return change, currentStock

def processPayment(order_cost):
    print(f"That will be ${order_cost:.2f}")
    print("Please insert coins!")

    coins = {
        "Quarters": 0.25,
        "Dimes": 0.1,
        "Nickels": 0.05,
        "Pennies": 0.01
    }

    total = 0
    remaining_cost = order_cost

    for coin_name, coin_value in coins.items():
        coin_count = int(input(f"How many {coin_name}? "))
        total += coin_count * coin_value
        remaining_cost -= coin_count * coin_value

        if total >= order_cost:
            break

        print(f"You still owe ${remaining_cost:.2f}")

    return total


while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")

    if order == "off":
        break

    elif order == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${resources['money']:.2f}")

    elif order in MENU:
        lacking_ingredients = checkResources(MENU[order], resources)
        if not lacking_ingredients:
            total = processPayment(MENU[order]["cost"])

            if total >= MENU[order]["cost"]:
                change, resources = makeDrink(MENU[order], resources, total)

                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {order}. ☕️ Enjoy!")
            else:
                print("Sorry, that's not enough money. Money refunded.")

        else:
            print("The following ingredients are lacking or insufficient:")
            print('\n'.join(lacking_ingredients))
