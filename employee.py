"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from typing import Any


class Employee:
    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commission = commission

    def __get_salary(self):
        salary_value = self.contract.calcSalary()
        print(salary_value)
        return salary_value

    def __get_commission(self):
        if self.commission != None:
            commission_value = self.commission.get_commission()
            print(commission_value)
            return commission_value
        else:
            print(0)
            return 0

    def get_pay(self):
        total = self.__get_salary() + self.__get_commission()
        print(self.name + ": " + str(total))
        return total

    def __str__(self): # TO DO
        return self.name

################## CONTRACT TYPES ##################

class Contract:
    def __init__(self):
        self.a = 21
    
class HourlyContract(Contract):
    contractType = "Hourly"
    def __init__(self, rate, hours):
        super().__init__()
        
        self.rate = rate
        self.hours = hours
    
    def calcSalary(self):
        return self.rate * self.hours

class MonthlyContract(Contract):

    contractType = "Monthly"

    def __init__(self, salary):
        super().__init__()
        
        self.salary = salary

    def calcSalary(self):
        return self.salary
        

################## COMMISSION TYPES ##################

class Commission:
    def __init__(self, commission):
        self.commission = commission
    
    def get_commission(self):
        return self.commission

class ContractCommission(Commission):
    def __init__(self, commission, contracts):
        super().__init__(commission)
        self.contracts = contracts

    def get_commission(self):
        return self.commission * self.contracts

class BonusCommission(Commission):
    def __init__(self, commission):
        super().__init__(commission)

    def get_commission(self):
        return self.commission
    
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlyContract(4000), None)
billie.get_pay()

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25, 100), None)
charlie.get_pay()

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlyContract(3000), ContractCommission(200, 4))
renee.get_pay()

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25, 150), ContractCommission(220, 3))
jan.get_pay()

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlyContract(2000), BonusCommission(1500))
robbie.get_pay()

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30, 120), BonusCommission(600))
ariel.get_pay()
