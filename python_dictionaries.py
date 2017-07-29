from pprint import pprint as pp

names_and_ages=[('John_Doe',32),('Jane Doe',31)]

# List of tuples can be converted into key value pairs.
dict1=dict(names_and_ages)

print(dict1)

# A dictionary doesn't maintain an order.

list1=[1,2,3,4,5]
dict2=dict(list(enumerate(list1)))
print(dict2)

phonetics=dict(a='alfa',b='bravo',c='charlie',d='delta',e='echo',f='foxtrot',g='golf')

print(phonetics,'dictionary using dict ()')

# To create a new dictionary with data in another dictionary.
phoneticsDict2=phonetics.copy()

phonetics['a']='alpha'

print(phonetics,'phonetics')
print(phoneticsDict2,'phoneticsDict2')

phoneticsDict3=dict(phoneticsDict2)

print(phoneticsDict3,'phoneticsDict3')

phoneticsFromHToL=dict(h='hotel',i='india',j='juliett',k='kilo',l='lima')

# To update one dictionary into another.
phonetics.update(phoneticsFromHToL)

print(phonetics,'phonetics after h to l updated')

groceries={'Oranges':4,'Apples':6,'Bananas':30}

groceries.update({'Oranges':10, 'Bananas':50})

print(groceries)

# Dictionary Iteration
for key in groceries:
    print("{key}=>{value}".format(key=key,value=groceries[key]))
    
# Dictionary iteration over values
for vals in groceries.values():
    print(vals)
    
# No need to use groceries.keys() since, by default
# dictionary is iterated over keys.
for key in groceries.keys():
    print("{key}=>{value}".format(key=key,value=groceries[key]))
    
# Key, value unpacking can be done using items() on
# dictionary.
for key,value in groceries.items():
    print("{key}=>{value}".format(key=key,value=value))
    
# in operator can be used only on keys.
print('Oranges' in groceries)

# del keyword can be used to remove a key value pair from
# the dictionary, can be applied on key.
del phonetics['l']

print(phonetics)

# In a dictionary, keys are immutable, but values can be 
# mutable.

# pretty printing.
pp(phonetics)
