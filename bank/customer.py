"""Set of class that is used to represent Account and Customer classes"""

from account import Account


class Customer:
    """Simulates a typical user object"""

    def __init__(self, first_name, last_name, username, age, email_address, phone_number, address):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.email_address = email_address
        self.phone_number = phone_number
        self.address = address
        self.login_attempt = 0
        self.account = Account(0)

    def describe_user(self):
        """Gives a description of the user profile"""
        print("Below is a brief description of the user:")
        print(f"\nfull name: {self.first_name} {self.last_name}\nusername: {self.username}\nage: {self.age}\n"
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

