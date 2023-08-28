class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0,
        }
        self.menu = {
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
            },
        }

    def print_report(self):
        print("Current Resources:")
        for resource, amount in self.resources.items():
            if resource != "money":
                print(f"{resource.capitalize()}: {amount}ml")
            else:
                print(f"{resource.capitalize()}: ${amount:.2f}")
        print()

    def check_resources(self, drink):
        for ingredient, amount in self.menu[drink]["ingredients"].items():
            if self.resources[ingredient] < amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        total_amount = quarters + dimes + nickels + pennies
        return total_amount

    def make_coffee(self, drink, payment):
        self.resources["money"] += self.menu[drink]["cost"]
        for ingredient, amount in self.menu[drink]["ingredients"].items():
            self.resources[ingredient] -= amount
        change = payment - self.menu[drink]["cost"]
        if change > 0:
            print(f"Here is ${change:.2f} dollars in change.")
        print(f"Here is your {drink}. Enjoy!\n")

    def run(self):
        while True:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

            if choice == "off":
                break
            elif choice == "report":
                self.print_report()
            elif choice in self.menu:
                if self.check_resources(choice):
                    payment = self.process_coins()
                    if payment >= self.menu[choice]["cost"]:
                        self.make_coffee(choice, payment)
                    else:
                        print("Sorry, that's not enough money. Money refunded.")
                else:
                    print("Sorry, not enough resources to make the selected drink.")
            else:
                print("Invalid choice. Please select from espresso, latte, cappuccino, or 'off'.")

coffee_machine = CoffeeMachine()
coffee_machine.run()
