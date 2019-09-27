# import heapq library
import heapq

def main():
    list_1=[1,3,5,7,9]

    # convert list into min heap
    heapq.heapify(list_1)
    print(list_1)

    """"
    Output:
    [1, 3, 5, 7, 9]
    After heapifying the list.
       1
       /\
      3  5
     /\
    7  9
    """

    # heappush pushes data into heap and organizes it
    # appropriately.
    heapq.heappush(list_1, 6)
    print(list(list_1))
    """"
    Output:
    [1, 3, 5, 7, 9, 6]
    After heapifying the list.
        1
       / \
      3   5
     /\   /
    7  9 6
    """
    # we also have heappop, which pops the first element
    # in the list and heapifies the list.
    heapq.heappop(list_1)
    print(list_1)
    """
    heap gets rearranged as follows:
                3
               / \
              6   5
             / \
            7   9
            
    Here 3 becomes parent since 3 is minimum of all.
    """
    # heappushpop simultaneously pushes and pops same element.
    heapq.heappushpop(list_1, 2)
    print(list_1)

    # heapreplace simultaneously pushes and pops same element.
    heapq.heapreplace(list_1, 2)
    print(list_1)
    """
        heap gets rearranged as follows:
                    2
                   / \
                  6   5
                 / \
                7   9

        Here 3 is popped out, 2 is replaced as parent.
        """

    # nlargest
    print("{} are the 3 largest elements in that order".format(heapq.nlargest(3, list_1)))

    # nsmallest
    print("{} are the 3 smallest elements in that order".format(heapq.nsmallest(3, list_1)))

if __name__ == "__main__":
    main()