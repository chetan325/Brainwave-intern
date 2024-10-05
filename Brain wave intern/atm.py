class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully! :-)")
        else:
            print("Invalid amount!!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully! :-)")
        elif amount > self.balance:
            print("Insufficient balance!!")
        else:
            print("Invalid amount!!")

    @staticmethod
    def authenticate(pin):
        # sample PIN for authentication
        correct_pin = "1234"
        return pin == correct_pin

    @staticmethod
    def atm_menu():
        print("\nWelcome to the ATM")
        print("1. Check the Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def main(self):
        user_attempts = 0
        max_attempts = 3

        while user_attempts < max_attempts:
            pin = input("Enter your 4-digit PIN: ")
            if self.authenticate(pin):
                print("Authentication Successful :-)\n")
                atm = ATM(balance=5000)  # initial balance for the user
                while True:
                    self.atm_menu()
                    choice = input("Enter your option: ")

                    if choice == "1":
                        atm.check_balance()
                    elif choice == "2":
                        amount = float(input("Enter the amount to deposit: "))
                        atm.deposit(amount)
                    elif choice == "3":
                        amount = float(input("Enter the amount to withdraw: "))
                        atm.withdraw(amount)
                    elif choice == "4":
                        print("Thank you for using our ATM service! Have a nice day :-)")
                        break
                    else:
                        print("Invalid option! Please try again :-(")
            else:
                user_attempts += 1
                print(f"Invalid PIN! You have {max_attempts - user_attempts} attempts left!!")
            if user_attempts == max_attempts:
                print("Account Locked!! Please contact the bank!!")

if __name__ == "__main__":
    ATM().main()
