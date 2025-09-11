class Bankaccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount
        print(f'deposited {amount} successfully')
    
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f'withdraw {amount} successfully')
        else:
            print("cannot withdraw")
    
    def get_balance(self):
        return self.__balance
    
class bankchild(Bankaccount):
    def __init__(self,balance):
        super().__init__(balance)
        print(self.get_balance())
    
obj=Bankaccount(0)
obj.deposit(5000)
obj.withdraw(9000)
w=bankchild(2000)
print('the balance is: ',obj.get_balance())