class BankAccount:
    def __init__(self, rate, balance, a_type):
        self.rate = rate
        self.account_balance = balance
        self.a_type = a_type

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
        print("Balance: $", + self.account_balance)
        return self

    def yield_interest(self):
        amount_earned = self.account_balance * self.int_rate
        self.account_balance += amount_earned
        return self


class User:
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.accounts = {'checking': BankAccount(
            int_rate, balance, 'checking')}

    def create_account(self, int_rate, balance, b_type):
        self.accounts[b_type] = BankAccount(int_rate, balance, b_type)
        return self


rash = User("Rash", .02, 1000)
porshea = User("Porshea", .05, 500)
porshea.create_account(.04, 200, 'saving')
porshea.accounts['checking'].display_account_info()
porshea.accounts['saving'].display_account_info()
