"""
	An introduction to class methods and static methods in Python.
"""

import datetime

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
	
	# class methods are not based on class instance,
	# they are to be used with cls variable which is
	# class itself.
	# Class methods can be used as alternative constructors.
	# They are called directly using class and not instance.
	# Class methods use decorator @classmethod to be declared
	# as class methods.
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount=amount
		
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split("-")
		return cls(first, last, pay)
	
	# if a method has a logical connection to the class
	# but need not use instance or class variables anywhere
	# in the method, then that class can be made a static method.
	# a static method uses decorator @staticmethod.
	@staticmethod
	def is_work_day(day):
		wkDay = day.weekday()
		if wkDay == 5 or wkDay == 6:
			return False
		return True
	
emp1 = Employee('John', 'Doe', 40000)
emp2 = Employee('Jane', 'Doe', 30000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

#	if someone want to create an employee object
#	using a string separated by a hyphen, below
#	usage works.

emp3 = Employee.from_string("Bob-Doe-35000")

print(emp3.email)
print(emp3.pay)

new_date = datetime.date(2017, 9, 23)

print("is new_date a workday: ", Employee.is_work_day(new_date))
