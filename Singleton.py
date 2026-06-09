#Creating singleton class Bankmanager
class BankManager:
    _instance = None
    #Defining new using instance so that only one instance of class exists
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.accounts = []
        return cls._instance
    #Class functions
    def add_account(self, account_no):
        self.accounts.append(account_no)
    def show_accounts(self):
        print("Accounts:", self.accounts)
#Creating two objects of the class
b1 = BankManager()
b2 = BankManager()
b1.add_account(11)
b1.add_account(122)
b2.show_accounts()
#To check if class is singleton or not
print(b1 is b2)