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

def test_user_account_invalid_pin(capsys):
    local_atm.parse_user_accounts('sample_accounts.csv')
    local_atm.authorize("2001377812", '2222')
    assert 'Account Not Found. Authorization failed.' in capsys.readouterr()   