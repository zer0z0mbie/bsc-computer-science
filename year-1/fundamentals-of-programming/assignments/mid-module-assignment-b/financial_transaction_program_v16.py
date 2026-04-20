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

transactions = dict()

expenses_dict = {"Rent": rent, "Utilities": utilities, "Groceries": groceries, "Other Expenses": other_expenses}

# Functions

def total_income():
    return income

def total_expenses():
    return rent + utilities + groceries + other_expenses

def remaining_balance():
    return total_income() - total_expenses()

def lowest_expense_category(ref_dict):
    return min(ref_dict, key=ref_dict.get)

def highest_expense_category(ref_dict):
    return max(ref_dict, key=ref_dict.get)

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
    payment_id = f"UTID{payment_id_num}"

    dictionary.update({payment_id: {"Category": category, "Date": date, "Amount": amount}})

# Program Body

print("* * * Welcome to the Financial Transaction Program * * *")
print()

while True:

    print(menu)
    menu_option_chosen = input("Please input your selection here: ")
    print()

    try: # Validating menu input to ensure user chooses a valid option
        menu_option_chosen = int(menu_option_chosen)

    except ValueError:
        print("Please select a valid option from 1 to 9")
        print()
        continue

    if menu_option_chosen == 1: # Add transactions
        print(transaction_category_options)

        while True:
            transaction_category_chosen = input("Please input your selection here: ")
            print()

            try: # Validate transaction category chosen
                transaction_category_chosen = int(transaction_category_chosen)

                if transaction_category_chosen in [1, 2, 3, 4, 5]:
                    payment_id_num += 1

                    # Validate day
                    while True:
                        day_chosen = input("Input the day of the month (dd): ")

                        if day_chosen.isdigit():
                            day_int = int(day_chosen)
                            if 1 <= day_int <= 31:
                                break
                            else:
                                print("Please enter a valid day (1-31)")
                        else:
                            print("Please enter numbers only")

                    # Validate month
                    while True:
                        month_chosen = input("Input the month (mm): ")

                        if month_chosen.isdigit():
                            month_int = int(month_chosen)
                            if 1 <= month_int <= 12:
                                break
                            else:
                                print("Please enter a valid month (1-12)")
                        else:
                            print("Please enter numbers only")

                    while True:
                        amount_chosen = input("Enter the amount: ")

                        try:
                            amount_chosen = float(amount_chosen)

                            if amount_chosen < 0:
                                print("Please enter a positive number")
                                continue

                            break

                        except ValueError:
                            print("Please enter a valid number")

                    print()

                    if transaction_category_chosen == 1:
                        add_to_dict(transactions, "Income", day_chosen, month_chosen, amount_chosen)
                        income += amount_chosen

                    elif transaction_category_chosen == 2:
                        add_to_dict(transactions, "Rent", day_chosen, month_chosen, amount_chosen)
                        rent += amount_chosen
                        expenses_dict.update({"Rent": rent})

                    elif transaction_category_chosen == 3:
                        add_to_dict(transactions, "Utilities", day_chosen, month_chosen, amount_chosen)
                        utilities += amount_chosen
                        expenses_dict.update({"Utilities": utilities})

                    elif transaction_category_chosen == 4:
                        add_to_dict(transactions, "Groceries", day_chosen, month_chosen, amount_chosen)
                        groceries += amount_chosen
                        expenses_dict.update({"Groceries": groceries})

                    elif transaction_category_chosen == 5:
                        add_to_dict(transactions, "Other Expenses", day_chosen, month_chosen, amount_chosen)
                        other_expenses += amount_chosen
                        expenses_dict.update({"Other Expenses": other_expenses})

                    break

                else:
                    print("Please choose an option from 1 to 5")
                    print()

            except ValueError:
                print("Please choose an option from 1 to 5")
                print()

    elif menu_option_chosen == 2: # Remove transactions
        if len(transactions) == 0:
            print("No transactions")
            print()

        else:
            transaction_to_delete = input("Please input the transaction you want to remove: ")
            del transactions[transaction_to_delete]
            print()

    elif menu_option_chosen == 3: # View transactions
        if len(transactions) == 0:
            print("No transactions")
            print()

        else:
            print("Transactions:")
            for transaction in transactions:
                data = transactions[transaction]
                print(f"- Transaction ID: {transaction} | Category: {data['Category']} | Date: {data['Date']} | Amount: {data['Amount']:.2f}")
            print()

    elif menu_option_chosen == 4: # View remaining balance
        print(f"Remaining Balance: {remaining_balance():.2f}")
        print()

    elif menu_option_chosen == 5: # View total income
        print(f"Total Income: {total_income():.2f}")
        print()

    elif menu_option_chosen == 6: # View total expenses
        print(f"Total Expenses: {total_expenses():.2f}")
        print()

    elif menu_option_chosen == 7: # View the lowest expense category
        lowest_category = lowest_expense_category(expenses_dict)
        print(f"Lowest Expense Category: {lowest_category} - {expenses_dict[lowest_category]:.2f}")
        print()

    elif menu_option_chosen == 8: # View the highest expense category
        highest_category = highest_expense_category(expenses_dict)
        print(f"Highest Expense Category: {highest_category} - {expenses_dict[highest_category]:.2f}")
        print()

    elif menu_option_chosen == 9: # Exit the program
        print("Thank you for using the Financial Transaction Program")
        break

    else:
        print("Please select a valid option from 1 to 9")
        print()