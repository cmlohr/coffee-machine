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


# TODO 2 Check resources sufficient to make drink order.


# needs to print the remaining resources
# provides change
# calculates change
# refunds money if not enough
# Thank you for shopping at this kiosk
# deduct resources add money into bank

# def kiosk():
#     menu()
total = 0
#     cont = True
#     while cont:

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

# Denomination
nickle = 0.05
dime = 0.1
penny = 0.01
quarter = .25

kiosk_help = str("type commands:\n---------------------------\n'report' displays the current supply level\n'off' turns off machine\n---------------------------")
# FORMAT TO THE SECOND DECIMAL PLACE
# formatted_total = "{:.2f}".format(###)

#######################input output conditions
order = input("What would you like to order?:\n> ").lower()
if order == "help":
    print(kiosk_help)
elif order == "report":
    print("_____Supply_____")
    print(f"Water Level: {water_supply}ml")
    print(f"Milk Level: {milk_supply}ml")
    print(f"Coffee Level: {coffee_supply}g")
    print("________________")
elif order == "espresso":
    total += price_espr
    water_supply -= espr_rec.get('water')
    coffee_supply -= espr_rec.get('coffee')
    print(f"Espresso:  ${espr_drink.get('cost')}")
#    print(total)  # test
elif order == "latte":
    total += price_latte
    water_supply -= latte_rec.get('water')
    coffee_supply -= latte_rec.get('coffee')
    milk_supply -= latte_rec.get('milk')
    print(f"Latte: ${latte_drink.get('cost')}")
    print(total)  # test
elif order == "cappuccino":
    total += price_capp
    water_supply -= capp_rec.get('water')
    coffee_supply -= capp_rec.get('coffee')
    milk_supply -= capp_rec.get('milk')
    #print(f"Supply Testing\nWater: {water_supply} | Coffee: {coffee_supply} | Milk: {milk_supply}")
    print(f"Cappuccino: ${capp_drink.get('cost')}")
    print(total) #test
elif order == "off":
    print("turn off machine")
else:
    print("Invalid Input")
    #kiosk()
# kiosk()