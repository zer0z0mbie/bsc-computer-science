# Variables

income = 0

rent = 0

utilities = 0

groceries = 0

other_expenses = 0

payment_id_num = 0

menu = """Select an operation:
1. Add Transactions
2. Remove Transactions
3. View Transactions
4. View Remaining Balance
5. View Total Income
6. View Total Expenses
7. View the Lowest Expense Category
8. View the Highest Expense Category
9. Exit"""

transaction_category_options = """Select a category:
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

def add_to_dict(dictionary, category, day, month, amount):
    """
    This function adds transactions to the data structure.
    """
    if len(day) == 1: # Formats the day to dd in case user inputs d instead of dd.
        day = f"0{day}"
    if len(month) == 1: # Formats the month to mm in case user inputs m instead of mm.
        month = f"0{month}"

    date = f"{day}/{month}"
    amount = float(amount)
    payment_id = f"UTID_{payment_id_num}"

    return dictionary.update({payment_id: {"Category": category, "Date": date, "Amount": amount}})

# Program Body

print("* * * Welcome to the Financial Transaction Program * * *")
print()

while True:

    print(menu)
    menu_option_chosen = input("Please input your selection here: ")
    print()

    if int(menu_option_chosen) == 1: # Add transactions
        print(transaction_category_options)
        transaction_category_chosen = input("Please input your selection here: ")
        print()

        if int(transaction_category_chosen) in [1, 2, 3, 4, 5]:
            payment_id_num += 1
            day_chosen = input("Input the day of the month (dd): ")
            month_chosen = input("Input the month (mm): ")
            amount_chosen = input("Enter the amount: ")
            print()

            if int(transaction_category_chosen) == 1:
                add_to_dict(transactions, "Income", day_chosen, month_chosen, amount_chosen)
                income += float(amount_chosen)

            elif int(transaction_category_options) == 2:
                add_to_dict(transactions, "Rent", day_chosen, month_chosen, amount_chosen)
                rent += float(amount_chosen)

            elif int(transaction_category_chosen) == 3:
                add_to_dict(transactions, "Utilities", day_chosen, month_chosen, amount_chosen)
                utilities += float(amount_chosen)

            elif int(transaction_category_options) == 4:
                add_to_dict(transactions, "Groceries", day_chosen, month_chosen, amount_chosen)
                groceries += float(amount_chosen)

            elif int(transaction_category_chosen) == 5:
                add_to_dict(transactions, "Other Expenses", day_chosen, month_chosen, amount_chosen)
                other_expenses += float(amount_chosen)

        else:
            print("Invalid operation")

    elif int(menu_option_chosen) == 2: # Remove transactions
        pass

    elif int(menu_option_chosen) == 3: # View transactions
        pass

    elif int(menu_option_chosen) == 4: # View remaining balance
        print(remaining_balance())
        print()

    elif int(menu_option_chosen) == 5: # View total income
        print(total_income())
        print()

    elif int(menu_option_chosen) == 6: # View total expenses
        print(total_expenses())
        print()

    elif int(menu_option_chosen) == 7: # View the lowest expense category
        print(lowest_expense_category())
        print()

    elif int(menu_option_chosen) == 8: # View the highest expense category
        print(highest_expense_category())
        print()

    elif int(menu_option_chosen) == 9: # Exit the program
        print("Thank you for using the Financial Transaction Program.")
        break

    else:
        print("Invalid operation")
        print()