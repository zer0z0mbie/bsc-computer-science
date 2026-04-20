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

income = 0

# Expenses Variables

rent = 0
utilities = 0
groceries = 0
other_expense = 0

# Other Variables

user_finished = False
payment_id_num = 0

# Data Structures

transactions_dict = dict()

# Functions

def total_income():
    return income

def total_expenses():
    return rent + utilities + groceries + other_expense

def remaining_balance():
    return total_income() - total_expenses()

def lowest_expense_category(category):
    pass

def highest_expense_category(category):
    pass

def generate_unique_payment_id():
    """
    This function generates unique payment ids, which are used as key in the respective dictionaries.
    """
    return f"UTID_{payment_id_num}"


def add_to_dict(payment_id, category, date, amount):
    """
    This function adds values to the respective dictionaries.
    """
    return transactions_dict.update({payment_id: {"Category": category, "Date": date, "Amount": amount}})

def day_month_format(day, month):
    """
    This function formats the date.
    """
    if len(day) == 1:
        day = f"0{day}"
    if len(month) == 1:
        month = f"0{month}"
    return f"{day}/{month}"

# Program Body

print("* * * Welcome to the Financial Transaction Program * * *")

while not user_finished:
    category_chosen = input(
"""Select a category:
1. Wages                4. Utilities
2. Passive income       5. Groceries
3. Rent                 6. Other Expense
Input your selection here: """)

    if int(category_chosen) in [1, 2, 3, 4, 5, 6]:
        day_chosen = input("Input the day of the month (dd): ")
        month_chosen = input("Input the month (mm): ")
        date_chosen = day_month_format(day_chosen, month_chosen)
        amount_chosen = input("Enter an amount: ")

        if int(category_chosen) == 1:
            amount_chosen = float(amount_chosen)
            payment_id_num += 1
            unique_payment_id = generate_unique_payment_id()
            add_to_dict(unique_payment_id, "Income", date_chosen, amount_chosen)
            amount_chosen += income

    else:
        print("Invalid operation")
        break








































