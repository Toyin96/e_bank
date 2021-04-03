class Account:
    """A model for a e-service bank"""

    def __init__(self, balance):
        """Initializes the bank attributes"""
        self.account_balance = balance

    def get_account_balance(self):
        """Returns the value of the account number"""
        print(f"Your account number is ${self.account_balance}")

    def deposit_funds(self, amount: int):
        """Deposits money upon verification to the given account"""

        if amount < 0:
            print("You cannot deposit an amount less than $0")
        else:
            self.account_balance += amount
