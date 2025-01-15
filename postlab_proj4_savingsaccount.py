"""
File: savingsaccount.py
This module defines the SavingsAccount class.
"""

class SavingsAccount:
    """This class represents a savings account with the owner's name, PIN, and balance."""

    RATE = 0.02  # Single rate for all accounts

    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        """Returns the string representation of the savings account."""
        result = f"Name: {self.name}\nPIN: {self.pin}\nBalance: {self.balance}"
        return result

    def getName(self):
        """Returns the account holder's name."""
        return self.name

    def getPin(self):
        """Returns the account's PIN."""
        return self.pin

    def getBalance(self):
        """Returns the account's balance."""
        return self.balance

    def deposit(self, amount):
        """Deposits an amount into the account if it is valid."""
        if amount <= 0:
            return "Deposit amount must be greater than 0"
        self.balance += amount
        return None

    def withdraw(self, amount):
        """Withdraws an amount from the account if valid."""
        if amount < 0:
            return "Withdrawal amount must be greater than 0"
        if self.balance < amount:
            return "Insufficient funds"
        self.balance -= amount
        return None

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    def __lt__(self, other):
        """Compares two SavingsAccount objects based on their names."""
        return self.name < other.name

    def __eq__(self, other):
        """Checks equality of two SavingsAccount objects."""
        return self.name == other.name and self.pin == other.pin
