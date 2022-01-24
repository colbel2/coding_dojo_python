class User():  #user class defined

    def __init__(self,name,email):      
        self.name = name
        self.email = email
        self.user_account = BankAccount()       #connecting user account to bank account

    def make_deposit(self, amount):
        self.user_account.deposit(self.name, amount) 
        print(f"{self.name} deposited ${amount}")
        
    
    def make_withdrawal(self, amount):
        self.user_account.withdraw(self.name,amount)
        print(f"{self.name} withdrew ${amount}")


    def display_balance(self):
        self.user_account.display_account_info()
        

    def interest(self):
        self.user_account.yeild_interest()
        

class BankAccount():  #bank class defined
    # accounts = []
    def __init__(self,balance = 0,int_rate = .02):
        self.int_rate = int_rate
        self.balance = balance
        # BankAccount.accounts.append(self)

    def deposit(self,name, amount):
        self.balance += amount
        print(f'The bank adds ${amount} to {name}')
        return self

    def withdraw(self,name,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self



colin = User("Colin Scott", "colinscott@email.com")

colin.display_balance()
colin.interest()

colin.make_deposit(50)
colin.make_withdrawal(25)
colin.display_balance()