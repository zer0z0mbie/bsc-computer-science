"""
1. Program Requirements:

a. Create a Python program that allows a user to track income and expenses.
b. Use variables to represent income sources and different expense categories (e.g., rent, groceries, utilities).
c. Implement control flow to allow the user to add, view, or delete transactions.
d. Design functions to calculate:
    • Total income and total expenses.
    • Remaining balance (total income - total expenses).
    • Highest and lowest expense categories.
e. Store transactions in a data structure (e.g., list of dictionaries) that includes details like amount, category, and date.

2. Example Program Flow:

a. Prompt the user to enter an income or expense amount, select a category, and input the date.
b. Display a summary of all transactions and the remaining balance.
c. Allow the user to view all income and expense entries or filter by category.
3. Submission Requirements:

a. Provide the Python code with comments explaining each section.
b. Write a short description (150 words) explaining the approach taken to model the transactions and handle calculations.
c. Include screenshots or a sample output showing the program in action.
"""

# Input Variables

active_income = 0
passive_income = 0

# Output Variables

rent = 0
utilities = 0
groceries = 0
other_expense = 0

# Other Variables

user_finished = False

category_message = """Select a category:
1. Active income        4. Utilities 
2. Passive income       5. Groceries
3. Rent                 6. Other Expense
Input your selection here: """

# Data Structures

income_dict = dict()
expenses_dict = dict()

# Functions

def total_income():
    return active_income + passive_income

def total_expenses():
    return rent + utilities + groceries + other_expense

def remaining_balance():
    return total_income() - total_expenses()

def lowest_expense_category():
    pass

def highest_expense_category():
    pass

def add_to_dict(dict_selected, category, date, amount):
    return dict_selected.update({category: (date, amount)})

# Program Body

print("* * * Welcome to the Financial Transaction Program * * *")

while not user_finished:

    amount_chosen = input("Enter an amount: ")
    category_chosen = input(category_message)
    date_chosen = input("Input the date in the format dd/mm: ")

    if int(category_chosen) == 1:
        add_to_dict(income_dict, "Active Income", date_chosen, amount_chosen)

    else:
        print("Invalid operation")


    #question = input("Are you finished? 'Y' or 'N': ").upper()

    #if question == "Y":
     #   break





































