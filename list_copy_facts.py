list1=[[1,2],[3,4]]
list2=list1[:]
print(list1 is list2) # False
print(list1==list2) # True
# but
print(list1[0]==list2[0]) # True, since two lists refer to same sub list.
list1[0]=[6,9]
print(list1[0]) # [6,9]
print(list2[0]) # [1,2]
print(list1[1] is list2[1]) # True, refers to same sublist.
print(list1[1] == list2[1]) # True still unmodified.
list1[1].append(5) # this operation also affects list2.
print(list1[1]) # [3,4,5]
print(list2[1]) # [3,4,5]
print(list1[1] is list2[1]) # True, refers to same sublist.
print(list1[1] == list2[1]) # True still unmodified.
print(list1)
print(list2)
