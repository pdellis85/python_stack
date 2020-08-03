class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User: " + self.name, "Balance: $" + str(self.account_balance))
        return self

    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self


rash = User("Rashaud", "rash@rash.com")
porshea = User("Porshea", "porsh@porsh.com")
kathy = User("Kathy", "kat@kat.com")

porshea.make_deposit(100).make_deposit(100).make_deposit(
    100).make_withdrawal(50).display_user_balance()


rash.make_deposit(50).make_deposit(1000).make_withdrawal(
    500).make_withdrawal(100).display_user_balance()

kathy.make_deposit(100).make_withdrawal(25).make_withdrawal(
    25).make_withdrawal(25).display_user_balance()

# BONUS
rash.transfer_money(kathy, 250).display_user_balance()
kathy.display_user_balance()
