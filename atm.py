from user_account import UserAccount
class Atm:
    def __init(self, total_money:float=10000):
        self.total_money = total_money
        self.user_accounts = set()
        self.current_account:UserAccount = None
    
    def set_current_account(self, account_id):
        if self.current_account != None:
            raise Exception('Should only set current_account after log out!')
        self.current_account = self.users_accounts.get(account_id)
    
    # update user_account details
    # set current_account to None
    def log_out(self):
        self.user_accounts.add(self.current_account)
        self.current_account = None
    
    def withdraw(self, value):
        if self.current_account == None:
            raise Exception('Need to authorize first!')
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
            raise Exception('Need to authorize first!')
        
        # update the balance for account
        self.current_account.deposit(value)
        # update total money in the ATM
        self.total_money += value
    
    def balance(self):
        if self.current_account == None:
            raise Exception('Need to authorize first!')
    
        self.current_account.show_balance()
    
    def history(self):
        if self.current_account == None:
            raise Exception('Need to authorize first!')
        self.current_account.history()