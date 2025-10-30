class Account:
    def __init__(self, initial_balance):
        self._balance = initial_balance
        self._active = True 

    def freeze(self):
        self._active = False

    def unfreeze(self):
        self._active = True


class SavingsAccount(Account):
    def __init__(self, name, initial_balance, pin, daily_limit):
        super().__init__(initial_balance)
        self.name = name
        self.__pin = pin  # private
        self.daily_limit = daily_limit
        self.used_today = 0
        self.atm_requested = False
        self.cheque_requested = False

    def check_balance(self, pin):
        if pin != self.__pin:
            return "Invalid PIN"
        if not self._active:
            return "Account inactive"
        return self._balance

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            return "Invalid PIN"
        if not self._active:
            return "Account inactive"
        if amount > self._balance:
            return "Not enough balance"
        if self.used_today + amount > self.daily_limit:
            return "Exceeds daily limit"
        self._balance -= amount
        self.used_today += amount
        return f"Withdrawn {amount}, balance now {self._balance}"

    def deposit(self, amount, pin):
        if pin != self.__pin:
            return "Invalid PIN"
        if amount <= 0:
            return "Invalid deposit amount"
        self._balance += amount
        return f"Deposited {amount}, balance now {self._balance}"

    def request_atm_card(self):
        if self.atm_requested:
            return "ATM card already requested"
        self.atm_requested = True
        return "ATM card approved"

    def request_cheque_book(self):
        if self.cheque_requested:
            return "Cheque book already requested"
        self.cheque_requested = True
        return "Cheque book approved"

    def freeze_account(self):
        if not self._active:
            return "Already frozen"
        self.freeze()
        return "Account frozen"

    def unfreeze_account(self):
        if self._active:
            return "Already active"
        self.unfreeze()
        return "Account unfrozen"


class BusinessAccount(Account):
    def __init__(self, business_name, initial_balance, overdraft_limit, loan_limit):
        super().__init__(initial_balance)
        self.business_name = business_name
        self.overdraft_limit = overdraft_limit
        self.loan_limit = loan_limit
        self.cheque_requested = False

    def check_balance(self):
        if not self._active:
            return "Account inactive"
        return self._balance

    def withdraw(self, amount):
        if not self._active:
            return "Account inactive"
        if amount > self._balance + self.overdraft_limit:
            return "Amount exceeds overdraft"
        self._balance -= amount
        return f"Withdrawn {amount}, balance now {self._balance}"

    def request_loan(self, amount):
        if amount > self.loan_limit:
            return "Loan exceeds limit"
        self._balance += amount
        return f"Loan approved {amount}, balance now {self._balance}"

    def request_cheque_book(self):
        if self.cheque_requested:
            return "Cheque book already requested"
        self.cheque_requested = True
        return "Cheque book approved"
sav = SavingsAccount("Alice", 1000, "1234", daily_limit=500)
print(sav.check_balance("1234"))  
print(sav.check_balance("0000"))  
print(sav.withdraw(200, "1234"))  
print(sav.withdraw(600, "1234"))  
print(sav.deposit(300, "1234"))  
print(sav.request_atm_card())   
print(sav.request_atm_card())   
print(sav.request_cheque_book()) 
print(sav.freeze_account())           
print(sav.withdraw(50, "1234"))      
print(sav.unfreeze_account())         
bus = BusinessAccount("MyBusiness", 2000, overdraft_limit=500, loan_limit=10000)
print(bus.check_balance())             
print(bus.withdraw(2400))             
print(bus.withdraw(3000))             
print(bus.request_loan(5000))          
print(bus.request_loan(20000))         
print(bus.request_cheque_book())      