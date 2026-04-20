
"""
--- Program Overview ---

This program is a console-based finance tracker that allows users to manage income and expenses, store transactions, and view financial summaries such as total income, total expenses, remaining balance, and spending categories.


--- Section 1: Variables, Data Structures, and Functions ---

1) Variables:
    This section includes the main global variables used in the program:
        1.1) program_name: stores the name of the program.
        1.2) income*: stores the total income.
        1.3) Expense variables*:
            1.3.1) rent: stores the total rent.
            1.3.2) utilities: stores the total utilities.
            1.3.3) groceries: stores the total groceries.
            1.3.4) other_expenses: stores the total amount for other expenses.
        1.4) payment_id_num: stores the payment ID number, used to generate unique payment IDs.
        1.5) menu**: stores the menu options, which are:
            1.5.1) Option 1 - Add Transactions: adds transactions.
                   Option 2 - Remove Transactions: removes transactions.
                   Option 3 - View/Filter Transactions: views or filters transactions.
                   Option 4 - View Remaining Balance: displays the remaining balance.
                   Option 5 - View Total Income: displays the total income.
                   Option 6 - View Total Expenses: displays the total expenses.
                   Option 7 - View the Lowest Expense Category: displays the lowest expense category.
                   Option 8 - View the Highest Expense Category: displays the highest expense category.
                   Option 9 - Exit: exits the program.
        1.6) transaction_category_options**: stores the transaction category options, which are:
            1.6.1) Option 1 - Income: transactions related to income.
                   Option 2 - Rent: transactions related to rent.
                   Option 3 - Utilities: transactions related to utilities.
                   Option 4 - Groceries: transactions related to groceries.
                   Option 5 - Other Expenses: transactions related to expenses not included in the main categories above.

    * Please note that the income and expense variables are updated whenever users add or remove transactions.
    ** Please note that the menu and transaction_category_options variables are created for reuse and future scalability.


2) Data Structures:
    This section includes the data structures used in the program:
        2.1) transactions: a dictionary used to store all user-input transactions.
             This allows fast access, addition, and removal using a unique payment ID.
        2.2) expenses_dict: a dictionary containing only expense categories and their totals.
             This is used to efficiently determine the lowest and highest expense categories.


3) Functions:
    This section includes the functions used in the program:
        3.1) total_income(): returns the total income.
        3.2) total_expenses(): returns the total expenses (rent + utilities + groceries + other_expenses).
        3.3) remaining_balance(): returns the remaining balance (total_income() - total_expenses()).
        3.4) lowest_expense_category(ref_dict): returns the category with the lowest expense.
        3.5) highest_expense_category(ref_dict): returns the category with the highest expense.
        3.6) add_to_dict(dictionary, payment_id, category, day, month, amount): adds a new transaction and formats the date as dd/mm.
        3.7) filter_transactions(transactions, selected_category): displays transactions filtered by a selected category (e.g., "Rent").


--- Section 2: Program Body ---

4) Welcome Message:
    Displays a welcome message to the user.

5) Transaction Operation:
    Prompts the user to select an operation:
        5.1) Option 1 - Add Transactions
             Option 2 - Remove Transactions
             Option 3 - View/Filter Transactions
             Option 4 - View Remaining Balance
             Option 5 - View Total Income
             Option 6 - View Total Expenses
             Option 7 - View the Lowest Expense Category
             Option 8 - View the Highest Expense Category
             Option 9 - Exit

6) Add Transactions:
    Adds transactions based on five categories:
        6.1) Option 1 - Income
             Option 2 - Rent
             Option 3 - Utilities
             Option 4 - Groceries
             Option 5 - Other Expenses

    After selecting a category, the program prompts for the day, month, and amount.
    A unique payment ID is generated, and the transaction is added to the transactions dictionary.

7) Remove Transactions:
    Removes a transaction using its ID.
    If the transaction exists, it is removed; otherwise, a "Transaction not found" message is displayed.

8) View/Filter Transactions:
    Options:
        - view all transactions, or
        - filter transactions by category.

    If "View All" is selected, all transactions are displayed.
    If filtering is selected, the user is prompted to choose a category (e.g., "Rent").

9) View Remaining Balance:
    Displays the remaining balance (total income minus total expenses).

10) View Total Income:
    Displays the total income.

11) View Total Expenses:
    Displays the total expenses.

12) View the Lowest Expense Category:
    Displays the lowest expense category and its amount.

13) View the Highest Expense Category:
    Displays the highest expense category and its amount.

14) Exit the Program:
    Exits the program.
"""

# ------ Variables, Data Structures, and Functions ------ #

# --- 1. Variables --- #

program_name = "Hamm Finance Life"
income = 0
rent = 0
utilities = 0
groceries = 0
other_expenses = 0
payment_id_num = 0

menu = """[1] Add Transactions
[2] Remove Transactions
[3] View/Filter Transactions
[4] View Remaining Balance
[5] View Total Income
[6] View Total Expenses
[7] View the Lowest Expense Category
[8] View the Highest Expense Category
[9] Exit"""

transaction_category_options = """[1] Income
[2] Rent
[3] Utilities
[4] Groceries
[5] Other Expenses"""

# --- 2. Data Structures --- #

transactions = dict()
expenses_dict = {"Rent": rent, "Utilities": utilities, "Groceries": groceries, "Other Expenses": other_expenses}

# --- 3. Functions --- #

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


def add_to_dict(dictionary, payment_id, category, day, month, amount):
    day = str(day)
    month = str(month)

    # Formats the day to dd in case user inputs d instead of dd
    if len(day) == 1:
        day = f"0{day}"

    # Formats the month to mm in case user inputs m instead of mm
    if len(month) == 1:
        month = f"0{month}"

    # Formats the date to dd/mm
    date = f"{day}/{month}"

    dictionary.update({payment_id: {"Category": category, "Date": date, "Amount": amount}})


def filter_transactions(transactions, selected_category):
    print()
    print(f"Transactions for {selected_category}:")
    found = False

    for transaction in transactions:
        data = transactions[transaction]

        if data["Category"] == selected_category:
            print(f"- Transaction ID: {transaction} | Date: {data['Date']} | Amount: {data['Amount']:.2f}")
            found = True

    if not found:
        print("No transactions in this category")

    print()

# ------ Program Body ------ #

# --- 4. Welcome Message --- #

print(f"* * * Welcome to {program_name} * * *")
print()

# --- 5. Transaction Operation --- #

while True:
    # Prompts the user to input an operation
    print("Select an operation:")
    print(menu)
    menu_option_chosen = input("Please input your selection here: ")
    print()

    # Validate menu input
    try:
        menu_option_chosen = int(menu_option_chosen)

    except ValueError:
        print("Please select a valid option from 1 to 9")
        print()
        continue

    # --- 6. Add Transactions --- #

    if menu_option_chosen == 1:
        print("Select a category:")
        print(transaction_category_options)

        while True:
            transaction_category_chosen = input("Please input your selection here: ")
            print()

            # Validate transaction category chosen
            try:
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

                            # Else statement in case the user enters an invalid day
                            else:
                                print("Please enter a valid day (1-31)")

                        # Else statement in case the user does not enter numbers
                        else:
                            print("Please enter numbers only")

                    # Validate month
                    while True:
                        month_chosen = input("Input the month (mm): ")

                        if month_chosen.isdigit():
                            month_int = int(month_chosen)

                            if 1 <= month_int <= 12:
                                break

                            # Else statement in case the user enters an invalid month
                            else:
                                print("Please enter a valid month (1-12)")

                        # Else statement in case the user does not enter numbers
                        else:
                            print("Please enter numbers only")

                    # Validate amount
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

                    payment_id = f"UTID{payment_id_num}"

                    if transaction_category_chosen == 1:
                        add_to_dict(transactions, payment_id, "Income", day_chosen, month_chosen, amount_chosen)
                        income += amount_chosen

                    elif transaction_category_chosen == 2:
                        add_to_dict(transactions, payment_id, "Rent", day_chosen, month_chosen, amount_chosen)
                        rent += amount_chosen
                        expenses_dict.update({"Rent": rent})

                    elif transaction_category_chosen == 3:
                        add_to_dict(transactions, payment_id, "Utilities", day_chosen, month_chosen, amount_chosen)
                        utilities += amount_chosen
                        expenses_dict.update({"Utilities": utilities})

                    elif transaction_category_chosen == 4:
                        add_to_dict(transactions, payment_id, "Groceries", day_chosen, month_chosen, amount_chosen)
                        groceries += amount_chosen
                        expenses_dict.update({"Groceries": groceries})

                    elif transaction_category_chosen == 5:
                        add_to_dict(transactions, payment_id, "Other Expenses", day_chosen, month_chosen, amount_chosen)
                        other_expenses += amount_chosen
                        expenses_dict.update({"Other Expenses": other_expenses})

                    break

                # Else statement in case the user selects an invalid transaction category option
                else:
                    print("Please choose an option from 1 to 5")
                    print()

            except ValueError:
                print("Please choose an option from 1 to 5")
                print()

    # --- 7. Remove Transactions --- #

    elif menu_option_chosen == 2:
        # If statement in case the transactions dictionary is empty
        if len(transactions) == 0:
            print("No transactions")
            print()

        else:
            # upper() method called in case the user inputs the transaction id in lowercase
            transaction_to_delete = input("Please input the transaction you want to remove: ").upper()
            print()

            if transaction_to_delete in transactions:
                data = transactions[transaction_to_delete]
                amount = data["Amount"]
                category = data["Category"]

                if category == "Income":
                    income -= amount

                elif category == "Rent":
                    rent -= amount
                    expenses_dict["Rent"] = rent

                elif category == "Utilities":
                    utilities -= amount
                    expenses_dict["Utilities"] = utilities

                elif category == "Groceries":
                    groceries -= amount
                    expenses_dict["Groceries"] = groceries

                elif category == "Other Expenses":
                    other_expenses -= amount
                    expenses_dict["Other Expenses"] = other_expenses

                del transactions[transaction_to_delete]
                print(f"Transaction {transaction_to_delete} removed successfully")
                print()

            # Else statement in case the transaction does not exist
            else:
                print("Transaction not found")
                print()

    # --- 8. View/Filter Transactions --- #

    elif menu_option_chosen == 3:
        while True:
            # If statement in case the transactions dictionary is empty
            if len(transactions) == 0:
                print("No transactions")
                print()

                break

            else:
                print("[1] View All")
                print("[2] Filter by Category")
                view_or_filter = input("Please input your selection here: ")
                print()

                try:
                    view_or_filter = int(view_or_filter)

                except ValueError:
                    print("Please choose either 1 or 2")
                    print()
                    continue

                if view_or_filter == 1:
                    print("Transactions:")

                    for transaction in transactions:
                        data = transactions[transaction]
                        print(
                            f"- Transaction ID: {transaction} | Category: {data['Category']} | Date: {data['Date']} | Amount: {data['Amount']:.2f}")
                    print()

                    break

                elif view_or_filter == 2:
                    print("Select a category:")
                    print(transaction_category_options)
                    transaction_to_filter = input("Please input your selection here: ")

                    try:
                        transaction_to_filter = int(transaction_to_filter)

                    except ValueError:
                        print("Please choose an option from 1 to 5")
                        print()
                        continue

                    if transaction_to_filter == 1:
                        filter_transactions(transactions, "Income")

                    elif transaction_to_filter == 2:
                        filter_transactions(transactions, "Rent")

                    elif transaction_to_filter == 3:
                        filter_transactions(transactions, "Utilities")

                    elif transaction_to_filter == 4:
                        filter_transactions(transactions, "Groceries")

                    elif transaction_to_filter == 5:
                        filter_transactions(transactions, "Other Expenses")

                    break

                # Else statement in case the user enters an invalid option
                else:
                    print("Please choose either 1 or 2")
                    print()

    # --- 9. View Remaining Balance --- #

    elif menu_option_chosen == 4:
        print(f"Remaining Balance: {remaining_balance():.2f}")
        print()

    # --- 10. View Total Income --- #

    elif menu_option_chosen == 5:
        print(f"Total Income: {total_income():.2f}")
        print()

    # --- 11. View Total Expenses --- #

    elif menu_option_chosen == 6:
        print(f"Total Expenses: {total_expenses():.2f}")
        print()

    # --- 12. View the Lowest Expense Category --- #

    elif menu_option_chosen == 7:
        lowest_category = lowest_expense_category(expenses_dict)
        print(f"Lowest Expense Category: {lowest_category} | Amount: {expenses_dict[lowest_category]:.2f}")
        print()

    # --- 13. View the Highest Expense Category --- #

    elif menu_option_chosen == 8:
        highest_category = highest_expense_category(expenses_dict)
        print(f"Highest Expense Category: {highest_category} | Amount: {expenses_dict[highest_category]:.2f}")
        print()

    # --- 14. Exit the Program --- #

    elif menu_option_chosen == 9:
        print(f"Thank you for using {program_name}")

        break

    # Else statement in case the user selects an invalid menu option
    else:
        print("Please select a valid option from 1 to 9")
        print()
