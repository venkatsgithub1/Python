def digit_sum (n):
    sum=0
    for item in [int(temp) for temp in str(n)]: 
        sum+=item
    return sum
