p=[1,2]

q=[3,4]

#appending q to p using append procedure.
p.append(q)

#printing below statement produces two elements and a third element as a list.
print (p)

#adding a new element to the end of list q.
q.append(5)

#below statement shows that it also append on q also effects p since,
#p stores the reference to list q, what happens in q also gets reflected in p.
print (p)

#the below statement produces the length of list p.
print (len(p))
