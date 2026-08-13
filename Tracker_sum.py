def greeting():
    print("Welcome to the Daily Expense Tracker!")
    print()
    print("Menu:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate all expenses")
    print("4. Clear all expenses")
    print("5. Exit")

    expenses = []
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            user_input = float(input("Enter expense: "))
            expenses.append(user_input)
            print("Expense added successfully!")
        elif choice == "2":
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("Your expenses:")
                for i, expense in enumerate(expenses, start=1):
                    print(f"{i}. {expense}")
        elif choice == "3":
            if not expenses:
                print("No expenses recorded yet.")
            else:
                total = sum(expenses)
                average = total / len(expenses)
                print(f"Total expense: {total}")
                print(f"Average expense: {average}")
        elif choice == "4":
            expenses.clear()
            print("All expenses cleared!")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

greeting()