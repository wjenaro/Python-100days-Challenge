#You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
#inputs height and width of the walll

def calculate_number_of_cans(width, height) -> float:
    return (width*height)/5
#inputs
w=int(input("Width: "))
#inputs
h=int(input("Height: "))

print(f"You need around {round(calculate_number_of_cans(w,h))} cans")