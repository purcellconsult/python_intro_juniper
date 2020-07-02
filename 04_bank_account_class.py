
class BankAccount:
    """
    This is a class that emulates
    a BankAccount using OOP in python.
    """
    def __init__(self, balance, account_number, customer):
        self.balance = balance
        self.account = account_number
        self.customer = customer

    def __str__(self):
        return f'{self.customer}, {self.account}, {self.balance}'

    def get_balance(self):
        return self.balance

    def withdrawal(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough funds")
        elif amount > 10000:
            raise ValueError("Can't withdraw more than 10000 in a day")
        elif amount <= 0:
            raise ValueError("Enter in a value greater than 0")
        else:
            self.balance -= amount

    def make_deposit(self, amount):
        if amount > 10000:
            raise ValueError("Amount is too large")
        elif amount <= 0:
            raise ValueError("Enter in a positive number!")
        else:
            self.balance += amount


b1 = BankAccount(1000, '2628-8267-2732-3828', 'Daniel')
print(b1.get_balance())

b1.withdrawal(500)
print(b1.get_balance())
b1.withdrawal(400)
print(b1.get_balance())
b1.withdrawal(100)
print(b1.get_balance())
b1.make_deposit(2500)
print(b1.get_balance())
print(b1)


