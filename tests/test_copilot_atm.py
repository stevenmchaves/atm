# Test class created by Microsoft Copilot
# 02/26/2024
import pytest

# This was the original import statement from Microsoft Copilot
# from atm import Atm
# This is the correct one
from atm.app import Atm
from atm.user_account import UserAccount

def test_atm_initialization():
    atm = Atm()
    assert atm.total_money == 10000
    assert atm.user_accounts == {}
    assert atm.current_account is None

def test_authorize():
    atm = Atm()
    # This did not work as Copilot assumed account_id was a member variable
    # user_account = UserAccount(account_id='123', pin='456')
    # This works
    user_account = UserAccount({'ACCOUNT_ID': '123', 'PIN': '456', 'BALANCE': '0.00'})
    atm.user_accounts['123'] = user_account
    atm.authorize('123', '456')
    assert atm.current_account == user_account

def test_log_out():
    atm = Atm()
    # This did not work as Copilot assumed account_id was a member variable
    # user_account = UserAccount(account_id='123', pin='456')
    # This works
    user_account = UserAccount({'ACCOUNT_ID': '123', 'PIN': '456', 'BALANCE': '0.00'})
    atm.user_accounts['123'] = user_account
    atm.authorize('123', '456')
    atm.log_out()
    assert atm.current_account is None

def test_withdraw():
    atm = Atm(total_money=200)
    # This did not work as Copilot assumed account_id was a member variable
    # user_account = UserAccount(account_id='123', pin='456', balance=100)
    # This works
    user_account = UserAccount({'ACCOUNT_ID': '123', 'PIN': '456', 'BALANCE': '100'})
    atm.user_accounts['123'] = user_account
    atm.authorize('123', '456')
    atm.withdraw(20)
    assert atm.total_money == 180
    assert atm.current_account.balance == 80

def test_deposit():
    atm = Atm(total_money=200)
    # This did not work as Copilot assumed account_id was a member variable
    # user_account = UserAccount(account_id='123', pin='456', balance=100)
    # This works
    user_account = UserAccount({'ACCOUNT_ID': '123', 'PIN': '456', 'BALANCE': '100'})
    atm.user_accounts['123'] = user_account
    atm.authorize('123', '456')
    atm.deposit(20)
    assert atm.total_money == 220
    assert atm.current_account.balance == 120
