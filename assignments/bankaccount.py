class BankAccount():     #declare bank classs

    def __init__(self,name,email):  #use init and self to begin
        self.name = name    #gave accounts names and emails
        self.email = email
        self.user_balance = 0   #starting balance
        self.interest_rate = .02    #interest rate amount

    def balance(self):  #balance of bank account
        print(f"{self.name} has {self.user_balance}")
        return self

    def make_withdrawal(self,amount):  #allows money to be withdrawn 
        self.user_balance -= amount
        print(f"{self.name} withdrew {amount}")     #prints updated balance
        self.balance()  
        return self

    def make_deposit(self,amount): #allows deposit into account
        self.user_balance += amount
        print(f"{self.name} deposited {amount}")    #prints updated balance
        self.balance() 
        return self
    
    
    def interest_rate(self):        #interest rate calculation
        self.balance *= (self.interest_rate + 1)
        print(self.balance)     #print interest rate
        return self

colin = BankAccount("Colin Scott", "colin.scott@email.com")  #users bank accounts and info    
lexi = BankAccount("Lexi Anne", "lexi.anne@email.com")

#chained commands
colin.make_deposit(100).make_deposit(9999).make_deposit(500).make_withdrawal(1000).interest_rate.balance
lexi.make_deposit(5000).make_deposit(500).make_withdrawal(100).make_withdrawal(340).make_withdrawal(49).make_withdrawal(54).interest_rate.balance