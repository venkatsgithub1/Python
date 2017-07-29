def partition(a,low,high):
  pivot=a[high]
  current=low
  for index in range(low,high):
    if a[index]<pivot:
      a[index],a[current]=a[current],a[index]
      current+=1
      
  a[current],a[high]=a[high],a[current]
  print(a)
  return current
  
def quicksort(a,low,high):
  if low<high:
    partitionIndex=partition(a,low,high)
    quicksort(a,low,partitionIndex-1)
    quicksort(a,partitionIndex+1,high)
  
a=[123,34,1,13,35,13,12,9,6]
quicksort(a,0,len(a)-1)
print(a)
