# ----------------- Customer Class -----------------
class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def __str__(self):
        return f"Customer Name: {self.name}, ID: {self.customer_id}"


# ----------------- Base Account Class -----------------
class Account:
    def __init__(self, account_number, customer, balance=0):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance = {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New Balance = {self.balance}")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer: {self.customer.name}")
        print(f"Balance: {self.balance}")


# ----------------- Saving Account (Inheritance) -----------------
class SavingAccount(Account):
    def __init__(self, account_number, customer, balance=0, interest_rate=5):
        super().__init__(account_number, customer, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        print(f"Interest added: {interest}. New Balance = {self.balance}")


# ----------------- Current Account (Inheritance) -----------------
class CurrentAccount(Account):
    def __init__(self, account_number, customer, balance=0, overdraft_limit=5000):
        super().__init__(account_number, customer, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New Balance = {self.balance}")


# ----------------- Transaction Class -----------------
class Transaction:
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

    def process(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type!")


# ----------------- Example Usage -----------------
cust = Customer("Prafull", 101)

acc = SavingAccount(1001, cust, 2000)
acc.display_details()

# Deposit
t1 = Transaction(acc, 500, "deposit")
t1.process()

# Withdraw
t2 = Transaction(acc, 800, "withdraw")
t2.process()

# Add Interest
acc.add_interest()
