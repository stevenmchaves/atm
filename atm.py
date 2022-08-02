import pandas as pd
from user_account import UserAccount

class Atm:
    def __init__(self, total_money:float=10000):
        self.total_money = total_money
        self.user_accounts = {}
        self.current_account:UserAccount = None
    

    def authorize(self, account_id:int, pin:int):
        if account_id in self.user_accounts.keys():
            actual_pin = self.user_accounts.get(account_id)
            print(actual_pin)
            if actual_pin != None and actual_pin.pin == pin:
                print(account_id + ' successfully authorized.')
                self.current_account = actual_pin
            else:
                print('Authorization failed.')
    
    # update user_account details
    # set current_account to None
    def log_out(self):
        if self.current_account is None:
            print('No account is currently authorized.')
        else:
            self.user_accounts.add(self.current_account)
            print('Account ' + self.current_account.account_id + ' logged out.')
            self.current_account = None
    
    def withdraw(self, value):
        if self.current_account == None:
            print('Authorization required.')
        elif self.current_account.overdrawn:
            print('Your account is overdrawn! You may not make a withdrawal at this time.')
            return
        elif self.total_money == 0:
            print('Unable to process your withdrawal at this time.')
            return
        elif value > self.total_money:
            print('Unable to dispense full amount requested at this time.')
            value = self.total_money
        
        if value % 20 == 0:
            # update the balance for account
            self.current_account.withdraw(value)
            # update total money in the ATM
            self.total_money -= value
            self.current_account.show_balance()
        else:
            print('Withdrawal amount must be a multiple of $20.')
    
    def deposit(self, value):
        if self.current_account == None:
            print('Authorization required.')
        
        # update the balance for account
        self.current_account.deposit(value)
        # update total money in the ATM
        self.total_money += value
    
    def balance(self):
        if self.current_account == None:
            print('Authorization required.')
    
        self.current_account.show_balance()
    
    def history(self):
        if self.current_account == None:
            print('Authorization required.')
        self.current_account.history()
    
    def parse_user_accounts(self, file_name):
        df = pd.read_csv(file_name)
        # go there each row and add the UserAccount
        print(df)
        for index, row in df.iterrows():
            tempAccount = UserAccount(row)
            print(tempAccount)
            self.user_accounts.update({tempAccount.account_id: tempAccount})
        