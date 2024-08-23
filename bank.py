#Import Necessary modules to run the code:

import csv
import datetime

#python code to define class for bank Account

class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount} on {datetime.date.today()}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount} on {datetime.date.today()}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")

    def view_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

#python code to implement the main Program

def main():
    accounts = []

    def create_account():
        account_number = input("Enter account number: ")
        name = input("Enter account holder name: ")
        accounts.append(BankAccount(account_number, name))
        print("Account created successfully!")

    def view_accounts():
        for account in accounts:
            print(f"Account Number: {account.account_number}, Name: {account.name}")

    def find_account():
        account_number = input("Enter account number: ")
        for account in accounts:
            if account.account_number == account_number:
                return account
        print("Account not found.")

    def transaction():
        account = find_account()
        if account:
            choice = input("1. Deposit\n2. Withdraw\n3. Check Balance\n4. View Transaction History\nChoose: ")
            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == '3':
                account.check_balance()
            elif choice == '4':
                account.view_transaction_history()
            else:
                print("Invalid choice.")

    while True:
        print("\n1. Create Account\n2. View Accounts\n3. Transaction\n4. Exit\nChoose: ")
        choice = input()

        if choice == '1':
            create_account()
        elif choice == '2':
            view_accounts()
        elif choice == '3':
            transaction()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
