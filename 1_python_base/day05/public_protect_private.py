# Author: bibberzz
# Created: 2026/5/30 10:51
# Project: day5
# File: public_protect_private.py
# Description:

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # private type

    # def get
    # def save


if __name__ == '__main__':
    account = BankAccount(1000)
    # print(account.balance)    # error
    # print(account.__balance)  # error
    # account.get() # ok
