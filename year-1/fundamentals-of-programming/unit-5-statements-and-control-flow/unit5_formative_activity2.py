"""
Basic Function Exercise: Sum Calculator

Task: Define a function calculate_sum(num1, num2) that takes two numbers as input and returns their sum. Call the function with two values and print the result.
"""

def calculate_sum(num1, num2):
    return num1 + num2

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print(calculate_sum(number1, number2))
