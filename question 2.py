class BankAccount:
    def __init__(self):
        self.__balance = 0.0  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance

# Demonstration of depositing and withdrawing money
account = BankAccount()

# Deposit money
account.deposit(100.0)
print(f"Current Balance: ${account.get_balance():.2f}")  # Current Balance: $100.00

# Withdraw money
account.withdraw(30.0)
print(f"Current Balance: ${account.get_balance():.2f}")  # Current Balance: $70.00

# Attempt to withdraw more than the balance
account.withdraw(100.0)
print(f"Current Balance: ${account.get_balance():.2f}")  # Current Balance: $70.00