class BankAccount():     #declare class

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.user_balance = 0
        self.interest_rate = .02

    def balance(self): #user balance is stored here
        print(f"{self.name} has {self.user_balance}")
        return self

    def make_withdrawal(self,amount): #user can withdrawal money here
        self.user_balance -= amount
        print(f"{self.name} withdrew {amount}")
        self.balance()  #shows balance after each action
        return self

    def make_deposit(self,amount):  #user can make a deposit here
        self.user_balance += amount
        print(f"{self.name} deposited {amount}")
        self.balance()  #shows balance after each action
        return self
    
    
    def interest_rate(self): #allows users to transfer money to another account by selecting the account name and ammount they want transferred. It then shows the remaining balance of the first account and new balance of the second
        self.balance *= (self.interest_rate + 1)
        print(self.balance)
        return self

colin = BankAccount("Colin Scott", "colin.scott@email.com")    #3 iterations of User class
lexi = BankAccount("Lexi Anne", "lexi.anne@email.com")


colin.make_deposit(100).make_deposit(9999).make_deposit(500).make_withdrawal(1000).interest_rate.balance
lexi.make_deposit(5000).make_deposit(500).make_withdrawal(100).make_withdrawal(340).make_withdrawal(49).make_withdrawal(54).interest_rate.balance