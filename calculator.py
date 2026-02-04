def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations: + (add), - (subtract), * (multiply), / (divide)")
    print("-" * 40)

    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Error: Invalid operation.")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()

