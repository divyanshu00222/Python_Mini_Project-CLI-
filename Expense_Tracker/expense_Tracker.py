import csv

FILE = "expenses.csv"

# Initialize file with header if empty
def init_file():
    try:
        with open(FILE, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Category", "Amount"])
    except:
        pass


def add_expense():
    category = input("Category: ")
    amount = input("Amount: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([category, amount])

    print("✅ Expense added!")


def view_expenses():
    print("\n===== EXPENSE REPORT =====")
    with open(FILE, "r") as f:
        for row in csv.reader(f):
            print(row)


def menu():
    init_file()
    while True:
        print("""
1. Add Expense
2. View Expenses
3. Exit
""")
        choice = input("Choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        else:
            break


menu()
