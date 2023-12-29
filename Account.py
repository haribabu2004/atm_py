import os
# import users.txt

class ATM:

    def __init__(self, balance=0):
        self.balance = balance
        self.users_file = "C:\\Users\\sys\\Documents\\atm_py\\users.txt"

        self.users_data = self.load_users_data()

    def load_users_data(self):
        users_data = {}
        if os.path.exists(self.users_file):
            with open(self.users_file, "r") as file:
                for line in file:
                    username, password, balance_str = line.strip().split(",")
                    balance = float(balance_str)
                    users_data[username] = {"password": password, "balance": balance}
        return users_data

    def save_users_data(self):
        with open(self.users_file, "w") as file:
            for username, data in self.users_data.items():
                password = data["password"]
                balance = data["balance"]
                file.write(f"{username},{password},{balance}\n")

    def authenticate_user(self, username, password):
        if username in self.users_data and self.users_data[username]["password"] == password:
            return True
        else:
            return False

    def display_balance(self, username):
        print(f"Your balance is ${self.users_data[username]['balance']}")

    def deposit(self, username, amount):
        self.users_data[username]["balance"] += amount
        print(f"Deposited ${amount}")
        self.display_balance(username)
        self.save_users_data()

    def withdraw(self, username, amount):
        minimum_balance = 500  # Adjust this value to set the minimum balance requirement

        if amount > self.users_data[username]["balance"] - minimum_balance:
            print(f"Withdrawal failed. Minimum balance requirement not met.")
        else:
            self.users_data[username]["balance"] -= amount
            print(f"Withdrew ${amount}")
            self.display_balance(username)
            self.save_users_data()