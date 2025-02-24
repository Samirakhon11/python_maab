import json
import random
import os

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} was added to your balance"
        else:
            return f"Please, enter a valid amount to add"
        
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            return f"{amount} was withdrown from your account. Your currect balance is: {self.balance - amount}"
        elif amount < self.balance:
            return f"There is no enough money. Your balance is {self.balance}"
        else:
            return "Please, enter a valid amount to withdraw"
        
    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

class Bank:
    def __init__(self, filename = 'accounts.json'):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()

    def generate_account_number(self):
        while True:
            acc_num = random.randint(1000, 9999)
            if acc_num not in self.accounts:
                return acc_num
 
    def create_account(self, name, initial_deposit):
        account_number = self.generate_account_number()
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        return account_number
    
    def view_account(self, account_number):
        return self.accounts.get(account_number)
    
    def deposit(self, account_number, amount):
        account = self.view_account(account_number)
        if account and account.deposit(amount):
            self.save_to_file()
            return True
        return False
    
    def withdraw(self, account_number, amount):
        account = self.view_account(account_number)
        if account and account.withdraw(amount):
            self.save_to_file()
            return True
        return False
    
    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump({num: acc.to_dict() for num, acc in self.accounts.items()}, file)
    
    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    data = json.load(file)
                    self.accounts = {int(num): Account(**acc) for num, acc in data.items()}
                except json.JSONDecodeError:
                    self.accounts = {}

if __name__ == "__main__":
    bank = Bank()
    
    while True:
        print("\nWelcome to the Bank!")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            acc_num = bank.create_account(name, initial_deposit)
            print(f"Account created successfully! Your account number is {acc_num}.")
        
        elif choice == "2":
            acc_num = int(input("Enter your account number: "))
            account = bank.view_account(acc_num)
            if account:
                print(f"Account Number: {account.account_number}\nName: {account.name}\nBalance: ${account.balance}")
            else:
                print("Account not found!")
        
        elif choice == "3":
            acc_num = int(input("Enter your account number: "))
            amount = float(input("Enter deposit amount: "))
            if bank.deposit(acc_num, amount):
                print("Deposit successful!")
            else:
                print("Invalid deposit amount!")
        
        elif choice == "4":
            acc_num = int(input("Enter your account number: "))
            amount = float(input("Enter withdrawal amount: "))
            if bank.withdraw(acc_num, amount):
                print("Withdrawal successful!")
            else:
                print("Invalid withdrawal amount or insufficient funds!")
        
        elif choice == "5":
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice, please try again.")
