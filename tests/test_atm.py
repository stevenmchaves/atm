import datetime
import pytest
from atm.app import Atm

now_datetime = datetime.datetime.now()
local_atm = Atm()

local_atm_diff = Atm(5000)

def invalid_test_atm():
    with pytest.raises(TypeError):
        Atm({})

def invalid_test_atm_float():
    with pytest.raises(TypeError):
        Atm("h20480")
    
def test_atm():
    assert local_atm.total_money == 10000
    assert local_atm.user_accounts == {}
    assert local_atm.current_account == None

def test_authorize_no_accounts(capsys):
    local_atm.authorize('2222', '2222')
    assert 'Account Not Found. Authorization failed.\n' in capsys.readouterr()

def test_authorize_invalid_pin(capsys):
    local_atm.parse_user_accounts('sample_accounts.csv')
    local_atm.authorize("2001377812", '2222')
    assert 'Authorization failed.\n' in capsys.readouterr()   

def test_authorize(capsys):
    local_atm.parse_user_accounts('sample_accounts.csv')
    local_atm.authorize("2001377812", '5950')
    assert '2001377812 successfully authorized.\n' in capsys.readouterr()  

def test_logout_authorize(capsys):
    temp_local_atm = Atm()
    temp_local_atm.parse_user_accounts('sample_accounts.csv')
    temp_local_atm.authorize("2001377812", '5950')
    temp_local_atm.log_out()
    assert 'Account 2001377812 logged out.' in str(capsys.readouterr())
    
def test_logout_no_authorize(capsys):
    temp_local_atm = Atm()
    temp_local_atm.log_out()
    assert 'No account is currently authorized.\n' in capsys.readouterr()

def test_history_no_authorize(capsys):
    temp_local_atm = Atm()
    temp_local_atm.history()
    assert 'Authorization required.\n' in capsys.readouterr()

def test_history_no(capsys):
    temp_local_atm = Atm()
    temp_local_atm.parse_user_accounts('sample_accounts.csv')
    temp_local_atm.authorize("2001377812", '5950')
    temp_local_atm.history()
    assert 'No history found' in str(capsys.readouterr())
    
def test_history(capsys):
    temp_local_atm = Atm()
    temp_local_atm.parse_user_accounts('sample_accounts.csv')
    temp_local_atm.authorize("2001377812", '5950')
    temp_local_atm.withdraw(40)
    temp_local_atm.history()
    assert '$-40.00 $20.00' in str(capsys.readouterr())

def test_withdraw_no_authorize(capsys):
    temp_local_atm = Atm()
    temp_local_atm.withdraw(4)
    assert 'Authorization required.\n' in capsys.readouterr()

def test_deposit_no_authorize(capsys):
    temp_local_atm = Atm()
    temp_local_atm.deposit(12)
    assert 'Authorization required.\n' in capsys.readouterr()

def test_balance_no_authorize(capsys):
    temp_local_atm = Atm()
    temp_local_atm.balance()
    assert 'Authorization required.\n' in capsys.readouterr()
    
def test_withdraw_invalid_multiple(capsys):
    temp_local_atm = Atm()
    temp_local_atm.parse_user_accounts('sample_accounts.csv')
    temp_local_atm.authorize("2001377812", '5950')
    temp_local_atm.withdraw(10)
    assert 'Withdrawal amount must be a multiple of $20.' in str(capsys.readouterr())

def test_withdraw_invalid_amount():
    temp_local_atm = Atm()
    temp_local_atm.parse_user_accounts('sample_accounts.csv')
    temp_local_atm.authorize("2001377812", '5950')
    with pytest.raises(ValueError):
        temp_local_atm.withdraw('A10')

def test_withdraw_too_much(capsys):
    temp_local_atm = Atm()
    temp_local_atm.parse_user_accounts('sample_accounts.csv')
    temp_local_atm.authorize("2001377812", '5950')
    temp_local_atm.withdraw('20000')
    stdout_err = str(capsys.readouterr())
    assert 'Unable to dispense full amount requested at this time.' in stdout_err
    assert 'Amount dispensed: $10000' in stdout_err
    assert 'Amount dispensed: $20000' not in stdout_err
    
def test_withdraw_out_of_money(capsys):
    temp_local_atm = Atm()
    temp_local_atm.parse_user_accounts('sample_accounts.csv')
    temp_local_atm.authorize("1434597300", '4557')
    temp_local_atm.withdraw('10000')
    temp_local_atm.log_out()
    stdout_err = str(capsys.readouterr())
    assert 'Amount dispensed: $10000' in stdout_err
    temp_local_atm.authorize("2001377812", '5950')
    temp_local_atm.withdraw('20')
    stdout_err = str(capsys.readouterr())
    assert 'Unable to process your withdrawal at this time.' in stdout_err
    assert 'Amount dispensed: $20' not in stdout_err

def test_deposit_invalid_amount(capsys):
    temp_local_atm = Atm()
    temp_local_atm.parse_user_accounts('sample_accounts.csv')
    temp_local_atm.authorize("2001377812", '5950')
    with pytest.raises(ValueError):
        temp_local_atm.deposit('A10')
    
def test_deposit_negative_amount(capsys):
    temp_local_atm = Atm()
    temp_local_atm.parse_user_accounts('sample_accounts.csv')
    temp_local_atm.authorize("2001377812", '5950')
    temp_local_atm.deposit(-10)
    assert 'Deposit amount needs to be greater than 0.' in str(capsys.readouterr())


def test_balance(capsys):
    temp_local_atm = Atm()
    temp_local_atm.parse_user_accounts('sample_accounts.csv')
    temp_local_atm.authorize("2001377812", '5950')
    temp_local_atm.withdraw(40)
    temp_local_atm.balance()
    assert 'Current balance: $20.00' in str(capsys.readouterr())
