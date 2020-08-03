class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("User: " + self.name, "Balance: $" + str(self.account_balance))

    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)


rash = User("Rashaud", "rash@rash.com")
porshea = User("Porshea", "porsh@porsh.com")
kathy = User("Kathy", "kat@kat.com")

porshea.make_deposit(100)
porshea.make_deposit(100)
porshea.make_deposit(100)
porshea.make_withdrawal(50)
porshea.display_user_balance()

rash.make_deposit(50)
rash.make_deposit(1000)
rash.make_withdrawal(500)
rash.make_withdrawal(100)
rash.display_user_balance()

kathy.make_deposit(100)
kathy.make_withdrawal(25)
kathy.make_withdrawal(25)
kathy.make_withdrawal(25)
kathy.display_user_balance()

# BONUS
rash.transfer_money(kathy, 250)
rash.display_user_balance()
kathy.display_user_balance()
