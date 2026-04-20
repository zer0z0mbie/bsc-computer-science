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
user_options = [1, 2, 3, 4, 5, 6]
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

def lowest_expense_category(category):
    pass

def highest_expense_category(category):
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

# Program Body

print("* * * Welcome to the Financial Transaction Program * * *")

while not user_finished:
    category_chosen = input(
"""Select a category:
1. Wages                4. Utilities
2. Passive inco me       5. Groceries
3. Rent                 6. Other Expense
Input your selection here: """)

    if int(category_chosen) in user_options:
        day_chosen = input("Input the day of the month (dd): ")
        if len(day_chosen) == 1: # make a function for this part
            day_chosen = f"0{day_chosen}"
        month_chosen = input("Input the month (mm): ")
        if len(month_chosen) == 1: # make a function for this part
            month_chosen = f"0{month_chosen}"
        date_chosen = f"{day_chosen}/{month_chosen}"
        amount_chosen = input("Enter an amount: ")

        if int(category_chosen) == 1:
            amount_chosen = float(amount_chosen)
            payment_id_num += 1
            unique_payment_id = generate_unique_payment_id(wages_dict)
            add_to_dict(wages_dict, unique_payment_id, date_chosen, amount_chosen)
            amount_chosen += wages

        elif int(category_chosen) == 2:
            amount_chosen = float(amount_chosen)
            payment_id_num += 1
            unique_payment_id = generate_unique_payment_id(passive_income_dict)
            add_to_dict(passive_income_dict, unique_payment_id, date_chosen, amount_chosen)
            amount_chosen += passive_income

        elif int(category_chosen) == 3:
            amount_chosen = float(amount_chosen)
            payment_id_num += 1
            unique_payment_id = generate_unique_payment_id(rent_dict)
            add_to_dict(rent_dict, unique_payment_id, date_chosen, amount_chosen)
            amount_chosen += rent

        elif int(category_chosen) == 4:
            amount_chosen = float(amount_chosen)
            payment_id_num += 1
            unique_payment_id = generate_unique_payment_id(utilities_dict)
            add_to_dict(utilities_dict, unique_payment_id, date_chosen, amount_chosen)
            amount_chosen += utilities

        elif int(category_chosen) == 5:
            amount_chosen = float(amount_chosen)
            payment_id_num += 1
            unique_payment_id = generate_unique_payment_id(groceries_dict)
            add_to_dict(groceries_dict, unique_payment_id, date_chosen, amount_chosen)
            amount_chosen += groceries

        elif int(category_chosen) == 6:
            amount_chosen = float(amount_chosen)
            payment_id_num += 1
            unique_payment_id = generate_unique_payment_id(other_expense_dict)
            add_to_dict(other_expense_dict, unique_payment_id, date_chosen, amount_chosen)
            amount_chosen += other_expense

        print(wages_dict, passive_income_dict, rent_dict, utilities_dict, groceries_dict, other_expense_dict)

    else:
        print("Invalid operation")
        break








































