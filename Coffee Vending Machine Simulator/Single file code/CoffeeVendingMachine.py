def estimateCost():
    c1 = int(input("Quarters : "))
    c2 = int(input("Dimes : "))
    c3 = int(input("Nickles : "))
    c4 = int(input("Pennies : "))
    print()
    return c1 * 0.25 + c2 * 0.1 + c3 * 0.05 + c4 * 0.01


def checkResources(ingredients):
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print("Sorry there is not enough " + item)
            return False
    return True


def updateResources(check):
    innerItem = check["ingredients"]
    for item in innerItem:
        resources[item] = resources[item] - innerItem[item]
    resources["money"] = resources["money"] + check["cost"]


def preparation(userInput):
    check = MENU[userInput]
    if checkResources(check["ingredients"]):
        totalCost = estimateCost()
        if totalCost < check["cost"]:
            return "Sorry that's not enough money"
        elif totalCost == check["cost"]:
            updateResources(check)
        elif totalCost > check["cost"]:
            updateResources(check)
            change = totalCost - check["cost"]
            print("Here is " + f"{change:.{2}f}" + " dollars in change.")
            print()
    else:
        return ""
    return "Here is your ☕ " + userInput + ". Enjoy!."


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

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

while True:
    print()
    userInput = input("What would you like? (espresso/latte/cappuccino):")
    if userInput.lower() == "off":
        print()
        print("Coffee Machine is Terminated.")
        break
    elif userInput.lower() == "report":
        print()
        print("Water : ", resources["water"], "\nMilk : ", resources["milk"],
              "\nCoffee :", resources["coffee"], "\nMoney : ",
              resources["money"])
    elif userInput not in MENU:
        print()
        print("Please Enter Valid Input.")

    else:
        print()
        print(preparation(userInput.lower()))
