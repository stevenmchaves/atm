#!/usr/bin/python
import logging
import signal
from prompt_toolkit import prompt

from atm import Atm

TIMEOUT = 120 # number of seconds (2 minutes)

logging.basicConfig(level = logging.DEBUG,format = '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s')

atm: Atm = Atm()
    
def logout_timeout(signum, frame):
    #called when read times out
    logging.info('Logging out of account id: ' + atm.current_account.account_id)
    atm.log_out()

signal.signal(signal.SIGALRM, logout_timeout)

def timeout_input():
        command = input("\nEnter ATM operation:\n")
        return command
        
def main():
    atm.parse_user_accounts('/home/stevenmchaves/atm/sample_accounts.csv')
    command: str = None
    while 1:
        # set alarm
        signal.alarm(TIMEOUT)
        try:
            command_syntax = timeout_input()
        except:
            continue
        
        # disable the alarm after success
        signal.alarm(0)
        
        if command_syntax is not None:
            command_syntax = command_syntax.split(' ')
        command = command_syntax[0]
        
        if command.lower() == "authorize":
            if len(command_syntax) == 3:
                atm.authorize(command_syntax[1], command_syntax[2])
            else:
                logging.info('Missing additional parameters for authorize.\nProper syntax:\n')
                logging.info('authorize <account_id> <pin>')
        elif command.lower() == "logout":
            atm.log_out()
        elif command.lower() == "deposit":
            atm.deposit(command_syntax[1])
        elif command.lower() == "withdrawal":
            atm.withdraw(command_syntax[1])
        elif command.lower() == "history":
            atm.history()
        elif command.lower() == "balance":
            atm.balance()
        elif command.lower() == "end":
            # exit loop to end program
            break
        else:
            logging.info("Not a valid command.")
        


if __name__ == "__main__":
    main()