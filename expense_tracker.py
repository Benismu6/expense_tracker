def add_expense(expenses, amount, category):
    """
    Adds a new expense to the list of expenses.

    Args:
        expenses (list): The list of expenses.
        amount (float): The amount of the expense.
        category (str): The category of the expense.
    """
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    """
    Prints all expenses in the provided list.

    Args:
        expenses (list): The list of expenses.
    """
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    """
    Calculates the total expenses from the provided list.

    Args:
        expenses (list): The list of expenses.

    Returns:
        float: The total expenses.
    """
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    """
    Filters expenses by category from the provided list.

    Args:
        expenses (list): The list of expenses.
        category (str): The category to filter by.

    Returns:
        filter: Filtered expenses by category.
    """
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    """
    Main function to interact with the expense tracker.
    """
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
        elif choice == '5':
            print('Exiting the program.')
            break

if __name__ == '__main__':
    main()

