class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0.0):
        self.account_number=account_number
        self.name=name
        self.account_type=account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:",amount)
        print("Updated Balance:",self.balance,"\n")

    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Amount withdrawan:", amount)
            print("Remaining balance:",self.balance,"\n")
        else:
            print("Insufficient balance!\n")

    def display(self):
        print("------------Account Details--------")
        print("Account Number:",self.account_number)
        print("Name:",self.name)
        print("Account Type:",self.account_type)
        print("Balance:",self.balance)

# Example usage
acc1 = BankAccount("374932", "Aswathi", "Savings", 80000)
acc1.display()
acc1.deposit(2000)
acc1.withdraw(3000)
acc1.withdraw(5000)

