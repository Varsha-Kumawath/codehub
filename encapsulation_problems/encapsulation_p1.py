class bank_account:

    def __init__(self, inital_balance=0):
        self.__balance= inital_balance

    @property
    def  display_balance(self):
            return f"Current balance:  {self.__balance}"

    # @display_balance.setter
    def display_deposit(self,amount):
        if(amount>0):
            self.__balance=amount+self.__balance
            return f" Amount deposited {self.__balance}"
            print(amount)
        else:
                print("invalid deposit amount")

    # @display_balance.setter
    def display_withdraw(self,amount):
        if (amount <= self.__balance):
            self.__balance -= amount
            return f" Amount withdrawal :  {amount}"
            print(amount)

        else:
            print("Insufficient amount")


b=bank_account()
b.display_deposit(5000)
b.display_withdraw(10)
print(b.display_balance)