a = float(input("Enter first number: "))  #float shows with the decimal point. after the operation is done shows accurate value 
b = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /, %): ")

if operation == '+':
    print("Result:", a + b)
elif operation == '-':
    print("Result:", a - b)
elif operation == '*':
    print("Result:", a * b)
elif operation == '/':
    if b == 0:
        print("Error: Cannot divide by zero")
    else:
        print("Result:", a / b)
elif operation == '%':
    if b == 0:
        print("Error: Cannot modulo by zero")
    else:
        print("Result:", a % b)
else:
    print("Invalid operation")