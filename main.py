# import os
from Account import ATM

def main():
    atm=ATM()
    
    print("Welcome to the BKL Bank!")
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if atm.authenticate_user(username,password):
        print(f"Welcome, {username}!")
    else:
        print("Invalid username or password. Please try again.")
        return
    
    
    while True:
        print("\nOptions:")
        print("1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            atm.display_balance(username)
        elif choice == '2':
            amount = float(input("Enter deposit amount: $"))
            atm.deposit(username, amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: $"))
            atm.withdraw(username, amount)
        elif choice == '4':
            print("Exiting ATM. Thank you!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()