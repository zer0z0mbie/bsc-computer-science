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

# Income Variables

wages = 0
passive_income = 0

# Expenses Variables

rent = 0
utilities = 0
groceries = 0
other_expense = 0

# Other Variables

user_finished = False
category_message = """Select a category:
1. Wages                4. Utilities
2. Passive income       5. Groceries
3. Rent                 6. Other Expense
Input your selection here: """
payment_id_num = 0

# Data Structures

wages_dict = dict()
passive_income_dict = dict()
rent_dict = dict()
utilities_dict = dict()
groceries_dict = dict()
other_expense_dict = dict()

# Functions

def total_income():
    return wages + passive_income

def total_expenses():
    return rent + utilities + groceries + other_expense

def remaining_balance():
    return total_income() - total_expenses()

def lowest_expense_category():
    pass

def highest_expense_category():
    pass

def generate_unique_payment_id(category):
    """
    This function generates unique payment ids, which are used as key in the respective dictionaries.
    """
    if category == wages_dict:
        return f"WUID{payment_id_num}"
    elif category == passive_income_dict:
        return f"PUID{payment_id_num}"
    elif category == rent_dict:
        return f"RUID{payment_id_num}"
    elif category == utilities_dict:
        return f"UUID{payment_id_num}"
    elif category == groceries_dict:
        return f"GUID{payment_id_num}"
    elif category == other_expense_dict:
        return f"OUID{payment_id_num}"
    else:
        return "Operation invalid"

def add_to_dict(dict_selected, payment_id, date, amount):
    """
    This function adds values to the respective dictionaries.
    """
    return dict_selected.update({payment_id: (date, amount)})

def view_transactions(dict_selected):
    print(f"Transactions: {dict_selected}")

# Program Body

print("* * * Welcome to the Financial Transaction Program * * *")

while not user_finished:

    category_chosen = input(category_message)
    date_chosen = input("Input the date in the format dd/mm: ")
    amount_chosen = input("Enter an amount: ")

    if int(category_chosen) == 1:
        amount_chosen = float(amount_chosen)
        payment_id_num += 1
        unique_payment_id = generate_unique_payment_id(wages_dict)
        add_to_dict(wages_dict, unique_payment_id, date_chosen, amount_chosen)
        wages += amount_chosen

    elif int(category_chosen) == 2:
        amount_chosen = float(amount_chosen)
        payment_id_num += 1
        unique_payment_id = generate_unique_payment_id(passive_income_dict)
        add_to_dict(passive_income_dict, unique_payment_id, date_chosen, amount_chosen)
        passive_income += amount_chosen

    elif int(category_chosen) == 3:
        payment_id_num += 1
        unique_payment_id = generate_unique_payment_id(rent_dict)
        add_to_dict(rent_dict, unique_payment_id, date_chosen, amount_chosen)
        rent += amount_chosen

    elif int(category_chosen) == 4:
        payment_id_num += 1
        unique_payment_id = generate_unique_payment_id(utilities_dict)
        add_to_dict(utilities_dict, unique_payment_id, date_chosen, amount_chosen)
        utilities += amount_chosen


    elif int(category_chosen) == 5:
        payment_id_num += 1
        unique_payment_id = generate_unique_payment_id(groceries_dict)
        add_to_dict(groceries_dict, unique_payment_id, date_chosen, amount_chosen)
        groceries += amount_chosen

    elif int(category_chosen) == 6:
        payment_id_num += 1
        unique_payment_id = generate_unique_payment_id(other_expense_dict)
        add_to_dict(other_expense_dict, unique_payment_id, date_chosen, amount_chosen)
        other_expense += amount_chosen

    else:
        print("Invalid operation")





































