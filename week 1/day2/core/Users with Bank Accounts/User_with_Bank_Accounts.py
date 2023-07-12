class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")

# Example usage
user1 = User("John Doe", "john@example.com")  # Create a User instance
user1.display_user_balance()  # Output: User: John Doe, Balance: $0

user1.make_deposit(500)  # Deposit $500 into the user's account
user1.display_user_balance()  # Output: User: John Doe, Balance: $500

user1.make_withdrawal(200)  # Withdraw $200 from the user's account
user1.display_user_balance()  # Output: User: John Doe, Balance: $300
