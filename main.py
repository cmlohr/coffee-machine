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
    "water": 0,
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
    print("commands:")
    print("---------------------------")
    print("'report' displays the current supply level")
    print("'off' turns off machine")
    print("---------------------------")

    # print("Here is your {drink} ☕ enjoy!")
    # print("Sorry that's not enough money.  Money Refunded.")
# TODO 2 Check resources sufficient to make drink order.


# needs to print the remaining resources
# provides change
# calculates change
# refunds money if not enough
# Thank you for shopping at this kiosk
# deduct resources add money into bank

def kiosk():
    menu()

    nickle = 0.05
    dime = 0.1
    penny = 0.01
    quarter = .25
    wallet = 0
    bank = 0
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
        # Resources
        water_supply = resources.get('water')
        milk_supply = resources.get('milk')
        coffee_supply = resources.get('coffee')
        # input output conditions
        order = input("What would you like to order?:\n> ").lower()
        if order == "help":
            kiosk_help()
        elif order == "report":
            print("_____Supply_____")
            print(f"Water Level: {water_supply}ml")
            print(f"Milk Level: {milk_supply}ml")
            print(f"Coffee Level: {coffee_supply}g")
            print(f"Bank: ${bank}")
            print("________________")

        elif order == "espresso":
            if espr_rec.get('water') > water_supply:
                print("Sorry there isn't enough water.\nPlease contact management.")
                kiosk()
            if espr_rec.get('coffee') > coffee_supply:
                print("Sorry there isn't enough coffee grounds.\nPlease contact management.")
                kiosk()
            if espr_rec.get('milk') > milk_supply:
                print("Sorry there isn't enough milk.\nPlease contact management.")
                kiosk()
            total = 0
            total += price_espr
            water_supply -= espr_rec.get('water')
            coffee_supply -= espr_rec.get('coffee')
            form_total = "{:.2f}".format(total)
            print(f"your total is: {form_total}")
            print("Please insert coins:")
            q_coin = float(input("How many quarters?\n> "))
            wallet += q_coin * quarter
            print(wallet)
            d_coin = float(input("How many dimes?\n> "))
            wallet += d_coin * dime
            n_coin = float(input("How many nickles?\n> "))
            wallet += n_coin * nickle
            p_coin = float(input("How many penny's?\n> "))
            wallet += p_coin * penny
            change = wallet - total
            form_change = "{:.2f}".format(change)
            bank += total
            print(f"bank test: {bank}") #
            print(f"change test: Here is {form_change} in change.")
            drink = "Espresso"

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
            total = 0
            total += price_latte
            water_supply -= latte_rec.get('water')
            coffee_supply -= latte_rec.get('coffee')
            milk_supply -= latte_rec.get('milk')
            form_total = "{:.2f}".format(total)
            print(f"your total is: {form_total}")
            print("Please insert coins:")
            q_coin = float(input("How many quarters?\n> "))
            wallet += q_coin * quarter
            print(wallet)
            d_coin = float(input("How many dimes?\n> "))
            wallet += d_coin * dime
            n_coin = float(input("How many nickles?\n> "))
            wallet += n_coin * nickle
            p_coin = float(input("How many penny's?\n> "))
            wallet += p_coin * penny
            change = wallet - total
            form_change = "{:.2f}".format(change)
            bank += total
            print(f"bank test: {bank}")  #
            print(f"change test: Here is ${form_change} in change.")
            drink = "Latte"

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
            print(f"your total is: {form_total}")
            print("Please insert coins:")
            q_coin = float(input("How many quarters?\n> "))
            wallet += q_coin * quarter
            print(wallet)
            d_coin = float(input("How many dimes?\n> "))
            wallet += d_coin * dime
            n_coin = float(input("How many nickles?\n> "))
            wallet += n_coin * nickle
            p_coin = float(input("How many penny's?\n> "))
            wallet += p_coin * penny
            change = wallet - total
            form_change = "{:.2f}".format(change)
            bank += total
            print(bank)
            print(f"Here is {form_change} in change.")
            drink = "Cappuccino"

        elif order == "off":
            cont = False

        else:
            print("Invalid Input")
            kiosk()
kiosk()
 # print(f"Supply Testing\nWater: {water_supply} | Coffee: {coffee_supply} | Milk: {milk_supply}")
