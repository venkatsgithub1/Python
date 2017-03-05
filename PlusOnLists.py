#first list
list1=[0,1]

#second list1
list2=[2,3]

#concatenate lists using '+' operator
list1+list2

print (list1)

print (list2)

#above two print statements print the same lists because the + concatenation wasn't assigned to 
#other list, '+' operator doesn't mutates the old lists, it outputs a new list, so an assignment
# of output is required.

list3=list1+list2

#below line produces combined results of list1 and list2
print (list3)
