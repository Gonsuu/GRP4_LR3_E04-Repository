"""
File: bank.py
This module defines the Bank class.
"""
import pickle
from savingsaccount import SavingsAccount

class Bank:
    """This class represents a bank as a collection of savings accounts."""

    def __init__(self, fileName=None):
        """Creates a new bank and optionally loads accounts from a file."""
        self.accounts = {}
        self.fileName = fileName
        if fileName is not None:
            with open(fileName, 'rb') as fileObj:
                while True:
                    try:
                        account = pickle.load(fileObj)
                        self.add(account)
                    except EOFError:
                        break

    def __str__(self):
        """Returns the string representation of the bank, sorted by account names."""
        sorted_accounts = sorted(self.accounts.values())
        return "\n".join(map(str, sorted_accounts))

    def makeKey(self, name, pin):
        """Creates a unique key for the account."""
        return f"{name}/{pin}"

    def add(self, account):
        """Adds an account to the bank."""
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """Removes and returns an account from the bank."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Gets an account by name and PIN."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Computes and deposits interest for all accounts."""
        total_interest = 0
        for account in self.accounts.values():
            total_interest += account.computeInterest()
        return total_interest

    def save(self, fileName=None):
        """Saves accounts to a file."""
        if fileName is not None:
            self.fileName = fileName
        elif self.fileName is None:
            return
        with open(self.fileName, 'wb') as fileObj:
            for account in self.accounts.values():
                pickle.dump(account, fileObj)

# Functions for testing

def createBank(numAccounts=1):
    """Creates and returns a bank with the specified number of accounts."""
    import random
    names = ["Brandon", "Molly", "Elena", "Mark", "Tricia", "Ken", "Jill", "Jack"]
    
    if numAccounts > len(names):
        raise ValueError("Cannot generate more accounts than there are unique names.")
    
    bank = Bank()

    selected_names = random.sample(names, numAccounts)  # Ensure no name is duplicated
    for index, pinNumber in enumerate(range(1000, 1000 + numAccounts)):
        name = selected_names[index]
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pinNumber), balance))

    return bank

def main():
    """Main function for testing."""
    try:
        bank = createBank(8)  # Specify the number of accounts (up to 8 unique names)
        print("Bank Accounts (Sorted by Name):")
        print(bank)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
