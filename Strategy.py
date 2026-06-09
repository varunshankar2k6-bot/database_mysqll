#Seperate classes for different ways
class CreditCardPayment:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")
class UPIPayment:
    def pay(self, amount):
        print("Paid", amount, "using UPI")
class NetBankingPayment:
    def pay(self, amount):
        print("Paid", amount, "using Net Banking")
class Payment:
    def __init__(self, strategy):
        self.strategy = strategy
    def make_payment(self, amount):
        self.strategy.pay(amount)
#Creating objects for diffeent methods
p1 = Payment(CreditCardPayment())
p1.make_payment(100)
p2 = Payment(UPIPayment())
p2.make_payment(200)
p3 = Payment(NetBankingPayment())
p3.make_payment(300)