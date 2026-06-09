class CreditCard:
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")
class UPI:
    def pay(self, amount):
        print("Paid", amount, "using UPI")
class NetBanking:
    def pay(self, amount):
        print("Paid", amount, "using Net Banking")
class PaymentFactory:
    @staticmethod
    def paymenttype(method):
        if method == "creditcard":
            return CreditCard()
        elif method == "upi":
            return UPI()
        elif method == "netbanking":
            return NetBanking()
        else:
            return None
method = input("Enter payment method: ").lower()
amount = float(input("Enter amount: "))
payment = PaymentFactory.paymenttype(method)
if payment:
    payment.pay(amount)
else:
    print("Invalid Payment Method")