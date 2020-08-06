class User:
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.account_balance = 500

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User: " + self.name,  "has a Balance of $" +
              str(self.account_balance))
        return self

    def transer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdraw(amount)
        return self


rash = User("Rashaud", "Texas")
porsh = User("Porshea", "Washington")
kat = User("Kathy", "California")


rash.make_deposit(20).make_deposit(25).make_deposit(
    40).make_withdraw(120).display_user_balance()

porsh.make_deposit(200).make_deposit(100).make_withdraw(
    20).make_withdraw(20).display_user_balance()

kat.make_deposit(220).make_withdraw(20).make_withdraw(
    20).make_withdraw(20).display_user_balance()

# bonus
rash.transer_money(kat, 100).display_user_balance()
kat.display_user_balance()
