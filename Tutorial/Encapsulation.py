class Bank:
    def __init__(self):
        self.__balance = 0

    def checkBalance(self):
        return self.__balance

    def deposit(self, add):
        self.__balance = self.__balance + add
        return "Success"

    def withdraw(self, sub):
        if self.__balance - sub >= 0:
            self.__balance = self.__balance - sub
            return "Success"
        else:
            return "Insufficient balance"
