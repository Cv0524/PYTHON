import json
import os
import random
DATA_FILE = "C:/PYTHON/ATM/usersv1.json"


balance = 0
def generate_account_number():
    return random.randint(1000, 9999)
#load data
def load_users(path=DATA_FILE):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
#saved data
def save_users(users_info, path=DATA_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(users_info, f, indent=2)
#Global 
users_credential = load_users()
def edit_user():
    print("Edit User Credentials")
    account_number = str(input("Enter Account Number: ")).strip()
    if account_number in users_credential:
        fullname = users_credential[account_number]["fullname"].strip()

    while True:
        print(f"Account Access name is: {fullname}")
        print(f"Press [1] to change pin")
        print(f"Press [2] to change fullname")
        choice = str(input("Enter you choice here: "))
        if choice in {"1","2"}:
            print("Processing...")
            break
        print("--->Invalid input, try again<---")

    if choice == "1":
        valid_input = True
        while valid_input:
            new_pin = input("New pin: ").strip()
            if len(new_pin) < 4: #check the length of the pin
                print(f"Pin must be atleast 4 digits: ")
                continue
            if new_pin == users_credential[account_number]["pin"]: # check if new pin is like in the previous pin
                print("You entered previous PIN! Try new one")
                continue
            else:
                users_credential[account_number]["pin"] = new_pin
                print("PIN updated!")
                valid_input = False
    else:
            new_fullname = input("Enter new fullname: ").strip()
            if not new_fullname:
                print("Fullname cannot be empty!")
                
            users_credential[account_number]["fullname"] = new_fullname
            print("Fullname updated")
    save_users(users_credential)


def create_account():
    users_info = load_users()  # {account_number_str: {"pin": str, "fullname": str}}
    while True:
        print("Create new account")
        fullname = input("Enter your fullname: ").strip()
        pin = input("Enter your pin: ").strip()
        
        try:
            initial_deposite = int(input("Enter initial deposite amount: "))
            if initial_deposite < 0:
                print("Invalid amount!")
                continue
        except ValueError:
            print("Deposite amount must be integer")
        balance = initial_deposite

        acct = str(generate_account_number())
        while acct in users_info:
            acct = str(generate_account_number())

        users_info[acct] = {"fullname": fullname,"pin": pin, "balance": balance}
        save_users(users_info)  # persist immediately

        print("Added new user:", {"account_number": acct})
        cont = input("Add another? (y/n): ").strip().lower()
        if cont != "y":
            break

def withdraw():
    print("---> Withdraw <---")
    acct = input("Enter your account number: ")
    if acct in users_credential:
        amount = int(input("Enter amount: "))
        current_balance = users_credential[acct]["balance"]
        new_balance = current_balance - amount
        users_credential[acct]["balance"] = new_balance
        print("Processing...")
        print(f"{amount} Withdraw sucessully!")
    else:
        print("Invalid credentials")
    save_users(users_credential)
def balance():
    print("---> Check Balance <---")
    acct = input("Enter you account number: ")
    if acct in users_credential:
        print("You current balance: ", users_credential[acct]["balance"])
    else:
        print("Invalid credentials")
def deposite():
    print("---> Deposite <---")
    acct = input("Enter your account number: ")
    amount = int(input("Enter amount: "))
    if acct in users_credential:
        new_balance = users_credential[acct]["balance"] + amount
        users_credential[acct]["balance"] = new_balance
        view_balance = (users_credential[acct]["balance"])
        print("Your new balance is:", {view_balance})
    else:
        print("Invalic credentials!")
    save_users(users_credential)

def main():
    print("---> ATM machine <---")
    transaction = {1, 2, 3, 4, 5}
    while True:
        print("Transactions: ")
        print("[1] Create Account (New Client)")
        print("[2] Deposit")
        print("[3] Withdraw")
        print("[4] Balance")
        print("[5] Edit Credentials")
        try:
            choice = int(input("Type here: ").strip())
        except ValueError:  # catch wrong input like 'ss'
            print("!!---> Invalid input enter a number 1-5 <---!!")
            continue
        if choice not in transaction:
            print("!!---> Invalid transaction <---!!")
            continue
        print("Processing...")
        if choice in transaction:
            if choice == 1:
                create_account()
            elif choice == 2:
                deposite()
            elif choice == 3:
                withdraw()
            elif choice == 4:
                balance()
            elif choice == 5:
                edit_user()
            else:
                print("Invalid input")
main()