def Collatz (number):
    retVal=0
    if number%2==0:
        retVal=number//2
    else:
        retVal=3*number+1
    print (retVal)
    return retVal

n=int(input("Enter a number to commence Collatz Sequence:"))
while (n!=1):
    n=Collatz (n)
