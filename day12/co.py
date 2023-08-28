class CoffeeMachine:
    def __init__(self):
        self.resources = {
            'water': 300,
            'milk': 200,
            'coffee': 100,
            'money': 0,
        }
        self.menu = {
            'espresso': {'water': 50, 'milk': 0, 'coffee': 18, 'cost': 1.5},
            'latte': {'water': 200, 'milk': 150, 'coffee': 24, 'cost': 2.5},
            'cappuccino': {'water': 250, 'milk': 100, 'coffee': 24, 'cost': 3.0},
        }

    def report(self):
        print("Water: {}ml".format(self.resources['water']))
        print("Milk: {}ml".format(self.resources['milk']))
        print("Coffee: {}g".format(self.resources['coffee']))
        print("Money: ${:.2f}".format(self.resources['money']))

    def check_resources(self, choice):
        for item, amount in self.menu[choice].items():
            if item != 'cost' and self.resources[item] < amount:
                print("Sorry, there is not enough {}.".format(item))
                return False
        return True

    def process_coins(self, cost):
        print("Please insert coins.")
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        total_inserted = quarters + dimes + nickels + pennies
        if total_inserted < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return 0
        elif total_inserted > cost:
            change = total_inserted - cost
            print("Here is ${:.2f} dollars in change.".format(change))
            return cost
        else:
            return cost

    def make_coffee(self, choice, cost):
        print("Making your {}. Please wait...".format(choice))
        for item, amount in self.menu[choice].items():
            if item != 'cost':
                self.resources[item] -= amount
        self.resources['money'] += cost
        print("Here is your {}. Enjoy!".format(choice))

    def run(self):
        while True:
            user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

            if user_choice == 'off':
                break
            elif user_choice == 'report':
                self.report()
            elif user_choice in self.menu:
                if self.check_resources(user_choice):
                    cost = self.menu[user_choice]['cost']
                    payment = self.process_coins(cost)
                    if payment > 0:
                        self.make_coffee(user_choice, payment)
            else:
                print("Invalid choice. Please select from espresso, latte, cappuccino, or off.")


coffee_machine = CoffeeMachine()
coffee_machine.run()
