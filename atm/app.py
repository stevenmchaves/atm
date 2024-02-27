import logging
from flask import jsonify
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
                return jsonify({'message': f'Account {account_id} successfully authorized.'}), 200
            else:
                print('Authorization failed.')
                return jsonify({'message': 'Authorization failed.'}), 401
        else:
            print('Account Not Found. Authorization failed.')
            return jsonify({'message': 'Account Not Found. Authorization failed.'}), 404

    # update user_account details
    # set current_account to None
    def log_out(self):
        if self.current_account is None:
            print('No account is currently authorized.')
            return jsonify({'message': 'No account is currently authorized.'}), 401
        else:
            self.user_accounts[self.current_account.account_id] = self.current_account
            print('Account ' + self.current_account.account_id + ' logged out.')
            self.current_account = None
            return jsonify({'message': f'Account {self.current_account.account_id} logged out.'}), 200

    def withdraw(self, value):
        if self.current_account == None:
            print('Authorization required.')
            return jsonify({'message': 'Authorization required.'}), 401
        elif self.total_money == 0:
            return jsonify({'message': 'Unable to process your withdrawal at this time.'}), 400

        withdrawal_amount = min(value, self.total_money)
        if withdrawal_amount % 20 == 0:
            # Update the balance for the account
            self.current_account.withdraw(withdrawal_amount)
            # Update total money in the ATM
            self.total_money -= withdrawal_amount
            return jsonify({'message': f'Withdrawal successful. Remaining balance: {self.total_money}'}), 200
        else:
            return jsonify({'message': 'Withdrawal amount must be a multiple of 20.'}), 400

    def deposit(self, value):
        if self.current_account is None:
            return jsonify({'message': 'Authorization required.'}), 401
        else:
            float_deposit = float(value)
            if float_deposit > 0:
                # Update the balance for the account
                self.current_account.deposit(float_deposit)
                # Update total money in the ATM
                self.total_money += float_deposit
                return jsonify({'message': f'Deposit successful. New balance: {self.current_account.balance}'}), 200
            else:
                return jsonify({'message': 'Deposit amount needs to be greater than 0.'}), 400
    
    def balance(self):
        if self.current_account == None:
            return jsonify({'message': 'Authorization required.'}), 401
        else:
            return jsonify({'balance': self.current_account.balance}), 200
    
    def history(self):
        # Get transaction history
        if self.current_account is None:
            return jsonify({'message': 'Authorization required.'}), 401
        else:
            # Assuming you have a method to retrieve transaction history for the current account
            # Replace with your actual implementation
            transaction_history = self.current_account.get_transaction_history()
            return jsonify({'history': transaction_history}), 200
    
    def parse_user_accounts(self, file_name):
        df = pd.read_csv(file_name, dtype=str)
        # go there each row and add the UserAccount
        logger.debug(df)
        for index, row in df.iterrows():
            temp_account = UserAccount(row)
            logger.debug(temp_account)
            self.user_accounts.update({temp_account.account_id: temp_account})
    