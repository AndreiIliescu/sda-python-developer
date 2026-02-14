class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self):
        amount = int(input("Amount to deposit: "))
        self.balance += amount
        print(f"The amount: {amount} € was deposited.")

    def withdraw(self):
        amount = int(input("Amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"The amount: {amount} € was withdraw.")

    def check_balance(self):
        print(f"Current balance: {self.balance} €")


def menu(account):
    while True:
        print("\n=== Bank Menu ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose option (1-4): ")

        if choice == "1":
            account.deposit()
        elif choice == "2":
            account.withdraw()
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Exit... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


account = BankAccount()
menu(account)
