# Generated with Microsoft Copilot with knowledge of UserAccount class
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
    account = {'ACCOUNT_ID': '123', 'PIN': '456', 'BALANCE': '100'}
    user_account = UserAccount(account)
    atm.user_accounts['123'] = user_account
    atm.authorize('123', '456')
    assert atm.current_account == user_account

def test_log_out():
    atm = Atm()
    account = {'ACCOUNT_ID': '123', 'PIN': '456', 'BALANCE': '100'}
    user_account = UserAccount(account)
    atm.user_accounts['123'] = user_account
    atm.authorize('123', '456')
    atm.log_out()
    assert atm.current_account is None

def test_withdraw():
    atm = Atm(total_money=200)
    account = {'ACCOUNT_ID': '123', 'PIN': '456', 'BALANCE': '100'}
    user_account = UserAccount(account)
    atm.user_accounts['123'] = user_account
    atm.authorize('123', '456')
    atm.withdraw(20)
    assert atm.total_money == 180
    assert user_account.balance == 80

def test_deposit():
    atm = Atm(total_money=200)
    account = {'ACCOUNT_ID': '123', 'PIN': '456', 'BALANCE': '100'}
    user_account = UserAccount(account)
    atm.user_accounts['123'] = user_account
    atm.authorize('123', '456')
    atm.deposit(20)
    assert atm.total_money == 220
    assert user_account.balance == 120
