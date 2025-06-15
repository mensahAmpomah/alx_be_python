# Defining the class named BankAccount.

class BankAccount:
    def __init__(self,initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self.account_balance += amount
            # print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            # print(f"Withdrawn: ${amount}")
            return True
        else:
            print("Insufficient funds.")
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
        
