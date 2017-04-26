def is_int (x):
    lst=str(x).split(".")
    if len(lst)==1:
        return True  
    elif len(lst)==2 and lst[1]=="0":
        return True
    return False
