class BankAccount:
    def __init__(self,Account_number,Balance):
        self.balance = Balance
        self.accountnumber = Account_number

    def get_account_number(self):
        return self.accountnumber
    
    def get_balance(self):
        return self.balance

    def set_balance(self,amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Error balance cant be negetive")

    # def set_account_number(self):
    #     self.accountnumber = 

    