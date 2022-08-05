import datetime
import pytest
from atm.account_history import AccountHistory

now_datetime = datetime.datetime.now()
account_history = AccountHistory(now_datetime, 5, 500)

account_history_negative = AccountHistory(now_datetime, 50, -500)

    
def test_invalid_account_history():
    with pytest.raises(TypeError):
        AccountHistory({})
    
def test_account_history():
    assert account_history.amount == 5
    assert account_history.balance == 500
    assert account_history.date_time == now_datetime

def test_account_history_negative():
    assert account_history_negative.amount == 50
    assert account_history_negative.balance == -500
    assert account_history_negative.date_time == now_datetime

def test_account_history_print(capsys):
    print(account_history)
    expected_out = now_datetime.strftime("%Y-%m-%d %H:%M:%S")  + ' $5.00 $500.00\n'
    assert expected_out in capsys.readouterr()