"""
    An introduction to classes in Python.
"""
class Employee:
    
    raise_amount = 1.04
    num_of_employees = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay=pay
        self.email=self.first + "." + last + "@company.com"
        Employee.num_of_employees += 1
    
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
    
emp1 = Employee('John', 'Doe', 40000)
emp2 = Employee('Jane', 'Doe', 30000)

print(emp1.fullname())
# or
print(Employee.fullname(emp1))

print(emp1.__dict__)
print(Employee.__dict__)

emp1.raise_amount=1.05

print(emp1.__dict__)
print(Employee.__dict__)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(Employee.num_of_employees)
