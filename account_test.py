from bank1 import BankAccount


class AccountTest:

    @staticmethod
    def start_program():

        BankAccount.bank_message()

        account = BankAccount("Karan", 10000)

        account.display()

        account.deposit(2000)

        print()

        account.display()


AccountTest.start_program()