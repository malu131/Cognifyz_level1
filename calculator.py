def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero."


def modulus(x, y):
    return x % y


def calculator():
    print("Welcome to the Basic Calculator!")

    # Input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Input operator
    operator = input("Enter an operator (+, -, *, /, %): ")

    # Perform calculation based on the operator
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    elif operator == '%':
        result = modulus(num1, num2)
    else:
        return "Error: Invalid operator."

    return f"The result of {num1} {operator} {num2} = {result}"


# Main program
if __name__ == "__main__":
    print(calculator())
