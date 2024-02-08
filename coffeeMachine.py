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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def print_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nProfit: ${profit}")

while True:
    user_input = input("what would u like? (espresso/latte/cappucino): ").lower()

    if user_input == "off" :
        print("turning off the coffee machine. have a great day! ")
        break
    elif user_input == "report":
        print_report() 
    elif user_input in MENU:
        ingredients = MENU[user_input]["ingredients"]
        cost = MENU[user_input]["cost"]

        insufficient_resource = False
        for ingredient, amount in ingredients.items():
            if resources[ingredient] < amount:
                print(f"Sorry, not enough {ingredient}. Please choose another option.")
                insufficient_resource = True
                break
        if insufficient_resource:
            continue


        quarters = int(input("how many quarters? ")) * 0.25
        dimes = int(input("how many dimes? ")) * 0.10 
        nickels = int(input("how many nickels? ")) * 0.05 
        pennies = int(input("how many pennies? ")) * 0.01

        total_money_inserted = quarters + dimes + nickels + pennies

        if total_money_inserted < cost:
            print("sprry, not enough money. money refunded! ")
        else: 
            change = round(total_money_inserted - cost, 2) 
            profit += cost
            print(f"transaction successful. here is your {user_input}. ")
            if change > 0 :
                print(f"here is ${change} in change. ") 

            for ingredients, amount in ingredients.items() :
                resources[ingredient] -= amount
    else: 
        print("invalidinput. please enter 'espresso', 'latte', 'cappuccino', 'off', or 'report'. ")


