menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
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
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def order_ingredients():
    order_ingredients=menu[choice]['ingredients']
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
def cost():
    global profit
    charge=menu[choice]['cost']
    profit += charge
    resources["profit"]=profit
    print(f"Thank You For Ordering Here Is Your {choice}")
  
def is_resource_sufficient():
    order_ingredients=menu[choice]['ingredients']
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def process_money():
    total=int(input("Enter The ₹ In Machine  ₹"))
    cash=menu[choice]["cost"]
    if total>= cash:
        total -=  cash
        print("Here Is Your Change ₹",total)
        return True
    elif total<cash:
        print(f"You Need {-(total-cash)} ₹ to buy {choice}")
        return False
        

profit=0
power=True
while power:
    choice = input("What would you like? (espresso / latte /cappuccino) : ")
    if choice=="espresso":
        if is_resource_sufficient()==True:
            if process_money():
                order_ingredients()
                cost()
    elif choice=="latte":
        if is_resource_sufficient()==True:
             if process_money():
                order_ingredients()
                cost()
    elif choice=="cappuccino":
        if is_resource_sufficient()==True:
           if process_money():
            order_ingredients()
            cost()
    elif choice=="report":
        print(resources)
    elif choice =="off":
        power=False


