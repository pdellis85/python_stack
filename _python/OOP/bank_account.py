class BankAccount:
    def __init__(self, rate, balance):
        self.rate = rate
        self.account_balance = balance
        

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdraw(self, amount):
        if amount > self.account_balance:
            print(
                f"You are withdrawing {amount} but only have {self.account_balance}, charging $5 fee.")
            self.account_balance -= (amount+5)
            self.account_balance -= amount
        return self

    def display_account_info(self):
        print("Balance: $" + str(self.account_balance))
        return self

    def yield_interest(self):
        amount_earned = self.acctount_balance * self.int_rate
        self.account_balance += amount_earned
        return self


class User:
    def __init__(self, name):
        self.name = name
        self.accounts = BankAccount(.05,500)


rash = User("Rash")
porsh = User("Porshea")

rash.accounts.make_deposit(100).display_account_info()
porsh.accounts.make_withdraw(800).display_account_info()
