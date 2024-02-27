# Following code was generated from Microsoft Copilot
# I provided atm.py as a started point until it reached the 2000 characters
from flask import Flask, request
import logging

from app import Atm

logger = logging.getLogger(__name__)
flask_app = Flask(__name__)
flask_app.debug = True

# Initialize ATM
atm_instance = Atm()

@flask_app.route('/authorize', methods=['POST'])
def authorize():
    data = request.get_json()
    account_id = data.get('account_id')
    pin = data.get('pin')
    return atm_instance.authorize(account_id, pin)           

@flask_app.route('/logout', methods=['POST'])
def log_out():
    return atm_instance.log_out()

@flask_app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()
    value = float(data.get('value'))
    return atm_instance.withdraw(value)

@flask_app.route('/deposit', methods=['POST'])
def deposit():
    data = request.get_json()
    value = data.get('amount')
    return atm_instance.deposit(value)

@flask_app.route('/balance', methods=['GET'])
def get_balance():
    return atm_instance.balance()

@flask_app.route('/history', methods=['GET'])
def get_history():
    return atm_instance.history()

if __name__ == '__main__':
    # Load user accounts from CSV file
    atm_instance.parse_user_accounts('../sample_accounts.csv')  # Replace with your actual CSV file name
    flask_app.run(debug=True)
