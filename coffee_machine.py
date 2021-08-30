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
}


coins = {
    "1p": 0.01,
    "2p": 0.02,
    "5p": 0.05,
    "10p": 0.10,
    "20p": 0.20,
    "50p": 0.50,
    "£1": 1.00,
    "£2": 2.00
}

coffee_machine = True
money = 0


def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
    print(f"Money: £{money}")


def check_sufficient_resources(drink):
    """Checks whether there is enough milk, water and coffee to make the drink desired by the user."""
    for ingredient, amount in MENU[drink]['ingredients'].items():
        while resources[ingredient] < amount:
            return False
        else:
            return True


def make_drink(drink):
    """Changes the resources available by taking away what was used to make the drink."""
    for ingredient, amount in MENU[drink]['ingredients'].items():
        resources[ingredient] = resources[ingredient] - amount
        print(resources[ingredient])


while coffee_machine:
    drink_option = input('What would you like to drink? (Espresso/latte/cappuccino)\n').lower()
    if drink_option == "off":
        break
    elif drink_option == "report":
        report()
    elif drink_option == "espresso" or drink_option == "latte" or drink_option == "cappuccino":
        price = MENU[drink_option]['cost']
        if check_sufficient_resources(drink_option):
            print(f"This costs £{price}. Please insert some coins.")
            for key, value in coins.items():
                number_of_coins = float(input(f'How many {key} coins do you have? '))
                money = money + (number_of_coins * value)
            if money < price:
                print("Sorry, that's not enough money. You've been refunded.")
                money = 0
            elif money == price:
                make_drink(drink_option)
                print(f"Here's your {drink_option}! Enjoy!")
            else:
                make_drink(drink_option)
                change = money - price
                print(f"Here's your {drink_option} and £{change} in change! Enjoy!")
        else:
            print("Sorry, we don't have the ingredients to make that.")
    else:
        print("Sorry, that's not an option.")
