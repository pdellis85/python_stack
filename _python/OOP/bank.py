class BankAccount:
    def __init__(self, rate, balance):
        self.rate = rate
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient Funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print("Balance: $", + self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.rate
        return self


ba1 = BankAccount(.40, 500)
ba2 = BankAccount(.10, 400)

ba1.make_deposit(40).make_deposit(80).make_deposit(
    100).yield_interest().display_account_info()
ba2.make_deposit(100).make_deposit(100).make_withdraw(
    20).make_withdraw(400).yield_interest().display_account_info()
