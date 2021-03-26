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

    # def withdraw_funds(self, amount):
    #     """Withdraws money upon verification from the given account"""


class Customer:
    """Simulates a typical user object"""

    def __init__(self, first_name, last_name, age, email_address, phone_number, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email_address = email_address
        self.phone_number = phone_number
        self.address = address
        self.login_attempt = 0
        self.account = Account(0)

    def describe_user(self):
        """Gives a description of the user profile"""
        print("Below is a brief description of the user:")
        print(f"full name: {self.first_name} {self.last_name}\nage: {self.age}\n"
              f"email_address: {self.email_address}\nphone_number: {self.phone_number}\n"
              f"address: {self.address}\nlogin attempt: {self.login_attempt}\n")

    def greet_user(self):
        """Prints a personalized greeting to user"""
        print(f"Hello {self.first_name} {self.last_name}! How are you today?")

    def increment_login_attempt(self):
        """Increments the login_attempt by 1"""
        self.login_attempt += 1

    def reset_login_attempts(self):
        """Resets login attempts to 0"""
        self.login_attempt = 0

    def display_user_login_attempt(self):
        """Displays user's login attempt so far"""
        print(self.login_attempt)


customer = Customer("Toyin", "Onag", 25, "onagoruwam@gmail.com", "09043910175", "42, Aderupoko street, Iwaya")
customer.account.deposit_funds(-1)
customer.describe_user()
