# 2020 @Cmlohr

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


def menu():
    print("Welcome to the Coffee Kiosk")
    print("           MENU")
    print("---------------------------")
    print("Espresso\nLatte\nCappuccino")
    print("---------------------------")
    print("   type your selection")


def kiosk_help():
    print("Instructions")
    print("Type your order, eg: espresso")
    print("Other kiosk commands:")
    print("---------------------------")
    print("'report' displays a report of\nthe stock level and bank")
    print("'off' turns off machine")
    print("---------------------------")


def kiosk():
    print("---------------------------")
    nickle = 0.05
    dime = 0.10
    penny = 0.01
    quarter = 0.25
    wallet = 0.00
    bank = 0.00
    water_supply = resources.get('water')
    milk_supply = resources.get('milk')
    coffee_supply = resources.get('coffee')
    cont = True
    while cont:
        # Separating out the values
        espr_drink = MENU.get('espresso')
        latte_drink = MENU.get('latte')
        capp_drink = MENU.get('cappuccino')
        # PRICES
        price_espr = float(espr_drink.get('cost'))
        price_latte = float(latte_drink.get('cost'))
        price_capp = float(capp_drink.get('cost'))
        # Drink resources requirements
        espr_rec = espr_drink.get('ingredients')
        latte_rec = latte_drink.get('ingredients')
        capp_rec = capp_drink.get('ingredients')
        menu()


        order = input("What would you like to order?:\n> ").lower()
        if order == "help":
            kiosk_help()
        elif order == "report":
            print("----------report-----------")
            print(f"Water Level: {water_supply}ml")
            print(f"Milk Level: {milk_supply}ml")
            print(f"Coffee Level: {coffee_supply}g")
            form_bank = "{:.2f}".format(bank)
            print(f"Bank: ${form_bank}")
            print("---------------------------")

        elif order == "espresso":
            if espr_rec.get('water') > water_supply:
                print("Sorry there isn't enough water.\nPlease contact management.")
                print("---------------------------")
                kiosk()
            if espr_rec.get('coffee') > coffee_supply:
                print("Sorry there isn't enough coffee grounds.\nPlease contact management.")
                print("---------------------------")
                kiosk()
            total = 0.00
            total += price_espr
            water_supply -= espr_rec.get('water')
            coffee_supply -= espr_rec.get('coffee')
            form_total = "{:.2f}".format(total)
            print(f"your total is: {form_total}")
            print("Please insert coins:")
            q_coin = float(input("How many Quarters?\n> "))
            wallet += q_coin * quarter
            d_coin = float(input("How many Dimes?\n> "))
            wallet += d_coin * dime
            n_coin = float(input("How many Nickles?\n> "))
            wallet += n_coin * nickle
            p_coin = float(input("How many Pennies?\n> "))
            wallet += p_coin * penny
            if wallet < total:
                print("---------------------------")
                print("Sorry, that is not enough.\nYour transaction has been\ncanceled and money refunded.")
                print("---------------------------")
                kiosk()
            change = wallet - total
            form_change = "{:.2f}".format(change)
            bank += total
            print(f"Your change is ${form_change}")
            print(f"Here is your Espresso.️Enjoy!")
            print("Thank you for shopping with us!")
            print("---------------------------")

        elif order == "latte":
            if latte_rec.get('water') > water_supply:
                print("Sorry there isn't enough water.\nPlease contact management.")
                kiosk()
            if latte_rec.get('coffee') > coffee_supply:
                print("Sorry there isn't enough coffee grounds.\nPlease contact management.")
                kiosk()
            if latte_rec.get('milk') > milk_supply:
                print("Sorry there isn't enough milk.\nPlease contact management.")
                kiosk()
            total = 0.00
            total += price_latte
            water_supply = water_supply - latte_rec.get('water')
            coffee_supply = coffee_supply - latte_rec.get('coffee')
            milk_supply = milk_supply - latte_rec.get('milk')
            form_total = "{:.2f}".format(total)
            print(f"your total is: {form_total}")
            print("Please insert coins:")
            q_coin = float(input("How many Quarters?\n> "))
            wallet += q_coin * quarter
            d_coin = float(input("How many Dimes?\n> "))
            wallet += d_coin * dime
            n_coin = float(input("How many Nickles?\n> "))
            wallet += n_coin * nickle
            p_coin = float(input("How many Pennies?\n> "))
            wallet += p_coin * penny
            if wallet < total:
                print("---------------------------")
                print("Sorry, that is not enough.\nYour transaction has been\ncanceled and money refunded.")
                kiosk()
            change = wallet - total
            form_change = "{:.2f}".format(change)
            bank += total
            print(f"Your change is ${form_change}")
            print(f"Here is your Latte.️Enjoy!")
            print("Thank you for shopping with us!")

        elif order == "cappuccino":
            if capp_rec.get('water') > water_supply:
                print("Sorry there isn't enough water.\nPlease contact management.")
                kiosk()
            if capp_rec.get('coffee') > coffee_supply:
                print("Sorry there isn't enough coffee grounds.\nPlease contact management.")
                kiosk()
            if capp_rec.get('milk') > milk_supply:
                print("Sorry there isn't enough milk.\nPlease contact management.")
                kiosk()
            total = 0
            total += price_capp
            water_supply -= capp_rec.get('water')
            coffee_supply -= capp_rec.get('coffee')
            milk_supply -= capp_rec.get('milk')
            form_total = "{:.2f}".format(total)
            print(f"your total is: ${form_total}")
            print("Please insert coins:")
            q_coin = float(input("How many Quarters?\n> "))
            wallet += q_coin * quarter
            d_coin = float(input("How many Dimes?\n> "))
            wallet += d_coin * dime
            n_coin = float(input("How many Nickles?\n> "))
            wallet += n_coin * nickle
            p_coin = float(input("How many Pennies?\n> "))
            wallet += p_coin * penny
            if wallet < total:
                print("---------------------------")
                print("Sorry, that is not enough.\nYour transaction has been\ncanceled and money refunded.")
                kiosk()
            change = wallet - total
            form_change = "{:.2f}".format(change)
            bank += total
            print(f"Your change is ${form_change}")
            print(f"Here is your Cappuccino. Enjoy!")
            print("Thank you for shopping with us!")

        elif order == "off":
            cont = False
        else:
            print("Invalid Input")
            kiosk()


kiosk()
