class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.__balance = balance  #private variables
        
        
    def deposit(self, amount):
        self.__balance += amount
        print(f'Deposited {amount}. New balance {self.__balance}') 
        
        
    def get_balance(self):
        return self.__balance  #controlled access
    
    
account = BankAccount('12345', 5000)

account.deposit(2000)
print(account.get_balance())             