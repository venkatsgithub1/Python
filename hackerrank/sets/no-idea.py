x,y = list(map(int,input().split()))[:]
z=list(map(int,input().split()))
a=set(map(int,input().split()))
b=set(map(int,input().split()))
count=0
for data in z:
    if data in a:
        count+=1
    elif data in b:
        count-=1
print(count)
