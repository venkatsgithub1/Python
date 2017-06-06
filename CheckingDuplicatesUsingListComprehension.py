list1=[1,2,2,3,4,4,5,6,7,8,9]
temp=[]
[temp.append (x) for x in list1 if x not in temp]

print (temp)
