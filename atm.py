import logging
import pandas as pd
from user_account import UserAccount

logger = logging.getLogger(__name__)

class Atm:
    def __init__(self, total_money:float=10000):
        self.total_money = total_money
        self.user_accounts = {}
        self.current_account:UserAccount = None
    

    def authorize(self, account_id:str, pin:str):
        if account_id in self.user_accounts.keys():
            actual_pin = self.user_accounts.get(account_id)
            logger.debug(actual_pin)
            if actual_pin != None and actual_pin.pin == pin:
                logger.info(account_id + ' successfully authorized.')
                self.current_account = actual_pin
            else:
                logger.info('Authorization failed.')
        else:
            logger.info('Account Not Found. Authorization failed.')
    # update user_account details
    # set current_account to None
    def log_out(self):
        if self.current_account is None:
            logger.info('No account is currently authorized.')
        else:
            self.user_accounts.add(self.current_account)
            logger.info('Account ' + self.current_account.account_id + ' logged out.')
            self.current_account = None
    
    def withdraw(self, value):
        if self.current_account == None:
            logger.info('Authorization required.')
            return
        elif self.current_account.overdrawn:
            logger.info('Your account is overdrawn! You may not make a withdrawal at this time.')
            return
        elif self.total_money == 0:
            logger.info('Unable to process your withdrawal at this time.')
            return
        
        withDrawalAmount = float(value)
        
        if withDrawalAmount > self.total_money:
            logger.info('Unable to dispense full amount requested at this time.')
            withDrawalAmount = self.total_money
        if withDrawalAmount % 20 == 0:
            # update the balance for account
            self.current_account.withdraw(withDrawalAmount)
            # update total money in the ATM
            self.total_money -= withDrawalAmount
            self.current_account.show_balance()
        else:
            logger.info('Withdrawal amount must be a multiple of $20.')
    
    def deposit(self, value):
        if self.current_account == None:
            logger.info('Authorization required.')
        else:
            float_deposit = float(value)
            # update the balance for account
            self.current_account.deposit(float_deposit)
            # update total money in the ATM
            self.total_money += float_deposit
            self.current_account.show_balance()
    
    def balance(self):
        if self.current_account == None:
            logger.info('Authorization required.')
        else:
            self.current_account.show_balance()
    
    def history(self):
        if self.current_account == None:
            logger.info('Authorization required.')
        else:
            self.current_account.history()
    
    def parse_user_accounts(self, file_name):
        df = pd.read_csv(file_name, dtype=str)
        # go there each row and add the UserAccount
        logger.debug(df)
        for index, row in df.iterrows():
            tempAccount = UserAccount(row)
            logger.debug(tempAccount)
            self.user_accounts.update({tempAccount.account_id: tempAccount})
        