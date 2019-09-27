# import heapq library
import heapq

list_1=[1,3,5,7,9]

# convert list into min heap
heapq.heapify(list_1)
print(list_1)

heapq.heappush(list_1, 6)
print(list(list_1))