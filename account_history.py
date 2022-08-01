class AccountHistory:
    def __init__(self, date_time, amount, balance):
        self.date_time = date_time
        self.amount = amount
        self.balance = balance
    
    def show_history(self):
        print('{self.date_time} ${0.2f} ${0.2f}', self.amount, self.balance)