from menu import MENU, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
profit = 0


# TODO 1. Print report of all coffee machine resources


def report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Profit: ${profit}")


# TODO 2. Check resources sufficient to make drink order
def check_resources(order, cust_coffee):
    if order == 'espresso' and cust_coffee['water'] > water or cust_coffee['coffee'] > coffee:
        return False
    if order == 'latte' or order == 'cappuccino':
        if cust_coffee['water'] > water or cust_coffee['milk'] > milk or cust_coffee['coffee'] > coffee:
            return False

    return True


# TODO 3. Process coins
def payment():
    pennies = int(input("How many pennies? "))
    nickles = int(input("How many nickles? ")) * .05
    dimes = int(input("How many dimes? ")) * .10
    quarters = int(input("How many dimes? ")) * .25

    total = pennies + nickles + dimes + quarters
    return total

# TODO 4. Check transaction successful
# TODO 5. Make coffee

def resource_reduce(a,b=0):
    return a - b


on = True


while on:
    order = input("What would you like? (espresso/latte/cappuccino) ").lower()
    options = ['espresso', 'latte', 'cappuccino', 'report']

    if order not in options:
        print(f'{order} is not an option try again. ')
    elif order == 'report':
        report()
    else:
        order_ingredients = MENU[order]['ingredients']
        order_pricing = MENU[order]['cost']
        if check_resources(order, order_ingredients):
            cust_funds = payment()
            if cust_funds > order_pricing:
                change = cust_funds - order_pricing
                print(f"here is {change} in change")
                if 'milk' in order_ingredients:
                    milk = resource_reduce(milk, order_ingredients["milk"])
                water = resource_reduce(water, order_ingredients["water"])
                coffee = resource_reduce(coffee, order_ingredients["coffee"])
                profit = profit + order_pricing
            else:
                print("not enough funds")

