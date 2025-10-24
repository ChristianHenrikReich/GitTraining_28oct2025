"""
Good Code Practices - File 3/10
This file shows good code with some room for improvement in documentation and type hints.
"""

import json
import datetime


class BankAccount:
    """Simple bank account class."""
    
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append({
                'type': 'deposit',
                'amount': amount,
                'timestamp': datetime.datetime.now().isoformat(),
                'new_balance': self.balance
            })
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append({
                'type': 'withdrawal',
                'amount': amount,
                'timestamp': datetime.datetime.now().isoformat(),
                'new_balance': self.balance
            })
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        return self.transaction_history.copy()


class Bank:
    """Bank management system."""
    
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1000
    
    def create_account(self, owner_name, initial_deposit=0):
        account_number = f"ACC{self.next_account_number}"
        self.next_account_number += 1
        
        account = BankAccount(account_number, owner_name, initial_deposit)
        self.accounts[account_number] = account
        
        if initial_deposit > 0:
            account.deposit(initial_deposit)
        
        return account_number
    
    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
    def transfer_money(self, from_account, to_account, amount):
        source = self.get_account(from_account)
        destination = self.get_account(to_account)
        
        if source and destination:
            if source.withdraw(amount):
                destination.deposit(amount)
                return True
        return False
    
    def get_all_accounts(self):
        return list(self.accounts.values())
    
    def save_to_file(self, filename):
        data = {}
        for acc_num, account in self.accounts.items():
            data[acc_num] = {
                'owner_name': account.owner_name,
                'balance': account.balance,
                'transaction_history': account.transaction_history
            }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            for acc_num, acc_data in data.items():
                account = BankAccount(
                    acc_num,
                    acc_data['owner_name'],
                    acc_data['balance']
                )
                account.transaction_history = acc_data['transaction_history']
                self.accounts[acc_num] = account
                
                # Update next account number
                acc_number = int(acc_num[3:])  # Remove 'ACC' prefix
                if acc_number >= self.next_account_number:
                    self.next_account_number = acc_number + 1
                    
        except FileNotFoundError:
            print(f"File {filename} not found")
        except json.JSONDecodeError:
            print(f"Error reading {filename}")


def display_menu():
    print("\n=== Bank Management System ===")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Transfer Money")
    print("6. View Transaction History")
    print("7. List All Accounts")
    print("8. Save Data")
    print("9. Exit")


def main():
    bank = Bank()
    bank.load_from_file("bank_data.json")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")
        
        if choice == '1':
            name = input("Enter account owner name: ")
            try:
                initial_deposit = float(input("Enter initial deposit (0 for none): "))
                if initial_deposit < 0:
                    print("Initial deposit cannot be negative")
                    continue
            except ValueError:
                initial_deposit = 0
            
            account_number = bank.create_account(name, initial_deposit)
            print(f"Account created! Account number: {account_number}")
        
        elif choice == '2':
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                print(f"Current balance: ${account.get_balance():.2f}")
            else:
                print("Account not found")
        
        elif choice == '3':
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                try:
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f}. New balance: ${account.get_balance():.2f}")
                    else:
                        print("Invalid deposit amount")
                except ValueError:
                    print("Please enter a valid number")
            else:
                print("Account not found")
        
        elif choice == '4':
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):
                        print(f"Withdrew ${amount:.2f}. New balance: ${account.get_balance():.2f}")
                    else:
                        print("Insufficient funds or invalid amount")
                except ValueError:
                    print("Please enter a valid number")
            else:
                print("Account not found")
        
        elif choice == '5':
            from_acc = input("Enter source account number: ")
            to_acc = input("Enter destination account number: ")
            try:
                amount = float(input("Enter transfer amount: "))
                if bank.transfer_money(from_acc, to_acc, amount):
                    print(f"Successfully transferred ${amount:.2f}")
                else:
                    print("Transfer failed")
            except ValueError:
                print("Please enter a valid number")
        
        elif choice == '6':
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                history = account.get_transaction_history()
                if history:
                    print("\nTransaction History:")
                    for transaction in history:
                        print(f"  {transaction['type'].title()}: ${transaction['amount']:.2f} "
                              f"at {transaction['timestamp']} (Balance: ${transaction['new_balance']:.2f})")
                else:
                    print("No transactions found")
            else:
                print("Account not found")
        
        elif choice == '7':
            accounts = bank.get_all_accounts()
            if accounts:
                print("\nAll Accounts:")
                for account in accounts:
                    print(f"  {account.account_number}: {account.owner_name} "
                          f"(Balance: ${account.balance:.2f})")
            else:
                print("No accounts found")
        
        elif choice == '8':
            bank.save_to_file("bank_data.json")
            print("Data saved successfully")
        
        elif choice == '9':
            bank.save_to_file("bank_data.json")
            print("Data saved. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()