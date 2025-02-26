# 31 create account class with 2 attributes - balance and account no
# create methods for debit ,credit and printing the balance
class bank_account:
    def __init__(self,balance,acc_no):
        self.balance =balance
        self.acc_no = acc_no

    def debit(self,deb_amount) :
        self.balance = self.balance - deb_amount
        print('Rs.',deb_amount,'was debited from account number',self.acc_no)

    def credit(self,cre_amount) :
        self.balance = self.balance + cre_amount
        print('Rs.',cre_amount,'was credited for account number',self.acc_no)
    
    def prnt_balance(self):
        print("The balance is :", self.balance)


customer = bank_account(20000,566802010011828)
customer.prnt_balance()
customer.debit(5000)
customer.prnt_balance()
customer.credit(10000)
customer.prnt_balance()