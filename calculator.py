def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2 

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

continue_calculating = "y"

num1 = float(input("What's the first number?\n"))

while continue_calculating == "y":

  num2 = float(input("What's the second number?\n"))
  for operation in operations:
    print(operation)
  operation_symbol = input("Pick an operation from the line above: ")
  answer = operations[operation_symbol](num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  continue_calculating = input("Type 'y to continue calculating or type 'n' to exit.\n").lower()
  num1 = answer
else:
  print("Goodbye.")
