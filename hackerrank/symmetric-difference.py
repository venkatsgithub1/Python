m,mdata,n,ndata=int(input()),set(map(int,input().split())),int(input()),set(map(int,input().split()))
list1=sorted([x for x in list(mdata.union(ndata).difference(mdata.intersection(ndata)))])
for data in list1:
    print(data)
