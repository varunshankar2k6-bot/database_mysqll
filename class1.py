class BankAccount:
#Defining the class BankAccount with three attributes: account_number, holder_name, and balance. The account_number is public, the holder_name is protected, and the balance is private. The class also has three methods: deposit, withdraw, and check_balance.
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number      # Public
        self._holder_name = holder_name           # Protected
        self.__balance = balance                  # Private
 #Defining the methods
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Deposit amount must be greater than 0")
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")
    def check_balance(self):
        print("Current Balance is:", self.__balance)

#Create object
acc1 = BankAccount(11, "Varun",10000)
acc1.deposit(2000)
acc1.withdraw(1000)
acc1.check_balance()
print("Account Number:", acc1.account_number)
print("Holder Name:", acc1._holder_name)
print("Current Balance is:", acc1._BankAccount__balance)