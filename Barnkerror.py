class InsufficientBalanceError(Exception):
    def __init__(self, balance):
        self.balance = balance
balance = 5000
try:
    amount=int(input("Enter amount"))
    if amount > balance:
        raise InsufficientBalanceError(balance)
    else:
        print("Successful balance is ",amount-balance)
except InsufficientBalanceError as e:
    print("Invalid Amount")