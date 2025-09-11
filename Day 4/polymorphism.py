class Payment:
    def pay(self,amount):
        print(f'The amount is :{amount} and we are in base class')

class CashPayment(Payment):
    def pay(self,amount):
        print(f'Paid {amount} using cash')

class CardPayment(Payment):
    def pay(self,amount):
        print(f'Paid {amount} using credit/debit card')

class UPIPayment(Payment):
    def pay(self,amount):
        print(f'Paid {amount} using UPI')

list=[CashPayment(),CardPayment(),UPIPayment()]
for x in list:
    x.pay(1000)


