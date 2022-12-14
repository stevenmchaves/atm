class AccountHistory:
    def __init__(self, date_time, amount, balance):
        self.date_time = date_time
        self.amount = amount
        self.balance = balance

    def __str__(self):
        return self.date_time.strftime("%Y-%m-%d %H:%M:%S") + " ${:.2f} ${:.2f}".format(self.amount, self.balance)
        