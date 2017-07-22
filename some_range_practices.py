list1=[1,4,5,6,8,11,12]

# not so pythonic.
for idx in range(len(list1)):
    print(list1[idx])

# instead use:
for data in list1:
    print(data)
    
# use enumerate if it's actually necessary to use index:
# tuple unpacking in line 13.
list1=['a','b','c','d','e','f']
for idx,data in enumerate(list1):
    print("index {} has data {}".format(idx,data))
