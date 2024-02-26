import datetime
import logging
from atm.account_history import AccountHistory
OVERDRAFT_FEE = 5

logger = logging.getLogger(__name__)
class UserAccount:
    '''Class to describe User Account details
    '''
    def __init__(self, account, overdrawn=False):
        self.account_id = str(int(account['ACCOUNT_ID']))
        # because of the possibility of leading zeros needs to be string
        self.pin = str(account['PIN'])
        self.balance = float(account['BALANCE'])
        self.overdrawn = overdrawn
        self.account_history = []
    
    def __str__(self):
        return '"' + self.account_id + '" "' + str(self.pin) + '" ' + str(self.balance) + ' overdrawn=' + str(self.overdrawn)
    
    
    def show_balance(self):
        str_sign_balance = "-$" if self.balance < 0 else "$"
        out = "Current balance: " + str_sign_balance  + "{:.2f}".format(self.balance).lstrip("-") 
        print(out)  
        logger.debug(out)
    
    def withdraw(self, amount:float):
        applyFee = False
        if self.overdrawn:
            logger.info('Your account is overdrawn! You may not make a withdrawal at this time.')
            print('Your account is overdrawn! You may not make a withdrawal at this time.')
            return  
        elif self.balance < amount:
            self.overdrawn = True
            applyFee = True
        print('Amount dispensed: $' + str(int(amount)))
        # apply overdraft fee
        if applyFee:
            logger.info('You have been charged an overdraft charge of $' + str(OVERDRAFT_FEE))
            print('You have been charged an overdraft charge of $' + str(OVERDRAFT_FEE))
            amount += OVERDRAFT_FEE
        
        # update balance
        self.balance -= amount
        self.account_history.append(AccountHistory(datetime.datetime.now(), -abs(amount), self.balance))
        
        
    def deposit(self, amount: float):
        # update balance
        self.balance += amount
        self.account_history.append(AccountHistory(datetime.datetime.now(), amount, self.balance))
    
    def history(self):
        if len(self.account_history) == 0:
            logger.info('No history found')
            print('No history found')
        else:
            for record in reversed(self.account_history):
                logger.info(record)
                print(record)