class AccountHistory:
    def __init__(self, date_time, amount, balance):
        self.date_time = date_time
        self.amount = amount
        self.balance = balance

    def __str__(self):
        str_amount = " -$" if self.amount < 0 else " $"
        return self.date_time.strftime("%Y-%m-%d %H:%M:%S") + str_amount  + '{:.2f}'.format(self.amount).lstrip("-") + " ${:.2f}".format(self.balance)
        