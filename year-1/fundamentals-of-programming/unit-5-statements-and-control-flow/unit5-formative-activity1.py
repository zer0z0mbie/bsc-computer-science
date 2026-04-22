"""
Variable and Control Flow Exercise: Age Checker

Task: Write a program that asks the user to input their age. The program should print
"You are a minor" if the age is under 18.
"You are an adult" if the age is 18 or above.
"""

age = int(input("What is your age? "))

if age < 18:
    print("You are a minor")
else:
    print("You are an adult")
