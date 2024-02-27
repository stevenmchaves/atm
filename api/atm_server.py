# Following code was generated from Microsoft Copilot
# I provided atm.py as a started point until it reached the 2000 characters

from flask import Flask, jsonify, request

app = Flask(__name__)

class UserAccount:
    def __init__(self, account_id, pin):
        self.account_id = account_id
        self.pin = pin
        # Add any other necessary attributes for user accounts

# Initialize ATM
total_money = 10000
user_accounts = {}
current_account = None

@app.route('/authorize', methods=['POST'])
def authorize():
    data = request.get_json()
    account_id = data.get('account_id')
    pin = data.get('pin')

    if account_id in user_accounts:
        actual_pin = user_accounts.get(account_id)
        if actual_pin is not None and actual_pin.pin == pin:
            global current_account
            current_account = actual_pin
            return jsonify({'message': f'Account {account_id} successfully authorized.'}), 200
        else:
            return jsonify({'message': 'Authorization failed.'}), 401
    else:
        return jsonify({'message': 'Account Not Found. Authorization failed.'}), 404

@app.route('/logout', methods=['POST'])
def log_out():
    global current_account
    if current_account is None:
        return jsonify({'message': 'No account is currently authorized.'}), 401
    else:
        user_accounts[current_account.account_id] = current_account
        current_account = None
        return jsonify({'message': f'Account {current_account.account_id} logged out.'}), 200

@app.route('/withdraw', methods=['POST'])
def withdraw():
    data = request.get_json()
    value = float(data.get('value'))

    if current_account is None:
        return jsonify({'message': 'Authorization required.'}), 401
    elif total_money == 0:
        return jsonify({'message': 'Unable to process your withdrawal at this time.'}), 400

    withdrawal_amount = min(value, total_money)
    if withdrawal_amount % 20 == 0:
        # Update the balance for the account
        current_account.withdraw(withdrawal_amount)
        # Update total money in the ATM
        global total_money
        total_money -= withdrawal_amount
        return jsonify({'message': f'Withdrawal successful. Remaining balance: {total_money}'}), 200
    else:
        return jsonify({'message': 'Withdrawal amount must be a multiple of 20.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
