coffee_menu = {
    "espresso": {
        "water": 30,      # ml
        "milk": 0,        # ml
        "coffee": 7,      # g
        "sugar": 5,       # g
        "cost": 120       # INR
    },
    "latte": {
        "water": 30,
        "milk": 210,
        "coffee": 7,
        "sugar": 7,
        "cost": 180
    },
    "cappuccino": {
        "water": 30,
        "milk": 120,
        "coffee": 7,
        "sugar": 7,
        "cost": 180
    }
}

money=0
milk=1000
water=1000
coffee=100
sugar=100
espresso=0
latte=0
cappuccino=0
ex=0
print("Hello there. welcome to coffee machine\n")
while (water>30 and milk>0 and coffee>7 and sugar>5 ):
    choice=input("enter what you need espresso or latte or cappuccino : ").lower()
    rs5=int(input("How many 5 rs coin : "))
    rs10=int(input("How many 10 rs coin : "))
    rs20=int(input("How many 20 rs coin : "))
    print("\n")
    sum=(5*rs5+10*rs10+20*rs20)
    
    if choice=="espresso":
        if water>=30 and coffee>=7 and sugar >=5:
            if sum> coffee_menu['espresso']['cost']:
                print(f"Here is your change {sum-coffee_menu['espresso']['cost']}")
                print("Here is your espresso\n")
                money+=coffee_menu['espresso']['cost']
            elif sum==coffee_menu['espresso']['cost']:
                print(f"the amount is correct")
                print("Here is your espresso\n")
                money+=coffee_menu['espresso']['cost']
            else:
                print(f"The amount is lower please put {coffee_menu['espresso']['cost']} ")
                continue
            milk-=coffee_menu['espresso']['milk']
            water-=coffee_menu['espresso']['water']
            coffee-=coffee_menu['espresso']['coffee']
            sugar-=coffee_menu['espresso']['sugar']
            espresso+=1
        else:
            print("Sorry not enough ingredients")
            print(f"Here is your money back {sum}")
            continue
        
    elif choice=="latte":
        if water>=30 and coffee>=7 and sugar >=5 and milk>=210:
            if sum> coffee_menu['latte']['cost']:
                print(f"Here is your change {sum-coffee_menu['latte']['cost']}")
                print("Here is your latte\n")
                money+=coffee_menu['latte']['cost']
            elif sum==coffee_menu['latte']['cost']:
                print(f"the amount is correct")
                print("Here is your latte\n")
                money+=coffee_menu['latte']['cost']
            else:
                print(f"The amount is lower please put {coffee_menu['latte']['cost']} ")
                continue
            milk-=coffee_menu['latte']['milk']
            water-=coffee_menu['latte']['water']
            coffee-=coffee_menu['latte']['coffee']
            sugar-=coffee_menu['latte']['sugar']
            latte+=1
        else:
            print("Sorry not enough ingredients")
            print(f"Here is your money back {sum}")
            continue
                
    elif choice=="cappuccino":
        if water>=30 and coffee>=7 and sugar >=5 and milk>=210:
            if sum> coffee_menu['cappuccino']['cost']:
                print(f"Here is your change {sum-coffee_menu['cappuccino']['cost']}")
                print("Here is your Cappuccino\n")
                money+=coffee_menu['cappuccino']['cost']
            elif sum==coffee_menu['cappuccino']['cost']:
                print(f"the amount is correct")
                print("Here is your Cappuccino\n")
                money+=coffee_menu['cappuccino']['cost']
            else:
                print(f"The amount is lower please put {coffee_menu['cappuccino']['cost']} ")
                continue
            milk-=coffee_menu['cappuccino']['milk']
            water-=coffee_menu['cappuccino']['water']
            coffee-=coffee_menu['cappuccino']['coffee']
            sugar-=coffee_menu['cappuccino']['sugar']
            cappuccino+=1
        else:
            print("Sorry not enough ingredients")
            print(f"Here is your money back {sum}")
            continue
    else:
        print("Invalid input")
        print(f"Here is your money back {sum}")
        continue
    ex=int(input("Press 0 to continue and 1 to exit : "))
    if ex==0:
        continue
    elif ex==1:
        print("Enjoy the coffee!\n")
        break
else:
    print("we are out of ingredients")
    
print(f"You have ordered \n{espresso} espressos\n{latte} lattes\n{cappuccino} cappuccinos.\nAnd to purchase this you have paid Rs {money}\nThank You\n")
print("For opperators info. The remaining ingredients and money are as following")
print(f"money = {money} Rs\nsugar = {sugar} gm\nmilk = {milk} ml\nwater = {water} ml\ncoffee = {coffee} gm")




