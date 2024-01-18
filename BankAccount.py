"""
Author: Zachary Mason
Student ID: W0490903
Course: PROG1400
Date: 2024-01-18
Project: Intro OOP Functions to Classes
Repository: https://github.com/W0490903/PROG1400/
Programming Language: Python 3
"""

# Create a bank account and append it to a dictionary.
def create_account(owner, balance=0):
    return {"owner": owner, "balance": balance}

# Deposit money to an account.
def deposit(account, amount):
    account["balance"] += amount
    print(f"Deposit of ${amount} Successful. New Balance: ${account["balance"]}")

# Withdraw money from an account.
def withdraw(account, amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f"Withdrawal of ${amount} Successful. New Balance: ${account["balance"]}")
    else:
        print("Insufficient Funds.")

# Display the current balance of an account.
def display_balance(account):
    print(f"Account Owner: {account["owner"]}, Balance: ${account ["balance"]}")


# Main
account1 = create_account("Zach")
#print(account1)
display_balance(account1)
deposit(account1, 1000)
withdraw(account1, 1000)
print(type(account1))