import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    # ---------- LOAD DATABASE ----------
    @classmethod
    def load(cls):
        try:
            if Path(cls.database).exists():
                with open(cls.database, "r") as fs:
                    cls.data = json.load(fs)
            else:
                cls.data = []
        except Exception as err:
            print(f"Error loading database: {err}")
            cls.data = []

    # ---------- UPDATE DATABASE ----------
    @classmethod
    def update(cls):
        try:
            with open(cls.database, 'w') as fs:
                json.dump(cls.data, fs, indent=4)
        except Exception as err:
            print(f"Error updating database: {err}")

    # ---------- ACCOUNT GENERATOR ----------
    @classmethod
    def _accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        acc = alpha + num + spchar
        random.shuffle(acc)
        return "".join(acc)

    # ---------- CREATE ACCOUNT ----------
    def Createaccount(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        email = input("Enter your email: ")
        pin = input("Enter your 4-digit pin: ")

        if len(pin) != 4 or not pin.isdigit() or age < 18:
            print("Sorry, account cannot be created (invalid age or pin).")
            return

        pin = int(pin)

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": Bank._accountgenerate(),
            "balance": 0
        }

        Bank.data.append(info)
        Bank.update()

        print("Account created successfully!")
        for i in info:
            print(f"{i} : {info[i]}")
        print("Please note down your account number.")

    # ---------- DEPOSIT MONEY ----------
    def depositmoney(self):
        accnumber = input("Enter your account number: ")
        pin = input("Enter your pin: ")

        if not pin.isdigit():
            print("Invalid pin.")
            return

        pin = int(pin)

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry, no account found.")
            return

        amount = int(input("Enter amount to deposit: "))

        if amount <= 0 or amount > 100000:
            print("Invalid deposit amount.")
            return

        userdata[0]['balance'] += amount
        Bank.update()
        print(f"Amount deposited successfully. New balance: {userdata[0]['balance']}")

    # ---------- WITHDRAW MONEY ----------
    def withdrawmoney(self):
        accnumber = input("Enter your account number: ")
        pin = input("Enter your pin: ")

        if not pin.isdigit():
            print("Invalid pin.")
            return

        pin = int(pin)

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry, no account found.")
            return

        amount = int(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount.")
            return

        if userdata[0]['balance'] < amount:
            print("Insufficient balance.")
            return

        userdata[0]['balance'] -= amount
        Bank.update()
        print(f"Amount withdrawn successfully. New balance: {userdata[0]['balance']}")

    # ---------- SHOW DETAILS ----------
    def showdetails(self):
        accnumber = input("Enter your account number: ")
        pin = input("Enter your pin: ")

        if not pin.isdigit():
            print("Invalid pin.")
            return

        pin = int(pin)

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry, no account found.")
            return

        print("Your account details:")
        for k, v in userdata[0].items():
            print(f"{k} : {v}")

    # ---------- UPDATE DETAILS ----------
    def updatedetails(self):
        accnumber = input("Enter your account number: ")
        pin = input("Enter your pin: ")

        if not pin.isdigit():
            print("Invalid pin.")
            return

        pin = int(pin)

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("No account found.")
            return

        print("You cannot change age, account number, or balance.")
        print("Leave field empty to keep old value.")

        new_name = input("Enter new name: ")
        new_email = input("Enter new email: ")
        new_pin = input("Enter new 4-digit pin: ")

        if new_pin != "" and (not new_pin.isdigit() or len(new_pin) != 4):
            print("Invalid PIN format.")
            return

        userdata = userdata[0]

        if new_name:
            userdata['name'] = new_name
        if new_email:
            userdata['email'] = new_email
        if new_pin:
            userdata['pin'] = int(new_pin)

        Bank.update()
        print("Details updated successfully.")

    # ---------- DELETE ACCOUNT ----------
    def Delete(self):
        accnumber = input("Enter your account number: ")
        pin = input("Enter your pin: ")

        if not pin.isdigit():
            print("Invalid pin.")
            return

        pin = int(pin)

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("No account found.")
            return

        confirm = input("Press Y to confirm account deletion: ")

        if confirm.upper() == "Y":
            Bank.data.remove(userdata[0])
            Bank.update()
            print("Account deleted successfully.")
        else:
            print("Deletion cancelled.")


def run_cli():
    """Run the original terminal-based interface."""
    Bank.load()
    user = Bank()
    while True:
        print("\nWelcome to the Bank Management System")
        print("-------------------------------------")
        print("1. Create an account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Show account details")
        print("5. Update account details")
        print("6. Delete account")
        print("7. Exit")
        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice == 1:
            user.Createaccount()
        elif choice == 2:
            user.depositmoney()
        elif choice == 3:
            user.withdrawmoney()
        elif choice == 4:
            user.showdetails()
        elif choice == 5:
            user.updatedetails()
        elif choice == 6:
            user.Delete()
        elif choice == 7:
            print("Thank you for using the Bank Management System.")
            break
        else:
            print("Invalid choice.")
        print("Thank you for using the Bank Management System.")


if __name__ == "__main__":
    run_cli()