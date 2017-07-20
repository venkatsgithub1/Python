n = int(input())
s = set(map(int, input().split())) 
commandCount=int(input())
while commandCount!=0:
    commandInput=input().split()
    command=commandInput[0]
    length=len(s)
    if command=='pop' and length>0:
        s.pop()
    elif command=='remove' and length>0:
        s.remove(int(commandInput[1]))
    else:
        s.discard(int(commandInput[1]))
    commandCount-=1
print(sum(s))
