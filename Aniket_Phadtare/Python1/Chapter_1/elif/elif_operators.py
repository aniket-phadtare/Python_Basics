a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Addition:", a + b)

elif op == "-":
    print("Subtraction:", a - b)

elif op == "*":
    print("Multiplication:", a * b)

elif op == "/":
    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")