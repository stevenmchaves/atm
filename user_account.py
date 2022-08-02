import datetime
from account_history import show_history, AccountHistory
# Class to describe User Account details
OVERDRAFT_FEE = 5
class UserAccount:

    def __init__(self, account, overdrawn=False):
        self.account_id = account['account_id']
        self.pin = account['pin']
        self.balance = account['balance']
        self.overdrawn = overdrawn
        self.account_history = []
    
    
    def show_balance(self):    
        print('Current balance: ${0.2f}', self.balance)
    
    def withdraw(self, amount):
        applyFee = False
        if self.overdrawn:
            print('Your account is overdrawn! You may not make a withdrawal at this time.')
            return  
        elif self.balance < amount:
            self.overdrawn = True
            applyFee = True
        print('Amount dispensed: ${amount}')
        # apply overdraft fee
        if applyFee:
            print('You have been charged an overdraft charge of ${OVERDRAFT_FEE}')
            amount += OVERDRAFT_FEE
        
        # update balance
        self.balance -= amount
        self.account_history.append(AccountHistory(datetime.datetime.now(), -abs(amount), self.balance))
        
        
    def deposit(self, amount):
        # update balance
        self.balance += amount
        self.account_history.append(AccountHistory(datetime.datetime.now(), amount, self.balance))
    
    def history(self):
        if len(self.history) == 0:
            print('No history found')
        else:
            print(list(map(show_history, self.history)))