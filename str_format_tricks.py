print("The age of {0} is {1}".format('John Doe',32))
# Same delimeter argument is used twice and refers to
# word 'Doe'.
print("{0} {1} and {2} {1} are not related I guess.".format('John','Doe','Jane'))

# If field names are used in sequence, they can be omitted.
print("{} is a {}".format('Python','language'))

# Named arguments are matched by using syntax:
# name=argName
print('{original_name} is spiderman'.format(original_name='Peter Parker'))

companiesTuple=('LG','Blue Star','Samsung')

print('{}, all manufacture air conditioners.'.format(companiesTuple))
print('{}, all manufacture air conditioners.'.format(','.join(companiesTuple)))

# tuples can be used to format arguments in a string.
# syntax: tuple1=(1,2) = {someAlias[0]} 
# and in format specify someAlias refers to tuple1 using
# someAlias=tuple1.
height=(5,10)
print('John Doe is {manHeight[0]} feet and {manHeight[1]} inches tall'.format(manHeight=height))

# tuple logic can also be used on modules.
import math
print("Some math constants: pi={m.pi}, e={m.e}".format(m=math))
# {module.constant:decimal places} 3 in below case.
print("Some math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))
