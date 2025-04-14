Menu={
    "espresso":{
        "ingredients":{
        "water":50,
        "coffee":18,
    },
    "cost":20,
},

"latte":{
    "ingredients":{
        "water":200,
        "coffee":24,
        "milk":150,
        },
    "cost":50
    },
"cappuccino":{
    "ingredients":{
        "water":250,
        "coffee":24,
        "milk":100,
        },
    "cost":80
    }
}
resources={
    "water":300,
    "milk":200,
    "coffee":100,
}
stop=True
while stop:
    drink=input("What would you like espresso/latte/cappuccino:")
    if drink=="report":
        print(resources)
    amount_5=int(input(print("How many 5rs:")))
    amount_10=int(input(print("How many 10rs")))
    amount_20=int(input(print("How many 20rs:")))
    total_amount=(5*amount_5)+(10*amount_10)+(20*amount_20)

    def check_requirements(drink_name):
        if Menu[drink_name]["ingredients"].get("milk",0)<=resources["milk"] and Menu[drink_name]["ingredients"]["coffee"]<=resources["coffee"] and Menu[drink_name]["ingredients"]["water"]<=resources["water"] :
            return True
        else:
            print(resources)
            return False
    def check_amount(drink_name,amount):
        if amount>=Menu[drink_name]["cost"]:
            change=amount-Menu[drink_name]["cost"]
            print(f"cahnge:{change}")
            return True
        else:
            print(amount)
            return False

    def coffee_machine(drink):
        global stop
        if check_requirements(drink) and check_amount(drink,total_amount):
            print(f"Enjoy you're drink {drink}")
            resources["coffee"]=resources["coffee"]-Menu[drink]["ingredients"]["coffee"]
            resources["milk"]=resources["milk"]-Menu[drink]["ingredients"].get("milk",0)
            resources["water"]=resources["water"]-Menu[drink]["ingredients"]["water"]
        else:
            print("Unsufficient resourses ")
            stop=False
    coffee_machine(drink)    

      