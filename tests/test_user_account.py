import pytest
from atm.user_account import UserAccount, OVERDRAFT_FEE

user_account = UserAccount({'ACCOUNT_ID': '1234', 'PIN': '5678', 'BALANCE': '0.00'})
    
def test_invalid_user_account():
    with pytest.raises(KeyError):
        UserAccount({})
    
def test_user_account():
    assert user_account.account_id == '1234'
    assert user_account.pin == '5678'
    assert user_account.balance == 0.00
    assert user_account.account_history == []
    assert user_account.overdrawn is False

def test_show_balance_zero(capsys):
    user_account.show_balance()
    assert 'Current balance: $0.00' in str(capsys.readouterr()) 
    
def test_show_balance(capsys):
    user_account.deposit(20)
    user_account.show_balance()
    assert 'Current balance: $20.00' in str(capsys.readouterr()) 

def test_show_balance_negative(capsys):
    temp_user_account = UserAccount({'ACCOUNT_ID': '1234', 'PIN': '5678', 'BALANCE': '0.00'})
    temp_user_account.withdraw(20)
    temp_user_account.overdrawn == True
    temp_user_account.show_balance()
    assert 'Current balance: -$25.00' in str(capsys.readouterr()) 


def test_withdrawal_prevent(capsys):
    temp_user_account = UserAccount({'ACCOUNT_ID': '1234', 'PIN': '5678', 'BALANCE': '80.00'})
    temp_user_account.withdraw(100)
    temp_user_account.withdraw(100)
    assert 'Your account is overdrawn! You may not make a withdrawal at this time.' in str(capsys.readouterr())

def test_withdrawal_fee(capsys):
    temp_user_account = UserAccount({'ACCOUNT_ID': '1234', 'PIN': '5678', 'BALANCE': '80.00'})
    temp_user_account.withdraw(260)
    stdouterr = str(capsys.readouterr())
    assert 'Amount dispensed: $260' in stdouterr
    assert 'You have been charged an overdraft charge of $' + str(OVERDRAFT_FEE) in stdouterr
    
def test_withdrawal(capsys):
    user_account.withdraw(200)
    assert 'Amount dispensed: $200' in str(capsys.readouterr()) 

def test_deposit(capsys):
    user_account.deposit(30000.55)
    assert '' in capsys.readouterr() 
        
def test_history_none(capsys):
    temp_user_account = UserAccount({'ACCOUNT_ID': '1234', 'PIN': '5678', 'BALANCE': '0.00'})
    temp_user_account.history()
    assert 'No history found' in str(capsys.readouterr()) 

def test_history_one(capsys):
    '''Perform to one atm operation on the account and confirm history entry'''
    temp_user_account = UserAccount({'ACCOUNT_ID': '1234', 'PIN': '5678', 'BALANCE': '50.00'})
    temp_user_account.deposit(30.55)
    temp_user_account.history()
    assert '$30.55 $80.55' in str(capsys.readouterr()) 
        
def test_history_two(capsys):
    '''Perform to atm operations on the account and confirm history entries'''
    temp_user_account = UserAccount({'ACCOUNT_ID': '1234', 'PIN': '5678', 'BALANCE': '0.00'})
    temp_user_account.deposit(30)
    temp_user_account.withdraw(20)
    temp_user_account.history()
    stdouterr = str(capsys.readouterr())
    assert '$30.00 $30.00' in stdouterr
    assert '-$20.00 $10.00' in stdouterr 