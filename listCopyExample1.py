list1=list("LoremIpsum")
print(list1)
list1Copy=list1
print('list1\'s copy:',list1Copy)
# but
print(list1Copy is list1) # yes, here if we change data in list1, data changes in list1Copy too.
# but
list1Copy=list1[:]
# False, here if we change data in list1, data doesn't change in list1Copy.
# Since new list object.
# Also called shallow copy.
print(list1Copy is list1)
# but data is same.
print(list1Copy)
# Another example of shallow copy.
list2Copy=list1.copy()
print(list2Copy," list2Copy")
print(list2Copy is list1)
# Yet another example.
list3Copy=list(list1)
print(list3Copy," list3Copy")
print(list3Copy is list1)
