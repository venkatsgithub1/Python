"""
    An introduction to classes in Python.
"""
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay=pay
        self.email=self.first + "." + last + "@company.com"
    
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
emp1 = Employee('John', 'Doe', 40000)
emp2 = Employee('Jane', 'Doe', 30000)

print(emp1.fullname())
# or
print(Employee.fullname(emp1))
