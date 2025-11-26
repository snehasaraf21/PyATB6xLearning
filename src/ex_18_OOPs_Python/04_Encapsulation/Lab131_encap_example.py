class Bank():
    def __init__(self,account_no,balance):
        self.__account_no = account_no#private
        self.balance = balance#public

    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance += amount

    def show_balance(self,is_auth):
        if is_auth == True:
            print(self.__account_no)
        else:
            print("Not Allowed!!")

icici = Bank("ICICI9243",100)
icici.deposit(100)
icici.check_balance()
#print(icici.__account_no)#cnt acess as its private
#only cahhies who is authorised to see the account no can access the private variable
icici.show_balance(True)
