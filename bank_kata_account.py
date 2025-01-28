from datetime import datetime

class Account:
    def __init__(self):
        self.transactions = []

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.transactions.append((datetime.now().strftime("%d-%m-%Y"), amount))

    def withdraw(self, amount: int):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        self.transactions.append((datetime.now().strftime("%d-%m-%Y"), -amount))

    def print_statement(self):
        balance = 0
        statement = "DATE       | AMOUNT  | BALANCE\n"
        for date, amount in self.transactions:
            balance += amount
            statement += f"{date} | {amount:+7} | {balance:+7}\n"
        print(statement)

# Example usage
if __name__ == "__main__":
    account = Account()
    account.deposit(1000)  # Mock deposit  at date xx--1dd
    account.deposit(20000)