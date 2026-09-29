import json
import os
from datetime import datetime


DATA_FILE = "atm_data.json"


# LOAD DATA

def load_data():

    if os.path.exists(DATA_FILE):

        with open(DATA_FILE, "r") as file:
            return json.load(file)

    else:

        data = {
            "account": {
                "name": "Subhranjal Malakar",
                "account_number": "1234567890",
                "phone": "9876543210",
                "email": "modibharwa@Gmail.com",
                "balance": 5000.00,
                "pin": "1234",
                "locked": False,
                "transactions": []
            }
        }

        save_data(data)

        return data


# SAVE DATA


def save_data(data):

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ACCOUNT INFORMATION


def show_account_info(account):

    print("\n========== ACCOUNT INFORMATION ==========")

    print(f"Name           : {account['name']}")
    print(f"Account Number : {account['account_number']}")
    print(f"Phone          : {account['phone']}")
    print(f"Email          : {account['email']}")

    print("=========================================")

# CHECK BALANCE


def check_balance(account):

    print(f"\nCurrent Balance: ₹{account['balance']:.2f}")

# DEPOSIT MONEY


def deposit_money(account, data):

    try:
        amount = float(input("Enter deposit amount: ₹"))

        if amount > 0:

            account["balance"] += amount

            transaction = {
                "type": "Deposit",
                "amount": amount,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }

            account["transactions"].append(transaction)

            save_data(data)

            print(f"\n₹{amount:.2f} deposited successfully.")
            print(f"New Balance: ₹{account['balance']:.2f}")

        else:

            print("Invalid deposit amount.")

    except ValueError:

        print("Please enter a valid amount.")

# WITHDRAW MONEY


def withdraw_money(account, data):

    try:

        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:

            print("Invalid withdrawal amount.")

        elif amount > account["balance"]:

            print("Insufficient balance.")

        else:

            account["balance"] -= amount

            transaction = {
                "type": "Withdrawal",
                "amount": amount,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }

            account["transactions"].append(transaction)

            save_data(data)

            print(f"\nPlease collect ₹{amount:.2f}")
            print(f"Remaining Balance: ₹{account['balance']:.2f}")

    except ValueError:

        print("Please enter a valid amount.")


# TRANSACTION HISTORY


def show_transactions(account):

    print("\n========== TRANSACTION HISTORY ==========")

    transactions = account["transactions"]

    if len(transactions) == 0:

        print("No transactions yet.")

    else:

        for transaction in transactions:

            print(
                f"{transaction['date']} | "
                f"{transaction['type']} | "
                f"₹{transaction['amount']:.2f}"
            )

    print("==========================================")


# CHANGE PIN


def change_pin(account, data):

    print("\n========== CHANGE PIN ==========")

    old_pin = input("Enter current PIN: ")

    if old_pin != account["pin"]:

        print("Incorrect current PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():

        print("PIN must contain exactly 4 digits.")
        return

    confirm_pin = input("Confirm new PIN: ")

    if new_pin != confirm_pin:

        print("PINs do not match.")
        return

    if new_pin == old_pin:

        print("New PIN cannot be the same as old PIN.")
        return

    account["pin"] = new_pin

    save_data(data)

    print("PIN changed successfully.")

# ATM MENU


def atm_menu(account, data):

    while True:

        print("\n")
        print("================================")
        print("           ATM MENU")
        print("================================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Account Information")
        print("6. Change PIN")
        print("7. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            check_balance(account)

        elif choice == "2":

            deposit_money(account, data)

        elif choice == "3":

            withdraw_money(account, data)

        elif choice == "4":

            show_transactions(account)

        elif choice == "5":

            show_account_info(account)

        elif choice == "6":

            change_pin(account, data)

        elif choice == "7":

            print("\nThank you for using our ATM!")
            print("Please take your card.")

            break

        else:

            print("Invalid choice. Please try again.")


# LOGIN / PIN VERIFICATION

def login(data):

    account = data["account"]

    # Check whether account is locked

    if account["locked"]:

        print("\n================================")
        print("       ACCOUNT LOCKED")
        print("================================")
        print("Your account is currently locked.")
        print("Please contact the bank.")
        return False

    attempts = 0

    while attempts < 3:

        pin = input("\nEnter your PIN: ")

        if pin == account["pin"]:

            print("\nLogin successful!")
            return True

        else:

            attempts += 1

            print("Incorrect PIN.")

            remaining = 3 - attempts

            if remaining > 0:

                print(f"Attempts remaining: {remaining}")

    # Lock account after 3 failed attempts

    account["locked"] = True

    save_data(data)

    print("\n================================")
    print("       ACCOUNT LOCKED")
    print("================================")
    print("Too many incorrect attempts.")
    print("Your account has been locked.")

    return False


# MAIN PROGRAM

def main():

    data = load_data()

    account = data["account"]

    print("\n================================")
    print("        WELCOME TO ATM")
    print("================================")

    if login(data):

        atm_menu(account, data)


main()
