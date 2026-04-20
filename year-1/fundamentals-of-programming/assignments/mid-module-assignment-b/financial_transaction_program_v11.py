# Variables

income = 0

rent = 0

utilities = 0

groceries = 0

other_expenses = 0

payment_id_num = 0

menu = """Select an option:
1. Add transactions
2. Remove transactions
3. View transactions
4. View remaining balance
5. View the lowest expense category
6. View the highest expense category
7. Exit"""

transaction_options = """Select a category:
1. Income
2. Rent
3. Utilities
4. Groceries
5. Other Expenses"""

# Data Structures

expenses_list = [rent, utilities, groceries, other_expenses]

transactions = dict()

# Functions

def total_income():
    return income

def total_expenses():
    return rent + utilities + groceries + other_expenses

def remaining_balance():
    return total_income() - total_expenses()

def lowest_expense_category():
    expenses_list.sort()
    return expenses_list[0]

def highest_expense_category():
    expenses_list.sort()
    return expenses_list[-1]

def add_to_dict(category, day, month, amount):
    """
    This function adds values to the transactions dictionary.
    """
    if len(day) == 1:
        day = f"0{day}"
    if len(month) == 1:
        month = f"0{month}"

    date = f"{day}/{month}"
    amount = float(amount)
    payment_id = f"UTID_{payment_id_num}"

    return transactions.update({payment_id: {"Category": category, "Date": date, "Amount": amount}})

# Program Body

print("* * * Welcome to the Financial Transaction Program * * *")

print(menu)
menu_option_chosen = input("Please input your selection here: ")

if int(menu_option_chosen) == 1: # Add transactions
    print(transaction_options)
    category_chosen = input("Please input your selection here: ")

    if int(category_chosen) in [1, 2, 3, 4, 5]:
        payment_id_num += 1
        day_chosen = input("Input the day of the month (dd): ")
        month_chosen = input("Input the month (mm): ")
        amount_chosen = input("Enter an amount: ")

        if int(category_chosen) == 1:
            add_to_dict("Income", day_chosen, month_chosen, amount_chosen)
            income += float(amount_chosen)

        elif int(category_chosen) == 2:
            add_to_dict("Rent", day_chosen, month_chosen, amount_chosen)
            rent += float(amount_chosen)

        elif int(category_chosen) == 3:
            add_to_dict("Utilities", day_chosen, month_chosen, amount_chosen)
            utilities += float(amount_chosen)

        elif int(category_chosen) == 4:
            add_to_dict("Groceries", day_chosen, month_chosen, amount_chosen)
            groceries += float(amount_chosen)

        elif int(category_chosen) == 5:
            add_to_dict("Other Expenses", day_chosen, month_chosen, amount_chosen)
            other_expenses += float(amount_chosen)

    else:
        print("Invalid operation")

elif int(menu_option_chosen) == 2: # Remove transactions
    pass

elif int(menu_option_chosen) == 3: # View transactions
    pass

elif int(menu_option_chosen) == 4: # View remaining balance
    print(remaining_balance())

elif int(menu_option_chosen) == 5: # View the lowest expense category
    print(lowest_expense_category())

elif int(menu_option_chosen) == 6: # View the highest expense category
    print(highest_expense_category())

elif int(menu_option_chosen) == 7: # Exit the program
    print("Thank you for using the Financial Transaction Program.")
    exit()

else:
    print("Invalid operation")