def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def percentage(a,b):
    return a*100 /b
def divide(a, b): 
    if b != 0:
      return a / b
    if b == 0:
      print("Error: Cannot divide by zero!")
print("Simple Calculator")
print("Choose operation: +, -, *, /, %")
operation = input("Enter operation: ")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
if operation == '+':
    print("Result:", add(x, y))
elif operation == '-':
    print("Result:", subtract(x, y))
elif operation == '*':
    print("Result:", multiply(x, y))
elif operation == '%':
    print("Result:", percentage(x, y),"%")
elif operation == '/':
    print("Result:", divide(x, y))
elif operation == '/' and y == 0:
    print("Error: Cannot divide by zero!")
else:
    print("Invalid operation")

