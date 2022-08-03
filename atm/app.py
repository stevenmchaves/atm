import logging
import pandas as pd
from atm.user_account import UserAccount

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
                print(account_id + ' successfully authorized.')
                self.current_account = actual_pin
            else:
                print('Authorization failed.')
        else:
            print('Account Not Found. Authorization failed.')
    
    # update user_account details
    # set current_account to None
    def log_out(self):
        if self.current_account is None:
            print('No account is currently authorized.')
        else:
            self.user_accounts[self.current_account.account_id] = self.current_account
            print('Account ' + self.current_account.account_id + ' logged out.')
            self.current_account = None
    
    def withdraw(self, value):
        if self.current_account == None:
            print('Authorization required.')
            return
        elif self.total_money == 0:
            print('Unable to process your withdrawal at this time.')
            return
        
        withdrawal_amount = float(value)
        
        if withdrawal_amount > self.total_money:
            print('Unable to dispense full amount requested at this time.')
            withdrawal_amount = self.total_money
        if withdrawal_amount % 20 == 0:
            # update the balance for account
            self.current_account.withdraw(withdrawal_amount)
            # update total money in the ATM
            self.total_money -= withdrawal_amount
            self.current_account.show_balance()
        else:
            print('Withdrawal amount must be a multiple of $20.')
    
    def deposit(self, value):
        if self.current_account == None:
            print('Authorization required.')
        else:
            float_deposit = float(value)
            if float_deposit > 0:
                # update the balance for account
                self.current_account.deposit(float_deposit)
                # update total money in the ATM
                self.total_money += float_deposit
                self.current_account.show_balance()
            else:
                print('Deposit amount needs to be greater than 0.')
    
    def balance(self):
        if self.current_account == None:
            print('Authorization required.')
        else:
            self.current_account.show_balance()
    
    def history(self):
        if self.current_account == None:
            print('Authorization required.')
        else:
            self.current_account.history()
    
    def parse_user_accounts(self, file_name):
        df = pd.read_csv(file_name, dtype=str)
        # go there each row and add the UserAccount
        logger.debug(df)
        for index, row in df.iterrows():
            temp_account = UserAccount(row)
            logger.debug(temp_account)
            self.user_accounts.update({temp_account.account_id: temp_account})
        