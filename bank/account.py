from random import randrange


class Account:
    """A model for a e-service bank"""

    def __init__(self, balance=0):
        """Initializes the bank attributes"""
        self.account_balance = balance
        self.account_number = self.random_generator()

    def random_generator(self):
        """Generates a random number at every given call"""
        x = 1
        account_case = 'TOY'
        while x <= 7:
            account_case += str(randrange(9))
            x += 1
        return account_case

    def get_account_balance(self):
        """Returns the value of the account number"""
        print(f"Your account number is ${self.account_balance}")

    def deposit_funds(self, amount: int):
        """Deposits money upon verification to the given account"""

        if amount < 0:
            print("You cannot deposit an amount less than $0")
        else:
            self.account_balance += amount
