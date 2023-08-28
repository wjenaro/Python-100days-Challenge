def calculator():
  """A simple calculator that asks for two numbers and an operation, and then calculates and prints the answer."""

  first_number = float(input("Enter the first number: "))
  second_number = float(input("Enter the second number: "))
  operation = input("Enter the operation (+, -, *, or /): ")

  if operation == "+":
    answer = first_number + second_number
  elif operation == "-":
    answer = first_number - second_number
  elif operation == "*":
    answer = first_number * second_number
  elif operation == "/":
    answer = first_number / second_number
  else:
    print("Invalid operation.")
    return

  print(f"{first_number} {operation} {second_number} = {answer}")


if __name__ == "__main__":
  calculator()
