from __future__ import annotations

# Part 1:
# Define class CurrentAccount which represents a current account.
# Current accounts allow to withdraw and make transfers even if the balance is negative.
# deposit(amount: int) -> bool: balance increases by amount and always returns True.
# withdraw(amount: int) -> bool: balance decreases by amount and always returns True.
# transfer(amount: int, target) -> bool: sends amount to target account and returns True if successful, else False. Substracts the amount from the current account and adds it to the target account.

# Part 2:
# Define CheckingAccount which represents a checking account.
# Checking accounts are similar to current accounts but their balance can't be negative.
# deposit(amount: int) -> bool: balance increases by amount and always returns True.
# withdraw(amount: int) -> bool: Validates if the balance is enough to withdraw the amount. If not, returns False. If enough, balance decreases by amount and returns True.
# transfer(amount: int, target) -> bool: First validates if the balance is enough to withdraw the amount. If not, returns False. If enough, when the target account receives the amount, the balance of the current account decreases by the amount and the balance of the target account increases by the amount.

# Part 3:
# in main.py instantiate one object from CurrentAccount and one object from CheckingAccount and make some deposits, withdrawals and transfers between them.
# Make sure to handle the cases where the balance is not enough to withdraw the amount or the target account is not a CheckingAccount.

# Part 4:
# Define StudentAccount which represents a student account.
# Student accounts are similar to checking accounts, their balance can't be negative, and additionally they have limits for the balance max_money, for the deposit max_deposit and for transfer amount max_transfer.
# this class receives the max_money, max_deposit and max_transfer as parameters in the constructor, where the default values are:
# * max_money = 100000
# * max_deposit = 100000
# * max_transfer = 10000
# the methods in this class are defined as:
# deposit(amount: int) -> bool: Validates that the amount is not greater than max_deposit and that after the deposit the balance is not greater than max_money. If validation is successful, the balance increases by the amount and returns True and if not, returns False.
# withdraw(amount: int) -> bool: Validates that after the withdrawal the balance is not negative. If validation is successful, the balance decreases by the amount and returns True and if not, returns False.
# transfer(amount: int, target) -> bool: Validates that the amount is not greater than max_transfer and that after the transfer the balance is not greater than max_money. If validation is successful, the balance decreases by the amount and the target account increases by the amount and returns True and if not, returns False.

# Part 5:
# in main.py instantiate one object from StudentAccount and make some deposits, withdrawals and transfers between it and the CheckingAccount.
# Make sure to handle the cases where the balance is not enough to withdraw the amount or the target account is not a CheckingAccount.

# The definitions are now complete, please implement the classes and test them in main.py.

class CurrentAccount:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, amount: int) -> bool:
        self.balance += amount
        return True
    
    def withdraw(self, amount: int) -> bool:
        self.balance -= amount
        return True
    
    def transfer(self, amount: int, target) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            target.balance += amount
            return True
        return False
    
class CheckingAccount(CurrentAccount):
    def __init__(self, balance: int = 0):
        super().__init__(balance)

    def withdraw(self, amount: int) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

class StudentAccount(CheckingAccount):
    def __init__(self, balance: int = 0, max_money: int = 100000, max_deposit: int = 100000, max_transfer: int = 10000):
        super().__init__(balance)
        self.max_money = max_money
        self.max_deposit = max_deposit
        self.max_transfer = max_transfer

    def deposit(self, amount: int) -> bool:
        if amount > self.max_deposit:
            return False
        if self.balance + amount > self.max_money:
            return False
        self.balance += amount
        return True
    
    def withdraw(self, amount: int) -> bool:
        if self.balance - amount < 0:
            return False
        self.balance -= amount
        return True
    
    def transfer(self, amount: int, target) -> bool:
        if amount > self.max_transfer:
            return False
        if self.balance - amount < 0:
            return False
        self.balance -= amount
        target.balance += amount
        return True
