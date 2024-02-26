import pytest
from atm.user_account import UserAccount
from atm.account_history import AccountHistory

def test_user_account_initialization():
    account = {'ACCOUNT_ID': '123', 'PIN': '456', 'BALANCE': '100'}
    user_account = UserAccount(account)
    assert user_account.account_id == '123'
    assert user_account.pin == '456'
    assert user_account.balance == 100.0
    assert user_account.overdrawn == False
    assert user_account.account_history == []

def test_withdraw():
    account = {'ACCOUNT_ID': '123', 'PIN': '456', 'BALANCE': '100'}
    user_account = UserAccount(account)
    user_account.withdraw(20)
    assert user_account.balance == 80.0
    assert isinstance(user_account.account_history[0], AccountHistory)

def test_deposit():
    account = {'ACCOUNT_ID': '123', 'PIN': '456', 'BALANCE': '100'}
    user_account = UserAccount(account)
    user_account.deposit(20)
    assert user_account.balance == 120.0
    assert isinstance(user_account.account_history[0], AccountHistory)
