def insertionsort(list1,listLen):
    counter=0
    for idx1 in range(1,listLen):
        rootElement=int(list1[idx1])
        idx2=idx1
        while idx2>0 and int(list1[idx2-1])>rootElement:
            list1[idx2]=list1[idx2-1]
            idx2-=1
            counter+=1
        list1[idx2]=str(rootElement)
    print(counter)
        
n=int(input())
data=list(map(int,input().split()))
insertionsort(data,n)
