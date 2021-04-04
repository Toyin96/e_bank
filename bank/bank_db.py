from customer import Customer


class Bank:
    """Models a bank that acts like a DB that stores
     all the customers details"""

    def __init__(self):
        """Initializing the bank attributes"""
        self.list_of_customers = []

    def create_new_customer(self):
        """Adds a new customer to the database"""
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        username = input("Enter your preferred username: ")
        age = input("Enter your current age: ")
        email_address = input("Enter your active email: ")
        phone_number = input("Enter your phone_number: ")
        address = input("Enter your home address: ")

        customer = {}

        response = self.input_validator(first_name, last_name, username, int(age), email_address, int(phone_number),
                                        address)

        if response:
            new_customer = Customer(first_name, last_name, username, age, email_address, phone_number, address)
            customer['first_name'] = new_customer.first_name.strip().lower()
            customer['last_name'] = new_customer.last_name.strip().lower()
            customer['username'] = new_customer.username.strip().lower()
            customer['age'] = int(new_customer.age)
            customer['balance'] = new_customer.account.account_balance
            customer['account_number'] = new_customer.account.account_number
            customer['email_address'] = new_customer.email_address.strip().lower()
            customer['phone_number'] = int(new_customer.phone_number)
            customer['address'] = new_customer.address.strip().lower()

            self.list_of_customers.append(customer)
            print(f"\nAccount created successfully. Here are your details\n {self.list_of_customers}")
        else:
            print("Could not create account")

    def input_validator(self, first_name, last_name, username, age, email_address, phone_number, address):
        """validates user inputs"""

        if isinstance(first_name, str):
            pass
        else:
            raise ValueError
        if isinstance(last_name, str):
            pass
        else:
            raise ValueError
        if username is not None:
            pass
        else:
            raise ValueError
        if isinstance(age, int):
            pass
        else:
            raise ValueError
        if email_address is not None:
            pass
        else:
            raise ValueError
        if isinstance(phone_number, int):
            pass
        else:
            raise ValueError
        if address is not None:
            pass
        else:
            raise ValueError

        return True

    def view_list_of_customers(self):
        return self.list_of_customers

    def make_deposit(self):

        print("Welcome to toyin's bank!\n")
        user_id = input("Enter your username: ")
        amount = int(input("Enter your amount you wish to deposit into your account: "))

        for user in self.list_of_customers:
            if user_id.lower().strip() == user['username']:
                print(f"Found your account, {user['first_name']}")
                if amount > 0:
                    user['balance'] += amount
                    print(f"Verification successful...You've deposited ${amount} into"
                          f" your account.\nNew account balance is ${user['balance']}")
                else:
                    print("You did not enter a valid amount")
            else:
                print("Username not recognized")

    def withdraw_money(self):

        print("Welcome to toyin's bank!\n")
        user_id = input("Enter your username: ")
        amount = int(input("Enter your amount you wish to withdraw: "))

        for user in self.list_of_customers:
            if user_id.lower().strip() == user['username']:
                print(f"Found your account, {user['first_name']}")
                if amount < user['balance']:
                    user['balance'] -= amount
                    print(f"SUCCESS...You've successfully withdrawn ${amount} from your"
                          f" account.\nNew account balance is ${user['balance']}")
                else:
                    print("You cannot withdraw more than your available balance")
            else:
                print("Username not recognized")

    def get_customers(self):
        """fetches all the customers in the database"""
        for user in self.list_of_customers:
            print(user)


if __name__ == "__main__":
    toyin_bank = Bank()
    toyin_bank.create_new_customer()
    toyin_bank.create_new_customer()
    toyin_bank.customer.first_name
