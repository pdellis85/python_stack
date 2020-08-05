class User:
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.account_balance = 500

    def make_withdraw(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("User: " + self.name,  "has a Balance of $" +
              str(self.account_balance))


rash = User("Rashaud", "Texas")
porsh = User("Porshea", "Washington")
kat = User("Kathy", "California")

porsh.make_withdraw(20)
porsh.display_user_balance()

rash.make_withdraw(120)
rash.display_user_balance()

kat.make_withdraw(220)
kat.display_user_balance()
