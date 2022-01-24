class User:     #declare class

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.user_balance = 0

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
    
    
    def transfer_money(self, User, amount): #allows users to transfer money to another account by selecting the account name and ammount they want transferred. It then shows the remaining balance of the first account and new balance of the second
        print(f"Transfer {self.name} to {User.name} for {amount}")
        self.make_withdrawal(amount)
        User.make_deposit(amount)
        return self

colin = User("Colin Scott", "colin.scott@email.com")    #3 iterations of User class
lexi = User("Lexi Anne", "lexi.anne@email.com")
rachel = User("Rachel Kaye", "rachel.kaye@email.com")

colin.make_deposit(100).make_deposit(9000).make_deposit(700).make_withdrawal(1000).transfer_money(lexi,255)




lexi.make_deposit(5000).make_deposit(9000).make_withdrawal(200).make_withdrawal(1000)




rachel.make_deposit(5000).make_withdrawal(7000)

