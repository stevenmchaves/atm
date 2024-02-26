# test_account_history.py
# Generated from Microsoft CoPilot
from datetime import datetime
import pytest
from atm.account_history import AccountHistory  # Replace with the actual module name

# Test case for initialization
def test_account_history_initialization():
    date_time = datetime(2024, 2, 26, 13, 2, 33)
    amount = 100.0
    balance = 500.0
    transaction = AccountHistory(date_time, amount, balance)
    assert transaction.date_time == date_time
    assert transaction.amount == amount
    assert transaction.balance == balance

# Test case for __str__ method
def test_account_history_str_method():
    date_time = datetime(2024, 2, 26, 13, 2, 33)
    amount = 100.0
    balance = 500.0
    transaction = AccountHistory(date_time, amount, balance)
    expected_output = "2024-02-26 13:02:33 $100.00 $500.00"
    assert str(transaction) == expected_output

# Test case for date formatting
def test_account_history_date_formatting():
    date_time = datetime(2024, 2, 26, 13, 2, 33)
    amount = 100.0
    balance = 500.0
    transaction = AccountHistory(date_time, amount, balance)
    assert transaction.date_time.strftime("%Y-%m-%d %H:%M:%S") == "2024-02-26 13:02:33"

# Test case for negative amount
def test_account_history_negative_amount():
    date_time = datetime(2024, 2, 26, 13, 2, 33)
    amount = -50.0
    balance = 500.0
    transaction = AccountHistory(date_time, amount, balance)
    expected_output = "2024-02-26 13:02:33 -$50.00 $500.00"
    assert str(transaction) == expected_output

# Test case for zero balance
def test_account_history_zero_balance():
    date_time = datetime(2024, 2, 26, 13, 2, 33)
    amount = 100.0
    balance = 0.0
    transaction = AccountHistory(date_time, amount, balance)
    expected_output = "2024-02-26 13:02:33 $100.00 $0.00"
    assert str(transaction) == expected_output
