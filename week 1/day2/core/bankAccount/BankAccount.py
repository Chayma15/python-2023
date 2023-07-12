class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance += interest

# Example usage
account1 = BankAccount(0.01, 1000)  # Create a BankAccount instance with 1% interest and initial balance of $1000
account1.display_account_info()  # Output: Balance: $1000

account1.deposit(500)  # Deposit $500
account1.display_account_info()  # Output: Balance: $1500

account1.withdraw(200)  # Withdraw $200
account1.display_account_info()  # Output: Balance: $1300

account1.yield_interest()  # Apply interest
account1.display_account_info()  # Output: Balance: $1313
