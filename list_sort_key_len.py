list1=["hello","albert","doe"]

list1.sort()

# Here length is used a key for sorting. Hence we get
# sorted list items based on their length.
list1.sort(key=len)

print(list1)
