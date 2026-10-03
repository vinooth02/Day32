class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.__balance)

    @staticmethod
    def bank_message():
        print("Welcome to ABC Bank")