n=int(input())
str1=input()
lvl=0
valleycnt=0
belowSea=False
for chr1 in str1:
    if chr1=='D':
        lvl-=1
    else:
        lvl+=1
    if not(belowSea) and lvl<0:
        valleycnt+=1
        belowSea=True
    if lvl>=0:
        belowSea=False
print(valleycnt)
