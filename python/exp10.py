class bank_account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def bank_fees(self):
        self.bank_fees = self.balance * 0.05

    def display(self):
        print("-" * 64)
        print("Account No: ", self.acc_no)
        print("Accound Holder Name: ", self.name)
        print("Balance: ", self.balance)
        print("Bank Fees: ", self.bank_fees)

    def __del__(self):
        print("Object deleted")


def main():

    acc_no = int(input("Enter Account Number: "))
    name = input("Enter Account Holder Name: ")
    initial_balance = int(input("Enter Balance: "))

    first_acc = bank_account(acc_no, name, initial_balance)

    money_dep = int(input("Enter the amount to deposit: "))
    first_acc.deposit(money_dep)

    first_acc.bank_fees()

    first_acc.display()


main()
