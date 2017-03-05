list1=[0,1]

list2=["a",[0,1,"b"]]

string1="Testing Length"

#below line produces length 2, since two elements are present.
print (len (list1))

#below line produces length 2, since len method counts outer elements and not elements inside.
print (len (list2))

#len can also be used on strings. Produces output 14.
print (len (string1))
