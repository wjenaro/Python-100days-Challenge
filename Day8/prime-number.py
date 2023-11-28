#Prime numbers are numbers that can only be cleanly divided by themselves and 1.
def is_prime(num):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
          return False

    return True
    

number=int(input("Give a number: "))

number_is_prime=is_prime(number)
if number_is_prime==True:
    print(f"{number}  is prime number")
else:
    print(f"{number} is not prime")
