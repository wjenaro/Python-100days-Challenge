# Initialize resources and prices
resources = {
    "water": 300,  # ml
    "milk": 200,   # ml
    "coffee": 100, # mg
    "sugar": 2000, # mg
    "tea powder": 500, # mg
}

drink_prices = {
    'tea': 25,    # ksh
    'coffee': 30, # ksh
}

# Define drink recipes
recipe = {
    'tea': {
        'ingredients': {
            'milk': 200,
            'tea powder': 6,
            'water': 50,
            'sugar': 12
        },
        "cost": 15
    },
    'coffee': {
        'ingredients': {
            "water": 250,
            "coffee": 18,
            "sugar": 12,
        },
        "cost": 18
    }
}

machine_is_on = True

# Main loop
while machine_is_on:
    choice = input("What would you like? (coffee/tea) Input 'off' to turn off the machine: ")
    
    if choice == "off":
        print("Turning off the machine.")
        machine_is_on = False
    elif choice in recipe:
        drink = choice
        drink_data = recipe[drink]
        ingredients = drink_data['ingredients']
        drink_price = drink_prices[drink]
        
        print(f"The price of {drink} is: {drink_price} ksh")
        
        insufficient_resources = False
        for ingredient, required_amount in ingredients.items():
            if resources[ingredient] < required_amount:
                print(f"Sorry, not enough {ingredient}.")
                insufficient_resources = True
                break
        
        if insufficient_resources:
            continue
        
        coins = int(input("Insert coins: "))
        total_money = coins * 5  # Assuming each coin is 5 ksh
        
        if total_money < drink_price:
            print(f"Sorry, not enough money. Please insert {drink_price - total_money} ksh more.")
            machine_is_on = False
        else:
            balance = total_money - drink_price
            profit = drink_price - drink_data['cost']
            
            print(f"Dispensing {drink}. Enjoy!")
            print(f"Your balance: {balance} ksh")
            print(f"Profit from this sale: {profit} ksh")
            
            # Deduct the used resources
            for ingredient, required_amount in ingredients.items():
                resources[ingredient] -= required_amount
    else:
        print("Invalid choice. Please select 'coffee', 'tea', or 'off'.")
