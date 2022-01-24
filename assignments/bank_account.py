class User():

    def __init__(self,name,email_address):
        self.account = BankAccount()
        self.name = name
        self.email_address = email_address

    def make_deposit(self, amount):
        # self.account.balance += amount
        self.account.deposit_into_account(amount)
        return self

    def make_withdraw(self,amount):
        self.withdraw_from_account(amount)
        return self

    def display(self):
        self.display_account_info(amount)
        return self

class BankAccount():

    def __init__(self,balance = 0, interest_rate = .02):
        self.balance = balance
        self.interest_rate = interest_rate
        
    def deposit_into_account(self,amount):
        self.balance += amount
        return self

    def withdraw_from_account(self,amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yeild_interest(self):
        self.balance *= (self.interest_rate + 1)
        print(self.balance)
        return self
        

colin = BankAccount("Colin Scott","colinscott@email.com")
lexi = BankAccount("Lexi Anne", "lexianne@email.com")

colin.deposit_into_account(9999).deposit_into_account(500).deposit_into_account(4500).display_account_info
