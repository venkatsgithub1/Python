a = int(input('Enter first number'))
b = int(input('Enter second number'))

if a>b:
    min1 = a
else:
    min1 = b

while(True):
    if min1%a==0 and min1%b==0:
        print('LCM is:', min1)
        break
    min1 += 1
