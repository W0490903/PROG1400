"""
Author: Zachary Mason
Student ID: W0490903
Course: PROG1400
Date: 2024-01-18
Project: Intro OOP Functions to Classes
Repository: https://github.com/W0490903/PROG1400/
Programming Language: Python 3
"""

class BankAccount:
    # Constructor (__init__ method)
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Deposit money to an account.
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} Successful. New Balance: ${self.balance}")

    # Withdraw money from an account
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} Successful. New Balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account Owner: {self.owner}, Current Balance: ${self.balance}")

account1 = BankAccount("Zach")
account1.display_balance()
account1.deposit(1500)
account1.withdraw(700)
account1.display_balance()