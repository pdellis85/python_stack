class User:
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.account_balance = 500

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdraw(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("User: " + self.name,  "has a Balance of $" +
              str(self.account_balance))
    
    def transer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdraw(amount)

rash = User("Rashaud", "Texas")
porsh = User("Porshea", "Washington")
kat = User("Kathy", "California")


rash.make_deposit(20)
rash.make_deposit(25)
rash.make_deposit(40)
rash.make_withdraw(120)
rash.display_user_balance()

porsh.make_deposit(200)
porsh.make_deposit(100)
porsh.make_withdraw(20)
porsh.make_withdraw(20)
porsh.display_user_balance()

kat.make_deposit(220)
kat.make_withdraw(20)
kat.make_withdraw(20)
kat.make_withdraw(20)
kat.display_user_balance()

# bonus
rash.transer_money(kat, 100)
rash.display_user_balance()
kat.display_user_balance()