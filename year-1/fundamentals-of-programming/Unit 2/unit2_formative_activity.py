"""
Task
Create a basic calculator program that allows the user to choose between addition, subtraction, multiplication, and division.

Implement a menu system to select the operation.

Each operation should be implemented as its own function (e.g., add(), subtract(), and so on).

Outcome
Students will learn to abstract repeated logic into functions, making their code more modular and reusable.
"""

# Functions:

def add(num1, num2):
    """
    Adds two numbers.
    """
    return num1 + num2

def sub(num1, num2):
    """
    Subtracts two numbers.
    """
    return num1 - num2

def mult(num1, num2):
    """
    Multiplies two numbers.
    """
    return num1 * num2

def div(num1, num2):
    """
    Divides two numbers.
    """
    return num1 / num2

# Menu:

print("""
Please choose an operation:
1. Addition -> Type A
2. Subtraction -> Type S
3. Multiplication -> Type M
4. Division -> Type D
""")

# Prompting the user for information:

operation = input("Please enter your choice: ")
num1 = int(input("Type the first number: "))
num2 = int(input("Type the second number: "))

# Conditionals based on the operation chosen:

if operation.upper() == "A":
    result = add(num1, num2)
    operation_sign = "+"
elif operation.upper() == "S":
    result = sub(num1, num2)
    operation_sign = "-"
elif operation.upper() == "M":
    result = mult(num1, num2)
    operation_sign = "*"
elif operation.upper() == "D":
    result = div(num1, num2)
    operation_sign = "/"
else:
    print("Invalid operation.")
    exit()

# Output:

print(f"\nResult of {num1} {operation_sign} {num2}: {result}")

