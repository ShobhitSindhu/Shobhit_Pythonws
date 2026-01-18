class BankAccount:
    def __init__(self, acc_no, balance=0):
        self.account_number = acc_no
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount

account = BankAccount("123456", 1000)
account.set_balance(2000)
print(account.get_balance())
